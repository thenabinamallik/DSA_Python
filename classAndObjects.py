## Classes and Objects
""" Topics
- Class
- Attributes
- Objects
- Class Objects
- __init__() method
- Types of methods
- Types of Variables
"""

## Class
"""
- Class is a description of an object and aslo a group of variable and function
- It defines various attributes of an objects
- In python language termelogy we call both function and varibales as attributes
- Defining a class is creating an datatype

class Car:
    ## Attributes
    pass
     
## If Class is a common noun then the object is a proper noun i.e - Person is a Class and Nabina is an Object


"""

## Encapsulation
"""
An act of combining properties and method related same objet is known as Encapsulation
"""

## Attributes
"""
- Attributes are member varibles and member functions
Class Test:
    x = 5
    def fun():
"""

## Objects
"""
- Objects is an instance of a class (example)
- Objects are of two types
    1. Class Objects
    2. Instance Object

- Instace Object Variable

class Text:
    x = 10  # class object varible
    def f1();

Instance Object
t1 = Test()
t2 = Test()

Class object
- Class has exactly one class object but many instance object
- We dont need to creat an class object(Text)
- Class Object Variable (Static Varible)

t3 = Test

"""

## __init__() Method
"""
def __init(self):
    
"""

class Test:
    def __init__(self):
        print("This in object")
        # self.__fun()
    
    def __fun(self):
        print("this is funtion")

    @staticmethod
    def info():
        print("this is info")


t1 = Test()
t1.info()
