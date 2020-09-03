from string import ascii_lowercase

# How do you count the occurrence of a given character in a string?
a = 'shubhamsharma'
key = 'a'
res = 0
for i in a:
    if i == 'a':
        res += 1
print(res)


# How do you count the occurrence of a given character in a string?
a = ('shubhamsharma')
b = {i: 0 for i in (a)}
for i in a:
    b[i] += 1
print(b)
# you can also use ascii_lowercase inorder for O(1) space complexity

# How do you print the first non-repeated character from a string?
a = ('shubhamsharma')
b = {i: 0 for i in a}
for i in a:
    b[i] += 1
for i in b.keys():
    if b[i] == 1:
        print(i)
        break
# you can also use ascii_lowercase inorder for O(1) space complexity
# split and join to remove spaces


# How do you convert a given String into int like the atoi()?

def check(b):
    return all(i.isdigit() for i in b)


def atoi(a):
    if a[0] == '-':
        a = a[1:]
        if check(a):
            return -1*int(a)
        else:
            return 0
    else:
        if check(a):
            return int(a)
        else:
            return 0


print(atoi('-1234'))

# How do you remove duplicates from an array in place?
# How are duplicates removed from an array without using any library?
a = [1, 2, 3, 4, 5, 6, 1, 2, 3]
b = len(a)
a.sort()
i = 0
while i < b-1:
    if a[i] == a[i+1]:
        a.remove(a[i])
        b -= 1
    else:
        i += 1
print(a)

# How do you reverse an array in place?


def reverse(a):
    if len(a) == 0:
        return
    b = a.pop(0)
    # print(b)
    reverse(a)
    a.append(b)
    return a


a = [1, 2, 3, 4, 5, 6, 7]
print(reverse(a))

# How do you swap two numbers without using the third variable?
a, b = 10, 5
a = a+b
b = a-b
a = a-b
print(a)
print(b)

# How do you check if two rectangles overlap with each other?


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Returns true if two rectangles(l1, r1)
# and (l2, r2) overlap


def doOverlap(l1, r1, l2, r2):
    # Eliminate these cases
    # If one rectangle is on left side of other
    if(l1.x >= r2.x or l2.x >= r1.x):
        return False

    # If one rectangle is above other
    if(l1.y <= r2.y or l2.y <= r1.y):
        return False

    return True


# Driver Code
if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if(doOverlap(l1, r1, l2, r2)):
        print("Rectangles Overlap")
    else:
        print("Rectangles Don't Overlap")


# How do you find the missing number in a given integer array of 1 to 100?
# //	Floor division - division that results into whole number adjusted to the left in the number line
def getMissingNo(A):
    n = len(A)
    # here its (n+1)*(n+2) because include that no which is missing
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return total - sum_of_A


# Driver program to test the above function
A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)


# How do you find the duplicate number on a given integer array?
# How do you find duplicate numbers in an array if it contains multiple duplicates?
# Function to print duplicates

# use hashing for printing duplicates

# Time Complexity: O(n), only one traversal is needed, so time complexity is O(n)
# Auxiliary Space: O(1), no extra space is required, so space complexity is constant.

# How do you find the largest and smallest number in an unsorted integer array?


def large_small(arr):
    ma = 0
    mi = float('inf')
    for i in arr:
        if i > ma:
            ma = i
        if i < mi:
            mi = i
    print("MIN:", mi)
    print("MAX", ma)


large_small([1, 2, 3, 4, 5, 6, 7, 8, 9])

# How do you find all pairs of an integer array whose sum is equal to a given number?
arr = [1, 5, 7, -1, 5]
b = {i: 0 for i in set(arr)}
s = 6
for i in arr:
    if b.get(s-i) != None:
        print("{} & {}".format(i, s-i))
# there is an O(nlog(n)) approach to solve this question.
# let’s suppose arr is the array consisting of all number and sum is the required sum you want to find then,
# sort the array and then for every element num in the array find if(sum-num) is there in the array using binary search.
# now the complexity of this approach is n for iteration and log(n) for binary search so overall time complexity is O(nlog(n)).

