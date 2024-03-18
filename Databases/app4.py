import sqlite3
#if we wnat to delete our database ,we use(":memory:") in placee of customer.db
conn=sqlite3.connect("customer.db")
a=conn.cursor()
many_customers=[("Ben","Mugo","Ben_Mugo@gmail.com"),
                ("Esther","Wanjiku","Esther_wanjiku@gmail.com"),
                ("Beatrice","Mugo","Beatrice_Mugo_Mugo@gmail.com")]

a.execute("""CREATE TABLE  IF NOT EXISTS customers(
          id  INTEGER PRIMARY KEY,
          first_name TEXT NOT NULL,
          last_name TEXT NOT NULL,
          email   TEXT NOT NULL
);
""")
a.executemany("INSERT INTO customers VALUES(?,?,?)",many_customers)
a.execute("INSERT INTO customers VALUES('Esther','Wanjiku','estherwanjiqu@gmail.com')")
print("Table created successfully")
# a.execute("""UPDATE customers SET last_name='Nyagothii'  WHERE last_name='Mugo'
# """)
a.execute("UPDATE cuctomers SET email='Beatrice_Nyaguthii' WHERE last_name='Nyaguthii'")
a.execute("SELECT * FROM customers")
#a.execute("DELETE FROM customers WHERE first_name='Ben'")
a.execute("SELECT * FROM customers ")
items=a.fetchmany(2)
for item in items:
    print(item[0] + "" + item[1]+ "/t" +item[2])

conn.commit()
conn.close()