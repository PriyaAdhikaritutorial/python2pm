# what is filehandling:File handling is the process of creating, opening, reading, writing, and closing files stored on a computer using a programming language.
# types of file handling:1️⃣ Text File Handling

# Data is stored in human-readable form

# Examples: .txt, .csv, .log

# Used for text data

# 2️⃣ Binary File Handling

# Data is stored in binary format (0s and 1s)

# Not human-readable

# Examples: .bin, .dat, .jpg, .pdf
# mode of file handlling
# r,w,a,rt,wb,rb,ab:Read binary
# wb	Write binary
# ab	Append binary
# csv file? CSV (Comma Separated Values) file stores data in tabular form using commas.   



# file= open("student.txt", "w")
# file.write("Name: Priya Adhikari\n")
# file.write("study: Bachelors 2nd year\n")
# file.close()
# print("data written sucessfully")


# file=open("student.txt", "a")
# file.write("Address: Kathmandu\n")
# file.close()

# print("Data is appended sucessfully")

# Wb
# file=open("data.bin", "wb")
# file.write(b"Hello binary file")
# file.close()

# Rb
# file=open("data.bin", "rb")
# data=file.read()
# print("data")
# file.close()



# file=open("GUI/student_marks.txt", "w")
# file.write("subjects:nepali, math, science, social, english")
# file.write("student marksheet\n")

# nepali=int(input("Enter the marks of nepali subject: "))
# science=int(input("Enter the marks of science subject: "))
# social=int(input("Enter the marks of social subject: "))
# english=int(input("Enter the marks of english subject: "))
# math=int(input("Enter the marks of math subject: "))

# total=nepali+science+math+english+social
# percentage=total/5
# print("Total=", total)
# print("Percentage=", percentage)

# if percentage > 70:
#     grade= "A+"
# elif  percentage > 60:
#     grade= "A"
# elif  percentage > 50:
#     grade= "B"
# else:
#       grade= "c"

# file.write(f"nepali : {nepali}\n")
# file.write(f"english : {english}\n")
# file.write(f"social : {social}\n")
# file.write(f"science : {science}\n")
# file.write(f"math : {math}\n")


# file.write(f"total :{total}\n")
# file.write(f"percentage :{percentage}\n")
# file.write(f"grade :{grade}\n")
# file.write(f"grade: {grade}\n")
# file.close()   
# print("data of student_marks written sucessfully") 

# OR WRITE THIS CODE :

# file.close()
# print("\ntotal=",total)
# print("percentage=", percentage)
# print("grade=", grade)
# print("Data is written to student_marks sucessfully")


# file=open("GUI/students_marks.txt", "r")
# print(file.read())
# print(file.readlines())
# file.close()

# file.write(str(464656)) to print numbers becoz it does'nt print out directly numbers.


# import os
# import getpass

# if not os.path.exists("GUI/database.txt"):
#     handle=open("GUI/database.txt", "w")
#     handle.close()

# def register():
#     print("========== create a new account============")
#     username=input("Enter your username: ").strip().lower()
#     if username in open ("GUI/database.txt").read():
#         print("username already exists. please try a different one.")
#         exit()
#     password=getpass.getpass("Enter your password: ").strip()
#     confirm_password=getpass. getpass("confirm your password: " ).strip() 
#     if password != confirm_password:
#         print("password do not match. please try again.")
#         exit()
#         storedata=f"username:{username}, passwprd:{password}\n"
#         with open ("GUI/database.txt", "a") as file:
#             file.write(storeData)
#             print("Account created sucessfully!")  

# def login():
#     print("===========Login account============")
#     username=input("Enter your username: ").strip().lower()
#     password=getpass. getpass("Enter your password: "). strip()
#     with open("GUI/database.txt","r") as file:
#         is_login=False
#         for user in file.readlines():
#             udata=user.split(",")
#             uname=udata[0]
#             uname=uname[9:]
#             upass=udata[1]
#             upass=upass[9:].strip()
#             if username==uname and password==upass:
#                 is_login=True
#                 if is_login:
#                     print("welcome", username)
#                 else:
#                     print("username & password not match")

# question= input("Do you have  an account? (y/n): ")
# if question=="y":
#     login()
# else:
#     register()



# file=open("facebook_login.txt","w")
# file.write("username: Priya Adhikari\n")
# file.write("password: priy@221")
# file.write("login please")
# file.close()
# print("Data is written successfully")


# user_name="Priya Adhikari"   
# pass_word='priy@221'
# username=input("Enter the username: ")
# password=input("Enter the password: ")

# if username==user_name and password==pass_word:
#   print("login succesfully")
# else:
#     print("unable to login")


# file.close()
# print("Data is written sucessfully Thank You!")



# import os: os is a built-in Python module used to interact with the operating system.
# import system: This is also just a comment, not actual code, It helps you find files using patterns.
# import glob:

# file=open("students1.txt", "w")
# file.write("file runs correctly")
# file.close()

# print("data  is written sucessfully")



# import.os
# import.glob
# file=open("GUI/students1.txt")
# file.write("subjects: health,math,science,social,science")
# file.write("students_marksheet\n")

# health=input("Enter the marks of health: ")
# math=input("Enter the marks of math: ")
# english=input("Enter the marks eglish: ")
# science=input("Enter the marks of science: ")
# social=input("Enter the  marks of social: ")

# total=health+social+math+science+english
# percentage=total/5
# print("total=",  total)
# print("percentage=", percentage)

# if percentage > 70:
#     grade="A+"
# elif percentage > 60:
#     grade="A"
# elif percentage > 50:
#     grade="B"
# else:
#     grade="c"


# file.write(f"nepali: {health}\n")
# file.write(f"science: {science}\n")
# file.write(f"math: {math}\n")
# file.write(f"social: {social}\n")
# file.write(f"english: {english}\n")

# file.close()
# file.write("total=", total)
# file.write("percentage=", percentage)
# file.write("grade=", grade)
# print("Data written sucessfully to students1.txt Thank You!")


# files= glob.glob("marks/*,txt")
# print("\nText files inside marks folder:")
# for f in files:
#     print(f)


# 