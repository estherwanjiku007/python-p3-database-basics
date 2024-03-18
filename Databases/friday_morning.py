#ORMS helps us to interact with a relational database DB using an oop language
#Allows us t workwithidatabase entities
 #1. Simpplifies our opretions
 #2.Makes our code readable and maintainable
import  sqlite3
#PRODUCTS table-name,table
#nB :Tablees are the classes
#Tables columns:==attrs
#Table rows==object instances
class Product:
    conn=sqlite3.connect("products.db")
    cursor=conn.cursor()
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
        
    def save():
        Product.cursor.execute("""INSERT INTO products(id,name,price) VALUES(?,?,?),(self.id,self.name.self.price)""")
        Product.conn.commit()
        Product.conn.close()

    def createzz():
        conn=sqlite3.connect("")