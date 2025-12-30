# n=1
# total=0

# while n<=10:
#     total+=n
#     n+=1

#     print(total)


# n = 1
# even =0
# odd=0

# while n<=25:
#     if n%2==0:
#         even+=1
#     else:
#         odd+=1
#         n+=1 
#         print("total even number is ", even )
#         print("total odd number is ", odd )


# name1="Ram"
# name2="sita"
# n=1
# while n<=10:
#     if n<=5:
#      print(name1)
#     else:
#      print(name2)
#      n+=1

# n = 1

# while n<=5:
#     print(n)
#     n+=1


# n = 5

# while n>=1:
#     print(n)
#     n-=1



# name = "priya adhikari"
# n = 1
# while n<=10:
#     print(name)
#     n+=1


# i =1 
# while 1<=i:
#       print("hi")
      # i+=1


#  WAP to enter number of students : 5 enter the name of students
    

# a = int(input(f"Enter the number of students : "))

# students=[]
# x=0
# while x<=a:
#       name= input("Enter name of students:")
#       students.append(name)
#       x+=1
# print("List of the students: ",students)



# data =['ram','hari','gita','sita']
# x=0

# while x<len(data):
#     print("hello", "data[x]")
#     x+=1

# numbers=[23,56,78,97,67]
# total=0
# x=0
# while x<len(numbers):
#     total+=numbers[x]
#     x+=1

# print("Total is",total)

# data =[1,3,6,8,9,12,45]
# x=0
# while x<len(data):
#       if data[x]%2==0:   
#             print(data[x])
#       x+=1



# x = 1
# while x<=10:
# #     print(f"5x{x}={x*5}")
#   print("5 x",x,"=",x*5)
#   x+=1



# a= int(input("Enter the number of students :"))
# numbers=[]
# x=0

# while x<a:
#     n=int(input("Enter number:"))
#     if n%2==0:
#        numbers.append(n)
#     x+=1

# print("Even number list:",numbers)


# for x in range (1,11):
#     print(x, end=" ")

# for x in range (10, 1,-1):
#     print(x, end=" ")


# data=['ram','sita','gita','hari']
# for name  in data:
#     print(name)



# numbers=[1,2,3,6,7,9,11,12,14,15,16] 
# even=0  
# for n in numbers:
#     if n%2==0:
#         print(n)


# numbers=[1,3,6,7,9,11,12,15,17]
# for n in numbers:
#     if n==3 or n==7 or n==9 or n==15 or n==16:
#         print(n)
        


# data=['ram','sita','gita','hari','shyam']
# for names in data:
#          print(data[0], end=" ")

# data=['ram','sita','gita','hari','shyam']
# for names in data:
#         print(data[1],end=" ")   


# for n in range(1,16):
#         if n<=5:
#                 print("Ram")
#         elif n>5 and n <=10:  
#                 print("Sita")
#         else:
#                 print("Gita")  


# x = 1
# for x in range(1,11):
#     print("8 x",x,"=",x*8)
#     x+=1   



# data=[
# {'name':'ram','gender':'male'},
# {'name':'sita','gender':'female'},
# {'name':'hari','gender':'male'},
# {'name':'madan','gender':'male'},
# ]  

# total_users =?
# total_male =?
# total_female =?
# total_users = len(data)

# total_male = sum(1 for user in data if user['gender'] == 'male')
# total_female = sum(1 for user in data if user['gender'] == 'female')

# print("Total Users:", total_users)
# print("Total Male:", total_male)
# print("Total Female:", total_female)



# for loop
# users=[]

# num= int(input ("Enter the numnber of users: "))

# x=1

# while x<=num:
#     name=input("Enter username: ")
#     users.append(name)
#     x+=1

# for user in users:
#     print(f'Hello{user}')


# Enter the students 
# five subject marks
# total 
# div
# per    

# users=[]

# num= int(input("Enter the number of students: "))

# x=1

# while x<=num:
#     name=input("Enter studentname: ")
#     users.append(name)
#     x+=1


# sub=("math", "science", "nepali", "social", "english")
# marks=[]
# print("=======welcome to college======")
# num=int(input("Enter the number of students: "))
# x=1
# while x <= num:
#  print(f"~~~~~~~~~~~Student No: {x}~~~~~~~~~~~~~~")
#  eng=float(input("Enter the marks of english: "))
#  sci=float(input("Enter the marks of science: "))
#  math=float(input("Enter the marks of math: "))
#  soc=float(input("Enter the marks of social: "))
#  nep=float(input("Enter the marks of nepali: "))
#  total= nep+soc+math+sci+eng
#  marks.append(total)
#  x+=1

