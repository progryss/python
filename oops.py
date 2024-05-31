#OOPS in Python
#Top  map this real world scenerio, we started using objects in code.
#This is called object oriented programming

#Class is a blueprint for creating objects

# class Student:
#     name = "Sujeet"

# #creating object (instance)

# s2 = Student()
# print(s2.name)

#------------------------
#__init__ function - Constructor -> All classess have a function called _init_(), which always executed when the class/object is being initiated.

#Class and Instance Attributes = Class.attr and obj.attr
# class Student:
#     college_name = "ABC College" #Class Attibute
#     def __init__(self, name, marks): # SELF should be the first paramerter in this function
#         self.name = name #object Attribute
#         self.makrs = marks
# s1 = Student("PK", 25)
# print(s1.name, s1.makrs)

# s2 = Student("sujeet", 98)
# print(s2.name)
# print(Student.college_name)

#Methods are function that belong to object

# class Student:
#     college_name = "XYZ College"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self): #methods
#         print("Welcome", self.name)
    
#     def get_marks(self): #methods
#         return self.marks

# s1 = Student("Sujeet", 97)
# s1.welcome()
# print(s1.get_marks())


#practice - Create a student class that takes name and marks of 3 subject as arguments in constructor and then create a method to print the average


# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def welcome(self): 
#         sum = self.m1 + self.m2 + self.m3
#         print("Welcome", self.name, sum/3)

# s1 = Student("Sujeet", 10, 20, 30)
# s1.welcome()
        
#Static method - Methods that don't use the self parameter (work at class level)

#Abstraction - Hiding the implementation details of a class and only showing the essential features to the user.

# class Car:
#     def __init__(self):
#         self.brk = False
#         self.clut = False

#     def start(self):
#         self.brk = True
#         self.clut = True
#         print("Car started")

# car1 = Car()
# car1.start()

#Encapsulation - wrapping data and function into a single unit (object)

#practice - create a account class with 2 attributes - balance and account number. Create methods for debit, credit and printing the balance

# class Account:
#     def __init__(self, account, balance):
#         self.account = account
#         self.balance = balance
    
#     #debit
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount , "Debited from the account")
#         print("current amount in the acccount is ", self.balance)
#     #credit
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "credit in the account")
#         print("current amount in the acccount is ", self.balance)

#     def balance(self):
#         return self.balance


# acc1 = Account(1235, 10000)
# acc1.debit(500)
# acc1.credit(1500)


#del keyword - used to delete object properties or object itself

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Sujeet")
# s2 = Student("Kumar")
# print(s1.name, s2.name)
# del s1.name
# print(s2.name)

#Private (like) attribute & method
#conceptual implementaion in python
#Private attribute & methods are meant to be used only within the class and are not accessible from outside the class

#attribute private
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass #__ to private (attribute)
#     def reset(self):
#         print(self.__acc_pass)


# acc1 = Account("12345", "abc55sdjdsj")
# print(acc1.acc_no)
# print(acc1.reset())
# print(acc1.acc_pass)

#method private

# class Persone:
#     name = "Any name"
#     def __hello(self): #__ to private the method
#         print("Hello Person")
#     def welcome(self):
#         self.__hello

# p1 = Persone()
# print(p1.welcome)
# print(p1.__hello())

#inheritance: when one class(child/derived) derives the properties & method of another class (parent/base)

#types of inheritance - Single, multi-leve, multiple

#single inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car Started...")
#     @staticmethod
#     def stop():
#         print("Car Stopped..")

# class Merc(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = Merc("Merc")
# print(car1.name)
# print(car1.start())
# print(car1.stop())

#Multi level inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car Started...")
#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class Merc(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class GLS(Merc):
#     def __init__(self,type):
#         self.type = type

# car1 = GLS("Diesel")

# print(car1.type)
# car1.start()
# car1.stop()

#Multiple Inheritance

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A,B):
#     varC = "Welecome to classs C"

# c1= C()

# print(c1.varC)
# print(c1.varA)
# print(c1.varB)

#Super Method - super() method is used to access method of the parent class

#POLYMORPHISM : when same operator is allowed to have different meaning according to the context





