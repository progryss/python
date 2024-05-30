#STRING
#\n = for new line or line break
#\t = for tab space

#str1 = "progryss is a digital marketing agency and \tits also offers development services"

#print(str1[1:4])
#print(str1.endswith("ce"))
#print(str1.capitalize())
#print(str1.replace("digital", "are"))
#print(str1.find("is"))
#print(str1.count("s"))

name = input("Enter you first name:")
namelen = len(name)

print("Entered name is:", name , "and their character length is:", namelen, "ee display:", name.count("e"))