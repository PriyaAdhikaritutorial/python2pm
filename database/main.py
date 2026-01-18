# import sqlite3

# conn = sqlite3.connect("database/college.sqlite3")
# mycrs = conn.cursor()

# def create_table():
#     table = """
#     CREATE TABLE IF NOT EXISTS student(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         email TEXT UNIQUE NOT NULL,
#         address TEXT NOT NULL
#     )
#     """
#     mycrs.execute(table)
#     conn.commit()

# def insert(name, email, address):
#     insert_query = """
#     INSERT INTO student(name, email, address)
#     VALUES (?, ?, ?)
#     """
#     mycrs.execute(insert_query, (name, email, address))
#     conn.commit()
#     print("Data inserted successfully")

# create_table()

# name = input("Enter your name: ")
# email = input("Enter your email: ")
# address = input("Enter your address: ")

# insert(name, email, address)
# def create_employee_table():
#     table="""
#     CREATE TABLE IF NOT EXISTS employee (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     address TEXT NOT NULL
#     )
#     """
#     mycrs.execute(table)
#     conn.commit()


# def insert_employee(name,email,address):
#     insert_query= """
#     INSERT INTO employee (name,email,address)
#     VALUES (?,?,?)
#     """
#     mycrs.execute(insert_query, (name, email, address))
#     conn.commit()
#     print("Employee Data inserted successfully")

# create_employee_table()
# emp_name=input("Enter your name:")
# emp_email=input("Enter your email:")
# emp_address=input("Enter your address:")
# insert_employee(emp_name,emp_email,emp_address)




# def display():
#     sql = "SELECT * FROM student"
#     data = mycrs.execute(sql)
    # print (data.fetchall())
    # print (data.fetchone())
#     print(data.fetchmany(3))

# display()

# def update(name,email,address,id):
#     updateSql="""UPDATE student SET name=?,email=?,address=? WHERE id=?"""
#     mycrs.execute(updateSql,(name,email,address,id))
#     conn.commit()
#     print ("Data updated successfully")
# update("sam","sam@gmail.com","bkt",2)

# def delete(id):
#     sql = "DELETE FROM student Where id=?"
#     mycrs.execute(sql,(id,))
#     conn.commit()
#     print("Data deleted duccessfully")

# delete(1)



# import tkinter as tk

# app= tk.Tk()
# app.title("student Record Management system")
# app.geometry("600x700")

# sNameLebel =tk.Label(app, text="student Name: ")
# sNameLebel.grid (row=0, column=0, padx=10, pady=10)
# sName=tk.Entry(app)
# sName.grid(row=0, column=3, padx=10, pady=10)
# nLebel= tk.Label(app, text="Nepali  marks: ")
# nLebel.grid(row=1, column=0, padx=10, pady=10)
# nMarks=tk.Entry(app)
# nMarks.grid(row=1, column=3, padx=10, pady=10)
# eLebel= tk.Label(app, text="English marks: ")
# eLebel.grid(row=2, column=0, padx=10, pady=10)
# eMarks=tk. Entry(app)
# eMarks.grid(row=2, column=3, padx=10, pady=10)
# mLebel=tk.Entry(app ,text="Math marks: ")
# mLebel.grid(row=3, column=0, padx=10, pady=10)
# sLebel=tk.Entry(app, text="Science marks: ")
# mMarks= tk.Entry(app)
# mMarks.grid(row=3, column=3, padx=10, pady=10)
# sLebel= tk.Label(app,text="Social marks: ")
# sLebel.grid(row=4, column=0, padx=10, pady=10)
# sMarks= tk.Entry(app)
# sMarks.grid(row=4, column=3, padx=10, pady=10)
# cLebel=tk. Label(app, text="Computer marks: ")
# cLebel.grid(row=5, column=0, padx=10, pady=10)
# cMarks=tk.Entry(app)
# cMarks.grid(row=5, column=3, padx=10, pady=10)

# def add_record():
#     sName=sName.get()
#     nep=nMarks.get()
#     eng=eMarks.get()
#     mat=mMarks.get()
#     sci=sMarks.get()
#     soc=sMarks.get()
#     comp=cMarks.get()

#     print(nep, eng, mat, sci, soc,comp)

# button= tk.Button(app, text="Add Record", command=add_record)
# button.grid(row=6, column=3, padx=10, pady=10)

# app.mainloop()




import sqlite3
conn=sqlite3.connect("database/ecommerce.sqlite3")
mycrs= conn.cursor()
def create_category_table():
    table= """
    CREATE TABLE IF NOT EXISTS category(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
    """
     
    mycrs.execute(table)
    conn.commit()
def create_product_table():
    table="""
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cat_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    price INTEGER NOT NULL, 
    FOREIGN KEY (cat_id) REFERENCES  category(id)
    )
    """
    mycrs.execute(table)
    conn.commit()
create_category_table()
create_product_table()

def cat_insert(name):
    sql=f"INSERT INTO category(name) VALUES('{name})"
    mycrs.execute(sql)
    conn.commit()
    print("category inserted")

    cat_insert("laptop")
    cat_insert("mobile") 
    cat_insert("toshiba") 

def create_user_table():
    table= """
    CREATE TABLE IF NOT EXISTS users(
    uid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE  NOT NULL,
    address TEXT NOT NULL
    )
    """
    mycrs.execute(table) 
    conn.commit() 

# create_user_table()
# create_category_table()
# create_product_table()

# def insert_user(uid, name, email, address):
#     mycrs.execute(
#     "INSERT INTO users(uid, name, email, address)VALUES (?, ?, ?, ?)", 
#     (uid, name, email, address)
#     )
    
#     conn.commit()

# insert_user(1, "Ram", "ram@gmail.com", "KTM")
# insert_user(2, "Sita", "sita@gmail.com", "Pokhara")
# insert_user(3, "Gita", "gita@gmail.com", "Bhaktapur")
# insert_user(4, "Rita", "rita@gmail.com", "Birjung")
     
def create_Order_table():
    table= """
    CREATE TABLE IF NOT EXISTS orders(
    oid INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL
    )
    """
    mycrs.execute(table) 
    conn.commit() 

create_user_table()
create_category_table()    
create_product_table()
create_Order_table()








# user_table
# uid, name, email, address 
# 1,ram,ram@gmail.com, ktm
# 2,sita,sita@gmail.co , pokh

# category_table
# cid,user_id, cat_name


# product_table
# id,category_id , user_id ,  price, title, quantity
# 1,1,2,dell Inspiron, 55000, 10

# order_table
# oid, product_id, user_id, quantity
# 1,1,2,5
# 2,3,2,10