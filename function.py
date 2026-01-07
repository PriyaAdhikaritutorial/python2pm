# what is function 
# types of function
# built-in-function
# user-defined function


# cal(4,6)
# even_or_odd

# def eo(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")
    
# eo(5)



# a,b,c  pass the accending order and decending order numbers
# and sum that numbers

# *args, and **krgs

# a,b,c= 1,6,2
# numbers=[a,b,c]

# numbers.sort()
# print("Ascending order:", numbers)


# numbers.reverse()
# print("descending order:", numbers)


# total=a+b+c
# print("sum:",total )




# numbers= [10,50,82]
# print(sum(numbers))

# To find the max and min numbers
# nums= [10,30,88]
# print(max(nums))
# print(min(nums))


# To add the numbers.
# a= int(input("Enter the number: "))
# b= int(input("Enter the numbers: "))
# print(a+b)

# 1️⃣ Print your name
# 2️⃣ Add two numbers
# 3️⃣ Area of rectangle
# 4️⃣ Celsius to Fahrenheit
# 1.
# nums=[25,44]
# print(sum(nums))

# 2.
# l=55
# b=33
# area= l*b
# print("Area of rectangle: =", area)

# largest of three numbers.
# a=int(input("Enter the numbers: "))
# b=int(input("Enter the numbers: "))
# c=int(input("Enter the numbers: "))
# if a>b and a>c:
#     print("a is largest")
# elif b>c:
#     print("b is largest")
# else:
#     print(c)  

# To find even or odd numbers    
# num=int(input("Enter the numbers: "))
# if num %2== 0:
#     print("it is even")
# else:
#     print("it is odd")



# data= [
#     {'name':'ram', 'gender':'male'},
#     {'name':'sita', 'gender':'female'},
#     {'name':'hari', 'gender':'male'},
#     {'name':'laxmi', 'gender':'female'},
# ]

# output:
# male=[
#  {'name':'ram', 'gender':'male'},
#  {'name':'hari', 'gender':'male'},
# ]

# female=[
#  {'name':'sita', 'gender':'female'},
#  {'name':'laxmi', 'gender':'female'},
# ]


# def gender_difference(users):
#      male=[]
#      female=[]
#      for user in users:
#         if user ['gender']=='male':
#             male.append(user)
#         else:
#          female.append(user)
#      return[male,female]
# result = gender_difference(data)
# print(result)

# data= [
#     {'name':'ram', 'gender':'male'},
#     {'name':'sita', 'gender':'female'},
#     {'name':'hari', 'gender':'male'},
#     {'name':'laxmi', 'gender':'female'},
# ]

# search=input("Enter the name: ")

# def take_value():
#     p=10
#     t=10
#     r=10
#     return[p,t,r]


# def calculate():
#     a,b,c =take_value()
#     return a*b*c/100


# def display():
#     print(calculate())

# display()



# subjects = ['Nepali', 'English', 'Math', 'Social', 'Science']
# marks = []

# for sub in subjects:
#     m = float(input(f"Enter marks of {sub}: "))
#     marks.append(m)

# total = sum(marks)
# percentage = (total / (len(subjects) * 100)) * 100

# if percentage >= 70:
#     grade = "A+"
# elif percentage >= 50:
#     grade = "A"
# elif percentage >= 35:
#     grade = "B"
# else:
#     grade = "Fail"

# print("\n--- STUDENT RESULT SHEET ---")
# for i in range(len(subjects)):
#     print(subjects[i], ":", marks[i])

# print("Total =", total)
# print("Percentage =", percentage)
# print("Grade =", grade)

# users=[
#    {'username':'hari', 'password': 'hari002', 'role':'admin'},
#    {'username':'ram', 'password': 'ram002', 'role':'user'},
#    {'username':'sita', 'password': 'sita002', 'role':'user'},
# ]   

# def role_login():
#     uname = input("Enter username: ")
#     pwd = input("Enter password: ")

    
#     for user in users:   
#         if user['username'] == uname and user['password'] == pwd:
#             login_success = True
#             print("Login successful")

            
#             if user['role'] == 'admin':
#                 print("You are ADMIN")
#                 print("All usernames are:")
#                 for u in users:
#                     print(u['username'])
#             else:
#                 print("You are USER")
#                 print("You are not allowed to see other usernames")
#             break   
#     if login_success == False:
#         print("Invalid username or password")

#     role_login()

        
# output:take the input from user and check if the login is sucessful and make the rule that if therole is admin he/she can see the other username otherwise they cannot.
# what is module?

# def add (x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y

#QSN what is the data of today.
# import datetime
# today= datetime.datetime.now()
# print(today)

#QSN kati din ko vaye mh
# import datetime
# today= datetime.datetime.now()
# bday=datetime.datetime(2005,7,13)
# print(today-bday)

#QSN how many days left  for my next birthday.
# import datetime
# today= datetime.datetime.now()
# bday=datetime.datetime(2005,7,13)
# print(today-bday)

# QSN bday aauna kati din baki cha ki gai sakyo?
# import datetime
# today= datetime.datetime.now()
# dday=datetime.date(2005,7,13)




#To find total jobs available:
 
# jobs = [
#     "Software Developer",
#     "Web Designer",
#     "IT Manager",
# ]
# total_jobs=0
# software_dev=0
# IT_manager=0
# for job in jobs:
#     total_jobs = total_jobs + 1

#     if job == "Software Developer":
#         software_dev = software_dev + 1

#     if job == "IT Manager":
#         IT_manager = IT_manager + 1

# print("Total jobs available:", total_jobs)
# print("Software Developer jobs:", software_dev)
# print("IT Manager jobs:", IT_manager)











