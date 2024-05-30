#For Loops are used for sequential traveler. For traversting list, string, tuples, etc.

#list = [1,2,3]
#veg = ["kheera", "kakdi", "muli"]

# veg = "potato"

# for i in veg:
#     print(i)

# #prac 1

# num = [1,4,9,16,25,36,49,64,81,100]

# for i in num:
#     print(i)

#prac 2

# num = (1,4,9,16,25,36,49,64,81,100, 16)
# idx = 0
# for el in num:
#     if(el == 16):
#         print("16 found", idx)
#     idx += 1


#RANGE FUNCTION

# for i in range(100, 0, -1):
#     print(i)

#enter any number and print table
# num = int(input("Enter the number:"))

# for i in range (1,11):
#     print(num*i)

#practice - sum of number 

n = 5
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)