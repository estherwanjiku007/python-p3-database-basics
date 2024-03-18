import sqlite3
connection=sqlite3.connect("schoolreg.db")
conn=connection.cursor()
conn.execute("""CREATE TABLE IF NOT EXISTS registration(
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age INTEGER NOT NULL,
             birth_date TEXT NOT NULL,
             email TEXT NOT NULL
)""")

students_registered=[
    ("Mary_Wambui",14,"14/03/2010","mary_wambui@gmail.com"),
    ("Esther_Wanjiku",20,"23/09/2004","esther_wanjiku@gmail.com"),
    ("Faith_Chege",15,"15/03/2010","faith_chege@gmail.com"),
     ("Faith_Njeri",30,"15/03/2020","faith_njeri@gmail.com")
]
conn.executemany("INSERT INTO registration(name,age,birth_date,email) VALUES(?,?,?,?)",(students_registered))
conn.execute("UPDATE registration SET name='Beatrice_Nyagothii' WHERE name='Faith_Chege'")
conn.execute("UPDATE registration SET email='Beatrice_Nyagothii@gmail.com' WHERE name='Beatrice_Nyagothii'")
conn.execute("UPDATE registration SET name='Ben_Mugo' WHERE name='Faith_Njeri'")
conn.execute("UPDATE registration SET email='Ben_Mugo@gmail.com' WHERE name='Ben_Mugo'")
all_info=conn.execute("SELECT  * FROM registration   ORDER BY name DESC LIMIT 10 ").fetchall()
for info in range(len(all_info)):
    #print(f"{all_info[0]} ")
    print(f"{all_info[0]} {all_info[1]} {all_info[2]} {all_info[3]}")