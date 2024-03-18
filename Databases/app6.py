import sqlite3
#Database creation
conn=sqlite3.connect("data.db")
cursor=conn.cursor()
conn.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
             email TEXT NOT NULL            
              
);""")
#iNSERT DATA
many_customers=[("Ben","Mugo","Ben_Mugo@gmail.com"),
                ("Esther","Wanjiku","Esther_wanjiku@gmail.com"),
                ("Beatrice","Mugo","Beatrice_Mugo_Mugo@gmail.com")]
conn.executemany("INSERT INTO  users(first_name,last_name,email) VALUES(?,?,?)",(many_customers))
row=conn.execute("SELECT * FROM users ").fetchone()
print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
conn.commit()
conn.close()
    