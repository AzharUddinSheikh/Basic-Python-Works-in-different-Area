import sqlite3
import json
from pathlib import Path

movies = json.loads(Path('movies.json').read_text())
print(movies)

# sqlite3.connect('db.sqlite3') this method create one data base if it doesnot exists


with sqlite3.connect('db.sqlite3') as conn:
    command = "INSERT INTO movies VALUES(?,?,?)"
    # question mark is the placeholder so we ll supply values here
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()

'''here we get an error we dont have sqlite data base so download it create table movis with 3 columns 
run code again'''

# reading data from data base

with sqlite3.connect('db.sqlite3') as conn:
    command = "SELECT * From movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    '''fetch all method ll fetch all data in one go'''
    movies = cursor.fetchall()
    print(movies)

    # execute command take 2 para command and values in tuple format
