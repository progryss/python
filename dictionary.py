#Dictionary are used to store data values in key:value pairs
#They are unordered, mutable(changeble) and don't allow duplicate keys

# info = {
#     "name" : "Sujeet",
#     "Experience" : 10,
#     "Fields" : ["SEO", "Development", "Design"],
# }

# info["name"] = "SK"
# info["surname"] = "Kumar"

# print(info)


#Nested dictionary

student = {
"name" : "Sujeet",
"class" : "10th Standard",
"marks" :{
    "math" : 83,
    "hindi" : 94.50,
    "english" : 68,
}

}

#print(student["marks"]["math"])

#print(student.keys())
#print(list(student.keys())) - change in list
#print(student.values())
#print(student.items()) - return all values in tuple
# print(student["name"]) - if through error after code not print
# print(student.get("name")) - if through error after code can print

# student.update({"city" : "Delhi"})
# print(student)


#practice

mark = {}
math = int(input("Enter math number:"))
mark.update({"math": math})
eng = int(input("Enter eng number:"))
mark.update({"eng": eng})

print(mark)