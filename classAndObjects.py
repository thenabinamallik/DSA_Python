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
    
class Test:
    def __init__(self, a, b): ## Its a consructor
        self.a = a
        self.b = b
        ## a and b are instnce object object variable


t1 = Test(5,7)
t2 = Test(9,8)

print(t1.a , t1.b)
print(t2.a , t2.b)
"""


## Methods
"""
- Instance Method
- Static Method
- Class Method
"""

class Test:
    x = 10
    def __init__(self, a, b): ## Its a consructor
        self.a = a
        self.b = b
        ## a and b are instnce object object variable
    
    def fun(self):
        print("this is instance method")

    @staticmethod
    def info():
        print("this is static method")

    @classmethod
    def fun1(cls):
        print("this is class method", cls.x)
        pass

h = Test(3,5)

Test.fun1()