# How to find the maximum occurring character in given String?
a = 'shubhamsharma'
b = {i: 0 for i in set(a)}
for i in a:
    b[i] += 1
m = 0
for i in b.keys():
    if b[i] > m:
        m = b[i]
        max_char = i
print(max_char)

# How do you check if two strings are anagrams of each other?
str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
b1 = {i: 0 for i in set(str1)}
b2 = {i: 0 for i in set(str1)}
for i in str1:
    b1[i] += 1
for i in str2:
    b2[i] += 1
print(b1 == b2)

# How do you find all the permutations of a string?


def permute(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)
# Algorithm Paradigm: Backtracking
# Time Complexity: O(n*n!) Note that there are n! permutations and it requires O(n) time to print a a permutation.

# How do you check if a given string is a palindrome?
a = 'abcba'


def check_pali(a):
    j = len(a)-1
    i = 0
    while j>i:
        if a[i] != a[j]:
            return ('NO')
        i += 1
        j -= 1
    return 'YES'


print(check_pali(a))

# How do you reverse words in a given sentence without using any library method?
a = 'shubham sharma is a good boy'
a = a.split(' ')
a.reverse()
a = ' '.join(a)
print(a)

# How do you check if two strings are a rotation of each other?
string1 = "AACD"
string2 = "ACDA"
string1 = string1+string1
print(string2 in string1)
# T(n)= O(2*max(m,n))

# How to check if a given linked list is a palindrome?

# How to check if a given number is an Armstrong number?
a = 407
b = list(str(a))
s = 0
for i in b:
    s += int(i)**3
print(s == a)

# How to print Floyd’s triangle?
size = 7
k = 1
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        k = k + 1
    print()

# check whether the given number is even or odd without modulus operator
# By multiply and divide by 2. Divide the number by 2 and multiply by 2 if the result is same as input then it is an even number else it is an odd number.


def printPascal(n):

    for line in range(1, n + 1):
        C = 1  # used to represent C(line, i)
        for i in range(1, line + 1):

            # The first value in a
            # line is always 1
            print(C, end=" ")
            C = int(C * (line - i) / i)
        print("")


# Driver code
n = 5
printPascal(n)

# How to print all prime numbers up to a given number?


def isPrime(n):

    # Corner case
    if (n <= 1):
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False

    return True


# Driver Program
n = 11
for i in range(n):
    if isPrime(i):
        print(i)
# Time complexity = O(n)

# Finding all subsets of a given set
#  Find all substrings of String
s = 'abcd'
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])

# T(n)=O(N^2)
 
# Find second largest number in an array
a = [1, 2, 3, 4, 5, 6, 7]
f = s = 0
for i in a:
    f = max(i, f)
for i in a:
    if i != f:
        s = max(s, i)
print(s)

# Given a sorted array and a number x, find the pair in array whose sum is closest to x

#  Given an array of 0’s and 1’s in random order, you need to separate 0’s and 1’s in an array.
# Thanks to Naveen for suggesting this method.
# 1) Count the number of 0s. Let count be C.
# 2) Once we have count, we can put C 0s at the beginning and 1s at the remaining n – C positions in array.


# Find the Contiguous Subarray with Sum to a Given Value in an array.
def subArraySum(arr, n, Sum):

    # create an empty map
    Map = {}

    # Maintains sum of elements so far
    curr_sum = 0

    for i in range(0, n):

        # add current element to curr_sum
        curr_sum = curr_sum + arr[i]
        print("CURR SUM", curr_sum)

        # if curr_sum is equal to target sum
        # we found a subarray starting from index 0
        # and ending at index i
        if curr_sum == Sum:

            print("Sum found between indexes 0 to", i)
            return

        # If curr_sum - sum already exists in map
        # we have found a subarray with target sum
        if (curr_sum - Sum) in Map:

            print("Sum found between indexes",
                  Map[curr_sum - Sum] + 1, "to", i)

            return

        Map[curr_sum] = i

    # If we reach here, then no subarray exists
    print("No subarray with given sum exists")


# Driver program to test above function
if __name__ == "__main__":

    arr = [10, 2, -2, -20, 10]
    n = len(arr)
    Sum = -10

    subArraySum(arr, n, Sum)

