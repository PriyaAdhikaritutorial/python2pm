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



file=open("GUI/student_marks.txt", "w")
file.write("subjects:nepali, math, science, social, english")
file.write("student marksheet\n")

nepali=int(input("Enter the marks of nepali subject: "))
science=int(input("Enter the marks of science subject: "))
social=int(input("Enter the marks of social subject: "))
english=int(input("Enter the marks of english subject: "))
math=int(input("Enter the marks of math subject: "))

total=nepali+science+math+english+social
percentage=total/5
print("Total=", total)
print("Percentage=", percentage)

if percentage > 70:
    grade= "A+"
elif  percentage > 60:
    grade= "A"
elif  percentage > 50:
    grade= "B"
else:
      grade= "c"

file.write(f"nepali : {nepali}\n")
file.write(f"english : {english}\n")
file.write(f"social : {social}\n")
file.write(f"science : {science}\n")
file.write(f"math : {math}\n")


file.write(f"total :{total}\n")
file.write(f"percentage :{percentage}\n")
file.write(f"grade :{grade}\n")
file.write(f"grade: {grade}\n")
file.close()   
print("data of student_marks written sucessfully") 


file.close()
print("\ntotal=",total)
print("percentage=", percentage)
print("grade=", grade)
print("Data is written to student_marks sucessfully")


# file=open("GUI/students_marks.txt", "r")
# print(file.read())
# print(file.readlines())
# file.close()

# file.write(str(464656))
# import os
# import system
# import glob

