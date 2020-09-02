# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id BIGSERIAL PRIMARY KEY,
        start_time TIME NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR(10) NOT NULL,
        song_id  VARCHAR(20),
        artist_id VARCHAR(20),
        session_id INT NOT NULL,
        location VARCHAR(100),
        user_agent VARCHAR(200)
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        first_name  VARCHAR(20),
        last_name  VARCHAR(20),
        gender  VARCHAR(1),
        level VARCHAR(10) NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id  VARCHAR(20) PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        artist_id VARCHAR(20),
        year INT,
        duration DECIMAL NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        location VARCHAR(100),
        latitude REAL,
        longitude REAL
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIME NOT NULL,
        hour SMALLINT,
        day SMALLINT,
        week SMALLINT,
        month SMALLINT,
        year SMALLINT,
        weekday SMALLINT
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s);
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
    INSERT INTO TIME (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id FROM
    songs s
    INNER JOIN
    artists a
    ON s.artist_id = a.artist_id
    WHERE s.title=%s AND a.name=%s and s.duration=%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]