# Search in a row wise and column wise sorted matrix.


def search(mat, n, x):

    i = 0

    # set indexes for top right element
    j = n - 1
    while (i < n and j >= 0):

        if (mat[i][j] == x):

            print("n Found at ", i, ", ", j)
            return 1

        if (mat[i][j] > x):
            j -= 1

        # if mat[i][j] < x
        else:
            i += 1

    print("Element not found")
    return 0  # if (i == n || j == -1 )


# Driver Code
mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]
search(mat, 4, 29)

# Check if Array Elements are Consecutive.
# sort the array and check if each element differs by 1

# Given a sorted array and a number x, find the pair in array whose sum is closest to x
# Python3 program to find the pair
# with sum
# closest to a given no.

# A sufficiently large value greater
# than any
# element in the input array
MAX_VAL = 1000000000


# Prints the pair with sum closest to x

def printClosest(arr, n, x):

    # To store indexes of result pair
    res_l, res_r = 0, 0

    # Initialize left and right indexes
    # and difference between
    # pair sum and x
    l, r, diff = 0, n-1, float('inf')

    # While there are elements between l and r
    while r > l:
        # Check if this pair is closer than the
        # closest pair so far
        if abs(arr[l] + arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)

        if arr[l] + arr[r] > x:
            # If this pair has more sum, move to
            # smaller values.
            r -= 1
        else:
            # Move to larger values
            l += 1

    print('The closest pair is {} and {}'
          .format(arr[res_l], arr[res_r]))


# Driver code to test above
if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    n = len(arr)
    x = 54
    printClosest(arr, n, x)
# An efficient solution can find the pair in O(n) time

# Write a program to print all the LEADERS in the array.
# An element is leader if it is greater than all the elements to its right side.
# And the rightmost element is always a leader.

# Scan all the elements from right to left in an array and keep track of maximum till now. When maximum changes its value, print it.


def printLeaders(arr, size):

    max_from_right = arr[size-1]
    print(max_from_right)
    for i in range(size-2, -1, -1):
        if max_from_right <= arr[i]:
            print(arr[i])
            max_from_right = arr[i]


# Driver function
arr = [16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))

# Maximum difference between two elements such that larger element appears after the smaller number


def maxDiff(arr, n):

    # Initialize Result
    maxDiff = -1

    # Initialize max element from
    # right side
    maxRight = arr[n - 1]

    for i in range(n - 2, -1, -1):
        if (arr[i] > maxRight):
            maxRight = arr[i]
        else:
            diff = maxRight - arr[i]
            if (diff > maxDiff):
                maxDiff = diff
    return maxDiff


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 90, 10, 110]
    n = len(arr)

    # Function calling
    print("Maximum difference is", maxDiff(arr, n))


# Find a local minima in an array
# An array element is a peak if it is NOT smaller than its neighbours. For corner elements, we need to consider only one neighbour.
# We say that an element arr[x] is a local minimum if it is less than or equal to both its neighbors.
a = [1, 2, 3, 4, 0, 5, 2, 1]
for i in range(1, len(a)-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        peak = a[i]
        print("PEAK", peak)
    if a[i] < a[i-1] and a[i] < a[i+1]:
        loc = a[i]
        print("LOC", loc)
# T(n)=O(n)

# Given an array containing zeroes, ones and twos only. Write a function to sort the given array in O(n) time complexity.
# Approach: Count the number of 0s, 1s and 2s in the given array. Then store all the 0s in the beginning followed by all the 1s then all the 2s.
# heapq._heapify_max(heap)


# A more efficient solution is to use modulo operator in Euclidean algorithm .
# Recursive function to return gcd of a and b
def gcd(a, b):

    # Everything divides 0
    if (b == 0):
        return a
    return gcd(b, a % b)


# Driver program to test above function
a = 98
b = 56
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')


def findLCM(a, b):

    lar = max(a, b)
    small = min(a, b)
    i = lar
    while(1):
        if (i % small == 0):
            return i
        i += lar


# Driver Code
a = 5
b = 7
print("LCM of ", a, " and ",
      b, " is ",
      findLCM(a, b), sep="")

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(4))
