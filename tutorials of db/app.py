import sqlite3
conn=sqlite3.connect("tutorial.db")
def create_table():
    conn.execute("""CREATE TABLE IF NOT EXISTS stuff_to_plot(
                 unix REAL NOT NULL,
                 datestamp TEXT NOT NULL,
                 keyword TEXT NOT NULL,
                 value REAL NOT NULL
                 
    )""")

def data_entry():
    conn.execute("INSERT INTO stuff_to_plot VALUES(?,?,?)",('15-03-24','Python',5))
    conn.execute("INSERT INTO stuff_to_plot VALUES(?,?,?)",('15-03-24','Python',5))

    conn.commit()
    conn.close()

    data_entry()