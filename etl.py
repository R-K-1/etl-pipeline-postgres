import os
import glob
import psycopg2
import json
import pandas as pd
from sql_queries import *

artist_ids = set()
user_ids = set()

def process_song_file(cur, filepath):
    # open song file
    df = {}
    with open(filepath) as f:
        df = json.load(f)

    artist_id = df['artist_id']

    # insert song record
    song_data = []
    song_data.append(df['song_id'])
    song_data.append(df['title'])
    song_data.append(artist_id)
    song_data.append(df['year'])
    song_data.append(df['duration'])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    if artist_id not in artist_ids:
        artist_ids.add(artist_id)
        artist_data = []
        artist_data.append(artist_id)
        artist_data.append(df['artist_name'])
        artist_data.append(df['artist_location'])
        artist_data.append(df['artist_latitude'])
        artist_data.append(df['artist_longitude'])
        cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = ''    
    with open(filepath) as f:
        df = pd.read_json(f, lines=True)

    # filter by NextSong action
    df = df[df.page.eq("NextSong")]
    
    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    
    for i, row in df.iterrows():
        r = []
        r.append(row.ts.time())
        r.append(row.ts.hour)
        r.append(row.ts.day)
        r.append(row.ts.week)
        r.append(row.ts.month)
        r.append(row.ts.year)
        r.append(row.ts.weekday())
        cur.execute(time_table_insert, r)

    # insert user records
    for i, row in df.iterrows():
        user_id = int(row.userId)
        if user_id not in user_ids:
            user_ids.add(user_id)
            r = []
            r.append(user_id)
            r.append(row.firstName)
            r.append(row.lastName)
            r.append(row.gender)
            r.append(row.level)
            cur.execute(user_table_insert, r)

    # insert songplay records
    for i, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        songid = None
        artistid = None
        if results:
            songid, artistid = results

        # insert songplay record
        songplay_data = []
        songplay_data.append(row.ts.time())
        songplay_data.append(row.userId)
        songplay_data.append(row.level)
        songplay_data.append(songid)
        songplay_data.append(artistid)
        songplay_data.append(row.sessionId)
        songplay_data.append(row.location)
        songplay_data.append(row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()