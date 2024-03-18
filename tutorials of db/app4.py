import sqlite3

class Employees:
    def __init__(self,emp_id,name,position):
        self.emp_id=emp_id
        self.name=name
        self.position=position

class Databases:
    def __init__(self,db_name):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
                            emp_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            position TEXT NOT NULL                           
        )''')
        self.conn.commit()

    def insert_employee(self,all_employees):
        self.cursor.executemany('''INSERT INTO employees(name,position) 
                            VALUES(?,?)''',(all_employees))
        self.conn.commit()

    def check_table(self):
        employees=self.cursor.execute("SELECT * FROM employees").fetchall()
        for an_employee in employees:
            print(f"{an_employee[0]} {an_employee[1]} {an_employee[2]}")
        self.conn.commit()
        
    def close(self):
        self.conn.close()

#USAGE
if __name__=="__main__":
    my_db=Databases("company.db")
    my_db.create_table()

#Data
all_employees=[
("Esther Wanjiku","Developer"),
("Beatrice Nyagothii","general Manager")

]
my_db.insert_employee(all_employees)
my_db.check_table()
my_db.close()
    
