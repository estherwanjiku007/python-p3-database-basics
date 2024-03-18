import sqlite3

class Databases:
    def __init__(self,db_name):
        self.conn=sqlite3.connect(db_name)
        self.cur=self.conn.cursor()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS employee(
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            age INTEGER, 
                            position TEXT              
                            )''')
        self.conn.commit()
    
    def insert_employees(self,name,age,position):
        self.cur.execute('''INSERT INTO teachers(name,age,position) VALUES(?,?,?)''',(name,age,position))
        self.conn.commit()

    def get_all_employees(self):
        self.cur.execute('''SELECT * FROM teachers''')
        return self.cur.fetchall()
    
    def close(self):
        return self.conn.close()
    
my_db=Databases("employee.db")
my_db.insert_employees("Esther Wanjiku",20,"System analyst")
my_db.insert_employees("Beatrice Nyagothii",50,"pricipal")
my_db.get_all_employees()
my_db.close()
# my_db.insert_employees("Esther Wanjiku",20,"TECH dev")



        

       
     