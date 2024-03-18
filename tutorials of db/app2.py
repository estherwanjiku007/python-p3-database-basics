import sqlite3
connection=sqlite3.connect("data.db")
conn=connection.cursor()

conn.execute("""CREATE TABLE IF NOT EXISTS beans(
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 method TEXT NOT NULL,
                 rating INTEGER NOT NULL
    ) """)
connection.commit()
conn.close()