import numpy as np
a1=np.array([1,2,3,4])
print(a1)

print(np.zeros((2,3)))

np.arange(1,10,2)

arr= np.array([10,20,30,40,50,60])
print(arr[1:4])
print(arr[:3])
print(arr[3:])
print(arr[0])
print(arr[-1])
print(arr[2])

a1=np.array([1,2,3,4])
print(a1[0])
print(a1[2])
print(a1[-1])

# a) To get help on the add function
print("Help on numoy.add function: ")
help(np.add)

# Creating arrays using array(),zeroes(),ones(),inspace()
arr1=np.array([1,2,3,4])
arr2=np.array([4,3,2,1])

zeros_arr=np.zeros(2)
ones_arr=np.ones(4)
lin_arr=np.linspace(0,10,5)

print("\nArray 1: ",arr1)
print("Array 2: ",arr2)
print("Zeros Array: ",zeros_arr)
print("Ones Array: ",ones_arr)
print("Lin_arr Array: ",lin_arr)

# b) To test whether none of the elements of a given array is zero
arr3 = np.array([1,2,3,4])
result = np.all(arr3)
print("\nNone of the elements are zero: ",result)

arr4 = np.array([1,0,3,4])
print("None of the elements are zero: ",np.all(arr4))

# c) Element-wise comparsion of two arrays
print("\nElement-wise comparsion between arr1 and arr2: ")
print("")
