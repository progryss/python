#Loops

#while loops
# list = []

# i = 1

# while i <= 10:
#     a = i*i
#     list.append(a)
#     i += 1

# print(list)


#pract 2

# heros = ["s","m", "k", "n"]

# i = 0

# while i < len(heros):
#     print(heros[i])
#     i +=1


#prac 3 -  enter number and display table

# n = int(input("Enter any number:"))
# i = 1
# while i <=10:
#     print(i*n)
#     i += 1

#prac 4

# num = [1,4,9,16,25,36,49,64,81,100]

# idx = 0

# while idx < len(num):
#     print(num[idx])
#     idx += 1


# #prac 5- find x namber in tuple

# num = (1,4,9,16,25,36,49,64,81,100)

# n = int(input("Enter a number:"))
# idx = 0

# while idx < len(num):
#     if(num[idx] == n):
#         print("Found number 9 at", idx)
#         break #find the number and break the loop
#     else:
#         print("Finding...")
#     idx += 1

#prac 6  - continue

# i = 1

# while i <=10:
#     if(i%2 != 0):
#         i += 1
#         continue #if condition true then skip the next part
#     print(i)
#     i += 1
