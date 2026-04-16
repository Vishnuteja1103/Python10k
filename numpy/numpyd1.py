import numpy as np

arr=np.array([1,2,3,45]) #changes the list into  array (np.array)
print(arr)

arr2=np.array([[1,2,3],[2,3,4],[3,4,13]]) # multi dimension array
print(arr2)
# ``````````````````````````````````````````````````````````````````````````````````````
print(arr2.ndim) # shows the which type of dimension array 
print(arr2.dtype) # shows the datatype of the array 
print(arr2.shape) # shows the shape like which type of martix like arr2 is 3x3 matrix
# ``````````````````````````````````````````````````````````````````````````````````
print(np.zeros((2, 3)))   # 2x3 array of zeros |creates a matrix with zeros 
print (np.ones((2, 2)))    # 2x2 array of ones | create a matrix with ones
print(np.eye(3))          # Identity matrix | create a matrix with diaglone indentity
print (np.arange(0, 10, 2))  # [0,2,4,6,8] | prints the numbers in a range it have 
# start,end,step values | here it was started from 0 tp 10 with step value of 2
# it means it skips a value 
print(np.linspace(0, 1, 5)) # 5 values between 0 and 1 | gives 5 values in range betweeen 
# 0 to 1 ( five values )