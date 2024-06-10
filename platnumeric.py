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
# print(aa.astype(float)) #change type of value

#--------------------------------------------------------------------------

#Methematical operations and functions on arrays

arr1 = np.array([20,30,60,50])
arr2 = np.array([80,50,60,30])

print(np.add(arr1,arr2)) #add function
print(np.subtract(arr1,arr2)) #subtract function
print(np.multiply(arr1,arr2)) #multiply function
print(np.divide(arr1, arr2)) #divide function