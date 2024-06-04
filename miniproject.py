#Guess the number

# import random

# randNum = random.randint(1, 5)

# number1 = int(input("Enter the number:"))
# print("Current Random number is", randNum)


# if(number1 > randNum):
#     print("You have entered the big number. So, try to enter the lower number")
# elif(number1 < randNum):
#     print("You have entered the lower number. So, try to enter the big number")
# else:
#     print("Congratualtion, you guess the right number")


#Random Password Generator

import random
import string

passLower = string.ascii_lowercase
passUpper = string.ascii_uppercase
passDigit = string.digits
passPuntu = string.punctuation

addAll = passLower + passUpper + passDigit + passPuntu

passlen = 10
password = ""

for i in range(passlen):
    password += random.choice(addAll)



print("Your current password is:", password)

