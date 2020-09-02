# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (
        songplay_id BIGSERIAL PRIMARY KEY,
        start_time TIMESTAMP NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR(10) NOT NULL,
        song_id  VARCHAR(20) NOT NULL,
        artist_id VARCHAR(20),
        session_id INT NOT NULL,
        location VARCHAR(100),
        user_agent VARCHAR(200)
    );
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id INT PRIMARY KEY,
        first_name  VARCHAR(20),
        last_name  VARCHAR(20),
        gender  VARCHAR(1),
        level VARCHAR(10) NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id  VARCHAR(20) PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        artist_id VARCHAR(20),
        year INT,
        duration REAL NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        location VARCHAR(100),
        latitude REAL,
        longitude REAL
    );
""")

time_table_create = ("""
    CREATE TABLE time (
        start_time TIMESTAMP NOT NULL,
        hour VARCHAR(2),
        day VARCHAR(15),
        week VARCHAR(15),
        month VARCHAR(15),
        year INT,
        weekday VARCHAR(15)
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]