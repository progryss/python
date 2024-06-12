#Numpy stands for numerical python

import numpy as np

arr = np.array([10,20,30,40])

arrmul = np.array([[10,20,30], [40,50,60]])

arrsting = np.array(["sujeet", "kumar"])

#print(type(arr))

# print(arr[:2]) #slicing
# print(arr[1:]) #slicing

# print(arrmul[1,0:2]) #slicing of multi dimensional array

# print(np.shape(arrmul)) # check how many rows and column in array (row, column)
# print(np.size(arrmul)) #size of the array (row*column)
# print(np.ndim(arrmul)) #check the dimension of the array
# print(arrmul.dtype) #check the datatype of the array
# print(type(arrsting))
# print(arrsting.dtype)

#-----------------------------------------------------------------------

#Inspecting an array

a = [10,20,30,40]
aa = np.array(a)

# print(type(aa))
# print(aa.astype(float)) #change data type of value

#--------------------------------------------------------------------------

#Methematical operations and functions on arrays

arr1 = np.array([20,30,60,50])
arr2 = np.array([80,50,60,30])

# print(np.add(arr1,arr2)) #add function
# print(np.subtract(arr1,arr2)) #subtract function
# print(np.multiply(arr1,arr2)) #multiply function
# print(np.divide(arr1, arr2)) #divide function

num1 = np.array([3,4,2,1])
num2 = np.array([2])

#print(np.power(num1,num2)) #power caluculation
sq = np.sqrt([ 9,16, 4,1]) #square root calculation which display value in float

#print(sq.astype(int)) #float value change to int

#-----------------------------------------------------
#combining and spliting array
# arr1 = np.array([[20,30],[60,50]])
# arr2 = np.array([[80,50],[60,30]])

# print("Join two array")
# print(np.concatenate([arr1,arr2])) # join two array 
# print("Horizontal join two array")
# print(np.hstack([arr1,arr2]))
# print("Vertical join two arrya")
# print(np.vstack([arr1,arr2]))

# a = [10,20,50,60,80,90]
# arr = np.array(a)
# print(np.array_split(arr,2))

#--------------------------------------------
#adding and removing element from the array
# a = [10,20,50,60,80,90]
# arr = np.array(a)

# print(np.append(arr,100)) #add the value
# print(np.delete(arr,1)) #delete the value

#-----------------------
#Search, Sort and filter the array

# ar = np.array([5,2,9,7,12,4,6])
# #print(np.sort(ar)) #sorting array
# s = np.where (ar == 12) #search the array value position in array
# ars = np.sort(ar)
# ss = np.searchsorted(ars,12) # seach value in only sorted array
# #print(ss)
# fa = [False, True, False, False, True, True, True] #boolean value for filter
# far = ar > 10 #filter the array and find the value which greater then 10
# print(ar[fa]) #filter the value
# print(ar[far])

#--------------------------
#Aggregating function in array
# ar = np.array([5,2,9,7,12,4,6])
# ar1 = np.array([2,4,3,3,3,2,3])
# # print(np.sum(ar))
# # print(np.min(ar))
# # print(np.max(ar))
# # print(np.size(ar))
# # print(np.mean(ar))
# # print(np.average(ar))
# # #print(np.cumsum(ar))
# # print(np.cumprod(ar))
# # print(ar)
# # print(ar1)
# c = np.cumprod([ar,ar1], axis=0)
# print(c[1])
# print(np.sum(c[1]))

#-------------------------------------------------------------------------
#Statistical functions
import statistics as stats
bakedFood = [150,200,150,100,200,210]

ar = np.array(bakedFood)
print(np.mean(ar)) #sum of all values/ number of values
print(np.median(ar)) #central value after sorting
print(stats.mode(ar)) # find and display the recurring value
print(np.std(ar))