import sqlite3 
class Databases:
    def __init__(self):
        self.conn=sqlite3.connect("My_database.db")
        self.cursor=self.conn.cursor()
        self.cursor.execute("""CREATE TABLE If NOT EXISTS main_table(
                            ID INTEGER PRIMARY KEY,
                            log INTEGER NOT NULL,
                            Password TEXT NOT NULL
        ); 
""")
    def db_console(self):
        c_query=input("Enter your query")
        self.cursor.execute(c_query)
        self.conn.commit() 

    def add_value(self,log,pword):
        self.cursor.execute("INSERT INTO main_table(log,password) VALUES(?,?)",(log,pword))
        self.conn.commit()
    
    def check_table(self):
        for row in self.cursor.execute("SELECT * FROM main_table").fetchall():
            print(row)
            self.conn.commit()
    
    def close(self):
        self.conn.close()

    def validate_values(self):    
        first_test=self        
        first_test.add_value(1,"password123")
        first_test.check_table()
        first_test.close()

    
     