import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    roll_no INTEGER,
    marks INTEGER
)
""")

conn.commit()

print("Table Created")

cursor.execute(
    "INSERT INTO students VALUES (?, ?, ?)",
    ("Subhash", 101, 95)
)

conn.commit()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

conn.close()