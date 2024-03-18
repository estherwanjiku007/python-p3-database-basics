class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property
    def email(self):
        return "{} .{}".format(self.first,self.last)
    
    @property
    def full_name(self):
        return "{} {}".format(self.first,self.last)
    
    def __repr__(self):
     return "Employee({},{},{})".format(self.first,self.last,self.pay)

    def add_employee(self):
       e.execute("INSERT INTO employees(first,last,pay) VALUES(?)",(Employee.__repr__(self)))
import sqlite3
conn=sqlite3.connect("employee.db")
e=conn.cursor()
e.execute("""CREATE TABLE  IF NOT EXISTS employees(
          first TEXT NOT NULL,
          last TEXT NOT NULL,
          pay INTEGER NOT NULL
);
          """)
e.execute("INSERT INTO employees(first,last,pay) VALUES(?,?,?)",("Esther","Wanjiku",500000))
e.execute("INSERT INTO employees(first,last,pay) VALUES(?,?,?)",("Ben","Mugo",500000))
e.execute("INSERT INTO employees(first,last,pay) VALUES(?,?,?)",("Beatrice","Nyagothii",500000))
#e.execute("INSERT INTO employees(first,last,pay) VALUES(?)",(Employee.__repr__()))
employee1=Employee("Jane","Njeri",5000000)
c=e.execute("SELECT * FROM employees   ")
a=c.fetchall()

for c in range(len(a)):
   print(a[c])
conn.commit()
conn.close()


