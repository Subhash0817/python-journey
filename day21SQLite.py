import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    name TEXT,
    rating INTEGER
)
""")

connection.commit()

print("Table Created!")

connection.close()

import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM movies")

print(cursor.fetchall())

connection.close()


import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM movies")

movies = cursor.fetchall()

for movie in movies:
    print(movie)

connection.close()

import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

cursor.execute("""
UPDATE movies
SET rating = 9
WHERE name = "Interstellar"
""")

connection.commit()

print("Movie Updated!")

connection.close()



import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO movies(name, rating)
VALUES("Your Name", 9)
""")

cursor.execute("""
INSERT INTO movies(name, rating)
VALUES("Attack on Titan", 10)
""")

cursor.execute("""
INSERT INTO movies(name, rating)
VALUES("John Wick", 9)
""")

connection.commit()


cursor.execute("SELECT * FROM movies")

movies = cursor.fetchall()

for movie in movies:
    print(movie)

cursor.execute("""
UPDATE movies
SET rating = 10
WHERE name = "John wick"
""")

connection.commit()

print("Movie Updated!")
connection.close()