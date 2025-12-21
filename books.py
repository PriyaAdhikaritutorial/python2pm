# user = [
# {"username": "admin", "password": "admin002"},
# {"username": "hari", "password": "hari002"}
# ]

# username =  input("Enter your username: ")
# password = input("Enter your password: ")

# if  username==user[0]['username'] and password==user[0]['password']:
#     print("Login sucessfully")
# else:
#     print("Login failed")




# ktm(27km)
# 5-5 distance
# 1.kalanki to chabile(Rs.20)
# 2.kalanki to buspark(Rs.25)

# Route fares
# kalanki_to_chabahil = 20
# kalanki_to_buspark = 20
# kalanki_to_syambhu = 20
# kalanki_to_teku = 20
# kalanki_to_naikap = 20

# print("KTM (27 km)")
# print("5–5 distance")
# print("1. Kalanki to Chabahil (Rs.", kalanki_to_chabahil, ")")
# print("2. Kalanki to Bus Park (Rs.", kalanki_to_buspark, ")")
# print("3. kalanki to Syambhu (Rs.", kalanki_to_syambhu,")")
# print("4. kalanki to Teku (Rs.", kalanki_to_teku,")")
# print("5. kalanki to Naikap (Rs.", kalanki_to_naikap,")")

# if/else/ nested if statement.

# a = 205
# b = 50
# c = 70

# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")


# e = 200
# f = 100
# g = 22

# if e>f:
#     if e>g:
#         if g>f:
#          print(e,g,f)
#         else:
#          print(e,f,g)
#     else:
#          print(g,f,e)
# else:
#     if f>g:
#         if e>g:
#          print(f,e,g)
#         else:
#          print(f,g,e)
#     else:
#      print(g,f,e)
    

# a = 25
# b = 10
# c = 22
# d = 18

# if a > b:
#     if a > c:
#         if a > d:
#             if b > c:
#                 if b > d:
#                     if c > d:
#                         print(a, b, c, d)
#                     else:
#                         print(a, b, d, c)
#                 else:
#                     print(a, d, b, c)
#             else:
#                 if c > d:
#                     print(a, c, d, b)
#                 else:
#                     print(a, d, c, b)
#         else:
#             print(d, a, c, b)
#     else:
#         print(c, a, d, b)
# else:
#     if b > c:
#         if b > d:
#             if a > c:
#                 if a > d:
#                     if c > d:
#                         print(b, a, c, d)
#                     else:
#                         print(b, a, d, c)
#                 else:
#                     print(b, d, a, c)
#             else:
#                 if c > d:
#                     print(b, c, d, a)
#                 else:
#                     print(b, d, c, a)
#         else:
#             print(d, b, c, a)
#     else:
#         print(c, b, d, a)
   

# x = 200
# y = 101
# z = 190
# if z > y: 
#     if z > x:
#         if x > z:
#             print(z,y ,x)
#         else:
#          print(y,x,z)
#     else:
#        print(x, z, y)



# if x > y:
#    if y > z:
#       print(x,y,z)
#    else:
#     print(z,x,y)
# else:
#     print(z,x,y)


# a = 200
# b = 201
# c = 190
# d = 100
# if a > b:
#     if a > c:
#         if a > d:
#             if b > c:
#                 if b > d:
#                     if c > d:
#                         print(a,b, c, d)
#                     else:
#                         print(a,c,b,d)
#                 else:
#                     print(a,d,c,b)
#             else:
#                 print(b,c,d,a)
#         else:
#             print(b,d,c,a)
#     else:
#         print(c,d,b,a)

# if b > c:
#     if b > d:
#         if c > d:
#             print(a,c,b,d)
#         else:
#             print(b,c,d,a)
#     else:  
#         print(c,d,b,a)
# else:
#     print(d,c,b,a)      


# (this condition defines that if the age is more then 18 and less than 40 they are eligible to vote )
# a = 45
# b = 4
# age=34
# if age> 18 and age<40:
#     print(" is eligible")
# else:
#     print("is not eligible")

# party(age 18< 40>)
# drinks (age 18<40)
# 35<40 whisky

# print ("---------Party--------") 

# print ("age = 18")
# print("age = 40")
# if 18>40:
#     print("The people whose age 40 are able to enter in the party")
# else:
#     print("The people whose age 18 is not able to enter in the party")


# print("------Drinks------")

# print("age = 18")
# print("age = 40")
# if 18 < 40: 
#  print("The people whose age 18 allowed to drink soft drinks")
# else:
#    print("The people whose age 18 do not allowed to drink hard drinks")

# print("--------Whisky-------")

# print("age = 18")
# print("age = 40")
# if 40 > 18:
#    print("The people whose age is 40 are allowed to drink whisky")
# else:
#    print("The people whose age is 18 are not allowed to drink whisky ") 




# match case
# lang = 'english'

# match lang:
#    case 'nepal':
#       print("Namaste")
#    case 'english':
#       print("Hello")
#    case _:
#       print("Invalid language")




# a = int(input("Enter the number a:"))
# b = int(input("Enter the number b:")) 
# operator =input("Enter the operator"("+, -, /, *"))
# match operator:
#   case'+':
#     print(a+b) 
#   case'-':
#     print(a-b)
#   case'/':
#     print(a/b) 
#   case'*':
#       print(a*b)




# student = input("Enter student Id")
# name = input("Enter student name")
# print("Five subjects marks")

# nep = int(input("Enter nepali marks"))
# eng =  int(input("Enter engish marks"))
# soc = int (input("Enter social marks"))
# sci = int (input("Enter science marks"))
# math =int(input("Enter math marks"))

# total= nep+eng+math+sci+soc
# per = total/5 
# print('total',total)
# print('percentage',per)
# if per >35 and per <50:
#    print('c')
# elif per > 50 and per < 70:
#    print('b')
# elif per > 70 and per < 90:
#    print('a')
# elif per > 90 and  per < 100:
#    print('a+')
# else:
#    print('fail')




# data= ['alexa','olivia','nooma','sidney']
# name = input("Enter name")

# if name in data:
#    print(f"{name} is found")
# else:
#    print(f"{name} is found")



# wap to enter employe id,name, and salary.
# 100000> 20% bous
# 80-100000 > 15%
# 50-100000> 10%
# below 50000> 5%


emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))


if salary > 100000:
    bonus = salary * 0.20
elif 80000 <= salary <= 100000:
    bonus = salary * 0.15
elif 50000 <= salary < 80000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

total_salary = salary + bonus





