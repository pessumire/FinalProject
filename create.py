import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS todo (
              Task TEXT,
              Status TEXT)''')
conn.commit
