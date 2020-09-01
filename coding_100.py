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

# Python program to check if rectangles overlap


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
array = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr_size = len(array)
for i in range(arr_size):

    array[array[i] % arr_size] = array[array[i] % arr_size] + arr_size

print("The repeating elements are : ")
for i in range(arr_size):
    if (array[i] >= arr_size*2):
        print(i, " ")
# Time Complexity: O(n), only one traversal is needed, so time complexity is O(n)
# Auxiliary Space: O(1), no extra space is required, so space complexity is constant.

# How do you find the largest and smallest number in an unsorted integer array?


def large_small(arr):
    max = 0
    min = float('inf')
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    print("MIN:", min)
    print("MAX", max)


large_small([1, 2, 3, 4, 5, 6, 7, 8, 9])

# How do you reverse a linked list in place?

