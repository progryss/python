#Function - Block of statements that perform a specific task.
#function used to trim the redundacy of code

#Function Defination
# def calSum(a,b,c): #parameter in brackets
#     sum = a + b + c
#     print(sum)
#     return sum

# #Function call
# calSum(5,7,2) #arguments in bracket
# calSum(8,10,5)


# def printHello():
#     print("hello")

# printHello()

#average of three number

def avgNumber(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return(avg)

#avgNumber(1,2,3)

# a = int(input("Enter A value:"))
# b = int(input("Enter B Value:"))
# c = int(input("Enter C Value:"))

# avgNumber(a,b,c)

#practice

cities = ["delhi", "mumbai", "kolkata", "chennai", "pune", "patna"]

#create custome length function
# def print_len(list):
#     print(len(list))

# print_len(cities)

#print list in same line

# def printList(list):
#     for item in list:
#         print(item, end=" ")

# printList(cities)

#calculate factorial value of n

# def numFacto(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# num = int(input("Enter a number:"))
# numFacto(num)

#convert value from USD to INR

# def usdInr(n):
#     print("USD of",n,"is equal to", n*83,"INR")

# num = int(input("Enter a number:"))
# usdInr(num)

#find odd and even

def checkOE(n):
    if(n%2 ==0):
        print("This is odd value")
    else:
        print("This is even value")
    
num = int(input("Enter a number:"))
checkOE(num)