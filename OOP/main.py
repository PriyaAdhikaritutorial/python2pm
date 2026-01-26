# what is oop: Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
# what is method:
#
#  what is class:in Python, a class is a blueprint or template used to create objects.
# It defines the properties (variables) and behaviors (methods/functions) that objects will have.
# 
# what is inheritence:Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# 
# static methods:A static method is a method inside a class that does not use the object (self) or the class (cls).
# 
# class decorators:In Python, a decorator is a special function that modifies or extends the behavior of another function (or class) without changing its actual code.
# property decorators:



# class college:
#     x=10
#     def info(self):
#         print("This is a college info")
#     def add(self, a,b):
#         print(a+b)


# c1= college()
# print(c1.x)
# c1.info()
# c1.add(10,20)


# to make a calculator
# class calculator:
#   def add(self, a,b):
#       print(a+b)
#   def sub(self, a,b):
#       print(a-b)
#   def mul(self, a,b):
#       print(a*b)
#   def div(self, a,b):
#       print(a/b)

# calc= calculator()
# calc.add(10,20)
# calc.sub(20,10)
# calc.mul(10,20)
# calc.div(20,4)             


# class CRUD:
#     data=['priya','sita']

#     def show(self):
#         print("Data:",self.data)
#     def insert(self, name):
#         self.data.append(name)
#         self.show()
#         print(f"{name} inserted successfully")
#     def upadte(Self):
#         print("My marks is soo good") 
#     def delete(self):
#         print("hello")
#     def find(self,id):
#         print("priya adhikari")

# obj = CRUD() 
# obj.show()  

# class Laptop:
#     def brand(self,name):
#         print("Brand is:" ,name)

# class Dell:
#     def price(self):
#         pass

# class Toshiba(Laptop):
#     def price(Self):
#         pass


# obj=Dell()
# obj.brand("Dell")    

# class Laptop:
#     name='Dell'
#     _price=50000
#     _model="Inspiron"


# obj=Laptop
# print(obj.name)
# print(obj._price)
# print(obj._model)

# class Laptop:
#     __price=50000


#     def get_price(self):
#         return self.__price
    
#     def set_price(self, new_price):
#         self.__price= new_price


# obj= Laptop()
# obj.set_price(60000)
# print(obj.get_price())


# class Laptop:
#     def __init__(self, name, brand): 
#         print(name)
#         print(brand)

# class Dell(Laptop):
#     def __init__(self,name,brand,price):
#         super().__init__(name,brand)
#         print(price)



# obj = Dell('Dell','Intel', 5000)        
        

# decorator example
# def my_decorator():
#     def wrapper():
#         print("Before function")
#         print("After function")
#         return wrapper

# def say_Hello():
#     print("Hello")


# say_Hello()   

# static decorator
# class Math:
#     def add(a,b):
#         return a+b
    
# print(Math.add(5,3))







