# print("Hello python")
# print("It's a python code to say hello")
a = int(20) 
print(type(a))

b = ["apple", "mango", "cherry"] 
print(type(b))

# a =  float(10.0)
# print(type(a))

b = frozenset({"banana",  "apple", "orange"})
print(b)
print(type(b))

a = "priya adhikari"
print(a[1:6])

# slicing string
d = "how are you"
print(d[:5])

# upper case
datalist = "hello python"
print(datalist.upper())

# lower case
datalist = "HELLO PYTHON"
print(datalist.lower())

# replace
datalist = "hello"
print(datalist.replace("h", "m"))

# String Concatenation (if we don't need a gap between "hello python" we have to write a code like this )
a = "hello"
b = "python"
c = a + b
print(c)

# String Concatenation (if we need a gap between "hello python" we have to write a code like this) 
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# formatting string (To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.)
age = 20
txt= f"My name is Priya, I am {age}"
print(txt)

  
