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

class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
    
    #debit
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount , "Debited from the account")
        print("current amount in the acccount is ", self.balance)
    #credit
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "credit in the account")
        print("current amount in the acccount is ", self.balance)

    def balance(self):
        return self.balance


acc1 = Account(1235, 10000)
acc1.debit(500)
acc1.credit(1500)






