#pip install pandas - command to install pandas instance
#pip install openpyxl - command for read the excel file

import pandas as pd #import pandas module
import numpy as np #import numpy module

data = {
    "Name" : ["Sujeet", "Vishal", "Deepak"],
    "Age" :  [33,35,45],
    "Salary": [3000, 1000, 5000]   
}

dataList = ["sujeet", 35, 33.62, "suresh"]
#df = pd.DataFrame(dataList)
#df= pd.DataFrame(data)
#df = pd.Series(data)
#print(df)
data = pd.read_excel("D:/Simon/EBC/ProductUpload.xlsx")
#data = pd.read_csv("D:/Simon/EBC/ProductUploadFilter.csv")
#print(data)
#print(data.head(2)) # show the first two rows of data
#print(data.tail(2)) #show the last two rows of data
#print(data.info()) #show the data type of data
#print(data.describe()) #describe the dta 
#print(data.isnull()) #check if data has null value
#print(data.isnull().sum()) #show heading wise null check
#print(data["Engine"].duplicated().sum()) # find duplicate value by column
#print(data.drop_duplicates("Engine")) #delete duplicate values from the column
#print(data.dropna()) #drop null value row
#print(data.replace(np.nan, 2020)) #replace all nan value to suggested value
#data["End Year"] = data["End Year"].replace(np.nan, 2050) #replace nana value in seperate column
#print(data.fillna(method = "bfill")) #fill the nan value cell from the just after cell value 
#print(data.fillna(method = "ffill")) #fill the nan value cell from the just before cell value
data = pd.read_excel("D:/Simon/EBC/ProductUpload.xlsx")
# df.loc[(df["Engine %"] == 1.4), "Check"] = "wow"
# df.loc[(df["Engine %"] < 1.1), "Check"] = "no wow"
#data["Make Model"] = data["Make"].str.lower() + " " + data["Model"] #concatinate value of two column and show the value in new column
#data["Bo"] = (data["Start Year"]/100)*20 #calculation
#print(data)
gp = data.groupby("Make").agg({"Model": "count"}) #groupby data
gp1 = data.groupby(["Make", "Start Year"]).agg({"Model": "count"}) #groupby data
# print(gp1)
# monthData = {
#     "Months" : ["January", "February", "March", "April","July" ]
# }

# a = pd.DataFrame(monthData)
# def extract(value):
#     return value[0:3]

# a["Short"] = a["Months"].map(extract)
# print(a)

#-----------------------------------
#concatinate, join, merge

# data1 = {"EmpId":["001", "002", "003", "004", "005"],
#          "Name": ["ram", "shyam", "mangal", "bhawan", "hari"],
#          "Age": [40,35,85,17,52]
#         }
# data2 = {"EmpId":["001", "002", "003", "004", "005"],
#          "Salay": [25000,35000,85000,96000,5000],
#          "City": ["delhi", "mumbai", "punjab", "haridwar", "thane"]
#         }
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# #print(df1, df2)

# #print(pd.merge(df1,df2,on="EmpId")) #merge data function

# print(pd.concate(df1, df2))

#--------------------------
#compare

# fruits = {"Name": ["Banana", "Mango", "Lichi", "Chiku"],
#         "Price": [100,150,160,200],
#         "Quantity": [15,20,63,89]
#         }
# fruits1 = {"Name": ["Banana", "Mango", "Lichi", "Chiku"],
#         "Price": [140,180,130,220],
#         "Quantity": [17,23,60,70]
#         }
# fruitdf1 = pd.DataFrame(fruits)
# fruitdf2 = pd.DataFrame(fruits1)

# #print(fruitdf1)
# print()
# #print(fruitdf2)

# print(fruitdf1.compare(fruitdf2))

#-----------------------

#Pivoting and melting data frames

dict = {"Keys": ["K1", "K2", "K1", "K2"],
        "Names": ["John", "Peter", "Ben", "David"],
        "House": ["Blue", "Red", "Blue", "Green"]
        }
df = pd.DataFrame(dict)
print(df)
print(df.pivot("Keys", "Names", "House"))