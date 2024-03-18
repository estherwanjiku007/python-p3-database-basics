#import 
import sqlite3

#Create the database
conn=sqlite3.connect("moringa.db")
#creating our tables-students,tms, tms_students
#execute command allows us to execute our sql engine
conn.execute('''CREATE TABLE IF NOT EXISTS students(
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL         
); ''')
conn.execute('''CREATE TABLE IF NOT EXISTS tms(
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             staff no INTEGER
             
);''')
conn.execute('''CREATE TABLE IF NOT EXISTS tms_students(
             id INTEGER PRIMARY KEY,
             tmsid , 
             studentsid INTEGER,
             FOREIGN KEY (tmsid) REFERENCES tms(id),
             FOREIGN KEY (studentsid) REFERENCES students(id)      
                 
);  ''')
#CRUD
name="Esther Wanjiku"
email="estherwanjiqu@gmail.com"
#Insert query
conn.execute("INSERT INTO students(name,email) VALUES (?,?)",(name,email))
conn.execute("INSERT INTO students(name,email) VALUES (?,?)",("Mary","Mary@gmail.com"))
conn.execute("INSERT INTO students(name,email) VALUES (?,?)",("Ben","Ben_mugo05@gmail.com"))
conn.execute("UPDATE  students SET name='Beatrice' WHERE id=1")
#Read a record using the select statement
result=conn.execute("SELECT * FROM students ")
#loop thru the result 
for row in result:
    print(f"id:{row[0]}, name:{row[1]},email:{row[2]}")
#commit changes
conn.commit()
#close changes
conn.close()