# sId=1
# for total in marks:
#    per=total/5
# print(f"~~~~~~~~~~~~~sId: {sId}~~~~~~~~~~~~~")
# print(f"Total: {total}")
# print(f"Percentage: {per}")
# if per> 35 and per< 50:
#    print("B grade")
# elif per> 50 and per< 70:
#    print("A grade")
# elif per> 70 and per< 100:
#    print("A+ grade")
# else:
#    print("c grade")

# sId+=1    



# for x in range(1,11):
#     if x==3 or x==6 or  x==9:
#            continue
#     print(x)



# students=['ram', 'sita', 'gita', 'shyam']
# name=int(input("Enter the name of student"))

# for st in students:
#     if st==name:
#            is_found= True


# if is_found:
#       print(f"wellcome: {name}")
# else:
#       print("name not found", name)

# students= Data=[
#       {"username":"admin", "password": "admin02"},
#       {"username": "hari", "password": "hari09"},
#       {"username": "sanskrit", "password": "sanskrit98"},
# ]    

# username= (input("Enter the username: "))
# password= (input ("Enter the password: "))


# category=[
# {'cid':1, "name": "Laptop"},
# {"cid": 2, "name": "Mobile"},
# {"cid": 3, "name": "Tv"},

# ]

# products=[
#     {"pid":1, "cid":1, "product_name": "dell", "price": 20000, 'quantity': 5},
#     {"pid":2, "cid":1, "product_name": "mac", "price": 50000, 'quantity': 10},
#     {"pid":2, "cid":2, "product_name": "mi", "price": 15000, 'quantity': 50},
#     {"pid":2, "cid":3, "product_name": "sony", "price": 17000, 'quantity': 10},
# ]


# search= input("Enter the category name : ").title()
# is_found=False
# for cat in category:
#     if search ==cat['name']:
#         is_found=True
#         for product in products:
#             if cat['cid']==product['cid']:
#                 print(product)


# if not is_found:
#     print("product not found")
    


# authors=[
#     {"aid":1, "username":'admin', 'password':'admin002'},
#     {"aid":2, "username":'mike', 'password':'mike002'},
#     {"aid":3, "username":'dustin', 'password':'dustin002'},
#     {"aid":4, "username":'lucas', 'password':'lucas002'},
# ]
# books=[
#     {'bid':1 ,'author_id':1, 'title':"Python and django", 'price':2000, "quantity":5},
#     {'bid':2 ,'author_id':1, 'title':"Javascript", 'price':2000, "quantity":2},
#     {'bid':3 ,'author_id':2, 'title':"Java", 'price':2000, "quantity":5},
#     {'bid':4 ,'author_id':2, 'title':"Html and css", 'price':2000, "quantity":2},
#     {'bid':5 ,'author_id':2, 'title':"Database", 'price':2000, "quantity":3},

# ]

# name=input("Enter the username: ").lower()
# pw=input("Enter the password: ").lower()

# author_found==False
# for user in authors:
#  if user['username']==name and user['password']==pw:




books = [
    {'bid':1, 'title':"python and django", 'price':2000, 'quantity':5},
    {'bid':2, 'title':"javascript", 'price':3000, 'quantity':3},
]
# num=int(input("Enter the number of books: "))
# x=1
# while x <=num:
#     title= input('Enter book title: ')
#     price= float(input("Enter the book price: "))
#     quantity= int(input("Enter the book quantity: "))
#     insertData={
#         'title':'title',
#         'price':'price',
#         'quantity':'quantity'
#     }
#     books.append(insertData)
#     x+=1
#     print(books)
# print  welcome books store 
# 1.add books
# 2.view books
# 3.delete books 
# 4.update
# 5.exit

while True:
    print("~~~~~~~~~~~~~~Welcome to Book Store~~~~~~~~~~~~~~")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Update Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add Book
    if choice == 1:
        bid = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        price = float(input("Enter book price: "))
        quantity = int(input("Enter book quantity: "))

        book = {
            'bid': bid,
            'title': title,
            'price': price,
            'quantity': quantity
        }

        books.append(book)
        print("Book added successfully!")

    # 2. View Books
    elif choice == 2:
        print("--- Book List ---")
        for book in books:
            print(book)

    #  3. Delete Book
    elif choice == 3:
        bid = int(input("Enter book ID to delete: "))
        for book in books:
            if book['bid'] == bid:
                books.remove(book)
                print("Book deleted successfully!")
                break
        else:
            print("Book not found!")

    # 4. Update Book
    elif choice == 4:
        bid = int(input("Enter book ID to update: "))
        for book in books:
            if book['bid'] == bid:
                book['title'] = input("Enter new title: ")
                book['price'] = float(input("Enter new price: "))
                book['quantity'] = int(input("Enter new quantity: "))
                print("Book updated successfully!")
                break
        else:
            print("Book not found!")

    # 5. Exit
    elif choice == 5:
        print("Thank you for using Book Store!")
        break

    else:
        print("Invalid choice! Please try again.")








 
