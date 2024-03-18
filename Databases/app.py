#Databases 
#A structured collection of data that is organized and managed in a wya hat allows effective manipulation
##TYPES
#  Relational databases:organizes dat inot rows and columns and establishes the relationship using keys
#examples:mySql,Oracle DB,SQLite
#noSQL:non-relational databases.Theyre simply unstructured,structured or structured data
#3:Document_databases:Store data in a 
#Fundamentals when designing a database
         #Identify the requirements
        #Conceptual design:Use of ER diagrams(dbdiagram.io)
#        Normalize the data:SSOT
#        Define the keys:Identify the primary and foreign keys
#1.Import the package
import sqlite3
#Create the database
conn=sqlite3.connect("moringa.db")

#create the table
#students,tms,tms_students
conn.execute('''CREATE TABLE IF NOT EXISTS students(
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NULL

);
''')     #execute command allows u st o execute the 
conn.execute('''CREATE TABLE IF NOT EXISTS tms(
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NULL,
             staffno INTEGER NOT NULL

);
''')    
conn.execute('''CREATE TABLE IF NOT EXISTS student_tms(
             id INTEGER PRIMARY KEY,
             tmsid INTEGER,
             studentsid INTEGER, 
             FOREIGN KEY(tmsid) REFERNCES tms(id),
             FOREIGN KEY(studentsid) REFERNCES students(id)          

);
''') 
name="Esther Wanjiku" 
email="estherwanjqu@gmail.com"

conn.execute("INSERT INTO students(name,email) VALUES (??),(n)")
  


conn.commit()
conn.close()