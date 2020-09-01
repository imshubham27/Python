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
