# import tkinter as tk
 
# app = tk.Tk()
# app.title("My GUI Applicatiion")
# app.geometry("500x500")
# n1 = tk.Label(app,text="Enter first number : ")
# n1.pack()
# num1=tk.Entry(app)
# num1.pack()

# n2 = tk.Label(app,text="Enter first number: ")
# n2.pack()
# num2=tk.Entry(app)
# num2.pack()
# rn=tk.Label(app,text="Result")
# rn.pack()

# def sayHello():
#     x=int(num1.get())
#     y=int(num2.get())
#     total=x+y
#     rn.config(text=f"Total number is: {total}")    

# btn = tk.Button (app,text="Click Me",command=sayHello) 
# btn.pack()   
 
# app.mainloop()


# app.mainloop()


# import tkinter as tk
 
# app = tk.Tk()
# app.title("My GUI Applicatiion")
# app.geometry("500x500")
# entry_var = tk.StringVar()
# entry = tk.Entry(app, textvariable=entry_var, font=("Arial", 18))
# entry.grid(row=0, column=0, columnspan=4)


# def get_value(val):
#     print(val)
# expression = ""

# def get_value(value):
#     global expression
#     expression += str(value)
#     entry_var.set(expression)

# def calculate():
#     global expression
#     try:
#         result = eval(expression)
#         entry_var.set(result)
#         expression = str(result)
#     except:
#         entry_var.set("Error")
#         expression = ""

# def clear():
#     global expression
#     expression = ""
#     entry_var.set("")

# one= tk.Button(app,text="1", command=lambda:get_value(1),pady=10,padx=10)
# one.grid(row=1, column=0)
# two= tk.Button(app,text='2',command = lambda:get_value(2),pady=10,padx=10)
# two.grid(row=1, column=1)

# three=tk.Button(app,text='3', command=lambda:get_value(3),pady=10,padx=10)
# three.grid(row=2, column=0)

# four=tk.Button(app,text='4', command=lambda:get_value(4),pady=10,padx=10)
# four.grid(row=2, column=1)

# five=tk.Button(app,text='5', command=lambda:get_value(5), pady=10 ,padx=10)
# five.grid(row=3, column=0)
# six=tk.Button(app,text='6', command=lambda:get_value(6), pady=10 ,padx=10)
# six.grid(row=3, column=1)
# seven=tk.Button(app,text='7', command=lambda:get_value(7), pady=10 ,padx=10)
# seven.grid(row=4, column=0)
# eight=tk.Button(app,text='8', command=lambda:get_value(8), pady=10 ,padx=10)
# eight.grid(row=4, column=1)
# nine=tk.Button(app,text='9', command=lambda:get_value(9), pady=10 ,padx=10)
# nine.grid(row=5, column=0)
# ten=tk.Button(app,text='10', command=lambda:get_value(10), pady=10 ,padx=10)
# ten.grid(row=5, column=1)

# plus = tk.Button(app, text="+", command=lambda: get_value("+"), pady=10, padx=10)
# plus.grid(row=1, column=3)
# minus = tk.Button(app, text= '-', command=lambda: get_value("-"),pady=10, padx=10)
# minus.grid(row=1, column=4)
# divide=tk.Button(app,text='/', command=lambda: get_value("/"),pady=10, padx=10)
# divide.grid(row=2, column=3)
# multiply=tk.Button(app, text="*", command=lambda:get_value("*"), pady=10, padx=10)
# multiply.grid(row=2, column=4)
# mod=tk.Button(app, text="%", command=lambda:get_value("%"), pady=10, padx=10)
# mod.grid(row=3, column=3)

# equal = tk.Button(app, text='=', command=calculate, pady=10, padx=10)
# equal.grid(row=3, column=4)


# clear_btn=tk.Button(app, text='c', command=clear, pady=10, padx=10)
# clear_btn.grid(row=4, column=4)

# expression = ""

# def get_value(value):
#     global expression
#     expression += str(value)
#     entry_var.set(expression)

# def calculate():
#     global expression
#     try:
#         result = eval(expression)
#         entry_var.set(result)
#         expression = str(result)
#     except:
#         entry_var.set("Error")
#         expression = ""

# def clear():
#     global expression
#     expression = ""
#     entry_var.set("")

# app.mainloop()


# what is python regix:Regex is used to search, match, or change text patterns in Python.

# import re 
# name= 'ram  rai'
# patterns= r"[a-z \s]+"
# if re.fullmatch(patterns,name):
#     print("matched")
# else:
#     print("not matched")


# import re
# numbers=9877554499
# patterns="[1-9 \d]"
# if re.match(patterns,numbers):
#     print("matched numbers ")
# else:
#     print("not matched numbers")
