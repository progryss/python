#Fily I/O - Python can be used to perform operations on file. (read and write data)
#Text files: .txt, .doc, .log, etc.
#Binary Files : .mp4, .mov, .png, .jpg, etc.

#OPEN FILE
# f = open("demo.txt", "r")

# data = f.read()

# print(data)
# print(type(data))
# f.close()

#WRITE FILE

# f = open("demo.txt", "w") # remove all existing data and add new data in file
# f.write("Sujeet Kumar")
# f.close()

#apend file
# f = open("demo.txt", "a") # remove all existing data and add new data in file
# f.write("\nPython learning")
# f.close()

#read and write simentoneosly 

# f = open("demo.txt", "a+")
# f.write("\nabc")
# f.write("\nxyz")
# print(f.read())
# f.close()

# With Syntax

# with open("demo.txt", "r") as f:
#     demo = f.read()
#     print(demo)

# with open("demo.txt", "w") as f:
#     f.write("Progryss")


#practice - write a prodcut to create new file and enter text

# with open("practice.txt", "w+") as f:
#     f.write("Hi everyone \n we are learning file I/O \n using java. \n I like programming in Java.")
#     demo = f.read()
#     print(demo)

#practice - find Java and replace with Python

# with open("practice.txt", "r") as f:
#     demo = f.read()
#     new_demo = demo.replace("java", "Python")
#     print(new_demo)

# with open("practice.txt", "w") as f:
#     f.write(new_demo)

#Practice - write a function search if word "larning" or not

# def check_for_word():
#     with open("practice.txt", "r") as f:
#         demo = f.read()
#         if(demo.find("learning")):
#             print("Found learing word")
#         else:
#             print("can't find")
# check_for_word()

#practice - write a function to find in which line of the file doest the word "learning" occurs first

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as k:
#         while data:
#             data = k.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()

#practice : from a file containing numbers seperated by comma, print the count of even numbers.

def count_even():
    count = 0
    with open("practice.txt", "r") as f:
        data = f.read()
        #print(data)

        nums = data.split(",")
        for val in nums:
            if(int(val) % 2  == 0):
                count += 1
        
        print(count)

count_even()