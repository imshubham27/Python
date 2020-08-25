# It provides a high-performance multidimensional array object
# It is the fundamental package for scientific computing with Python.
# Numpy can also be used as an efficient multi-dimensional container of generic data.
# In Numpy, number of dimensions of the array is called rank of the array.
#  An array class in Numpy is called as ndarray
import numpy as np

# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n", arr)

# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)

# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print("Array with first 2 rows and"
      " alternate columns(0 and 2):\n", sliced_arr)

Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 0]]
print("\nElements at indices (1, 3), "
      "(1, 2), (0, 1), (3, 0):\n", Index_arr)

# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])

# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])

# Adding 1 to every element
print("Adding 1 to every element:", a + 1)

# Subtracting 2 from each element
print("\nSubtracting 2 from each element:", b - 2)

# sum of array elements
# Performing Unary operations
print("\nSum of all array "
      "elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print("\nArray sum:\n", a + b)


# Every ndarray has an associated data type (dtype) object.
# This data type object (dtype) provides information about the layout of the array.
# Integer datatype
# guessed by Numpy
x = np.array([1, 2])
print("Integer Datatype: ")
print(x.dtype)

# Float datatype
# guessed by Numpy
x = np.array([1.0, 2.0])
print("\nFloat Datatype: ")
print(x.dtype)

# Forced Datatype
x = np.array([1, 2], dtype=np.int64)
print("\nForcing a Datatype: ")
print(x.dtype)

# First Array
arr1 = np.array([[4, 7], [2, 6]],
                dtype=np.float64)

# Second Array
arr2 = np.array([[3, 6], [2, 8]],
                dtype=np.float64)

# Addition of two Arrays
Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)

# Square root of Array
Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)

# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)


# Creating array object
a = arr = np.array([[1, 2],
                    [4, 2]])
b = np.array([[4, 3],
              [2, 1]])
# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print("\nAn array initialized with all zeros:\n", c)

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype='complex')  # dtype can be int or float
print("\nAn array initialized with all 6s."
      "Array type is complex:\n", d)

# boolean array indexing example
cond = arr > 0  # cond is a boolean array
temp = arr[cond]
print("\nElements greater than 0:\n", temp)

# maximum element of array
print("Largest element is:", arr.max())
print("Row-wise maximum elements:",
      arr.max(axis=1))

# minimum element of array
print("Column-wise minimum elements:",
      arr.min(axis=0))

# sum of array elements
print("Sum of all array elements:",
      arr.sum())

# matrix multiplication
print("Matrix multiplication:\n", a.dot(b))

# multiply arrays (elementwise multiplication)
print("Array multiplication:\n", a*b)

# square root of array values
print("Square root of array elements:", np.sqrt(a))

array = np.arange(0, 8)
print("Original array : \n", array)

# shape array with 2 rows and 4 columns
array = np.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n", array)

# shape array with 2 rows and 4 columns
array = np.arange(8).reshape(4, 2)
print("\narray reshaped with 2 rows and 4 columns : \n", array)

arr = np.array([(1, 2, 3, 4), (3, 1, 4, 2)])

# using flatten method
print(arr.flatten())

# using fatten method
print(arr.flatten('F'))

#  Default value is ‘C’ (for row-major order).It will go row by row
# Use ‘F’ for column major order.
# using fatten method
print(arr.flatten('C'))


list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 9, 8, 7, 6, 5]

# Convert list1 into a NumPy array
a1 = np.array(list1)

# Convert list2 into a NumPy array
a2 = np.array(list2)

print(a1*a2)

a = np.array([[0, 1, 2], [3, 4, 5],
              [6, 7, 8], [9, 10, 11]])

print(a[1:2, 1:3])
print(a[1:2, [1, 2]])

# iterating  an array
for x in np.nditer(a, order='F'):  # column major
    print(x)

# first the number is converted to binary , then evaluated then converted back to decimal
in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]

print("Input array1 : ", in_arr1)
print("Input array2 : ", in_arr2)

out_arr = np.bitwise_and(in_arr1, in_arr2)
print("Output array after bitwise_and: ", out_arr)

out_arr = np.bitwise_or(in_arr1, in_arr2)
print("Output array after bitwise_or: ", out_arr)

out_arr = np.bitwise_xor(in_arr1, in_arr2)
print("bitwise_xor of 10 and 11 : ", out_arr)

# bitwise not is computed by adding 1 to it's binary representation
# and a negative sign and then revaluate its decimal form

out_arr = np.invert(in_arr1)
print("Output array after inversion: ", out_arr)

in_num = 5
bit_shift = 2
out_num = np.left_shift(in_num, bit_shift)
print("After left shifting 2 bit  : ", out_num)
out_arr = np.right_shift(in_num, bit_shift)
print("Output array after left shifting: ", out_arr)
out_num = np.binary_repr(in_num, width=10)
print("binary representation of 10 : ", out_num)


a = np.array(['geeks', 'for', 'geeks'])
# converting to lowercase
print(np.char.lower(a))
# counting a substring
print(np.char.count(a, 'geek'))
# counting a substring
print(np.char.count(a, 'fo'))

# numpy.rfind() : This function returns the highest index of the substring if found in given string.
# If not found then it returns -1.
# counting a substring
print(np.char.rfind(a, 'geek'))
# numpy.find()	It returns the lowest index of the substring if it is found in given string.
# If its is not found then it returns -1.

# comparing a string elementwise
# using equal() method
print(np.char.equal('geeks', 'for'))

# comparing a string elementwise
# using greater() method
a = np.char.greater('geeks', 'for')
print(a)

# Universal functions in Numpy are simple mathematical functions.
# It is just a term that we gave to mathematical functions in the Numpy library.
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis=1)
print("Along x axis : \n", arr1)
arr1 = np.sort(a, axis=0)
print("Along y axis : \n", arr1)

# numpy.argsort() : This function returns the indices that would sort an array.
# Numpy array created
a = np.array([9, 3, 1, 7, 4, 3, 6])
# unsorted array print
print('Original array:\n', a)
# Sort array indices
b = np.argsort(a)
print('Sorted indices of original array->', b)

# numpy.argmax() : This function returns indices of the max element of the array in a particular axis.
# numpy.argmin() : This function returns the indices of the minimum values along an axis.
# Working on 2D array
array = np.arange(12).reshape(3, 4)
# No axis mentioned, so works on entire array
print("\nMax element : ", np.argmax(array))
# returning Indices of the max element
# as per the indices
print("Indices of Max element(row-wise) : ", np.argmax(array, axis=1))
print("Indices of Max element(column-wise) : ", np.argmax(array, axis=0))
print("Min element : ", np.argmin(array))
# returning Indices of the max element
# as per the indices
print("Indices of Max element(row-wise) : ", np.argmin(array, axis=1))
print("Indices of Max element(column-wise) : ", np.argmin(array, axis=0))

# numpy.count_nonzero() : Counts the number of non-zero values in the array .
a = np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]])
b = np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]], axis=0)

print("Number of nonzero values is :",a)
print("Number of nonzero values is :",b)


