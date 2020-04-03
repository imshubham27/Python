# import config
# import os

# print(os.getcwd())

# def func(*names):
#     print(names)
#     t=(1,2,3,4)
#     print(t[0])    
#     t={1,2,3,4,5,21,1,2}
#     print(t)



# func("shubham","sharma")

# print(config.a)

# str = 'cold'

# # enumerate()
# list_enumerate = list(enumerate(str))
# print('list(enumerate(str) = ', list_enumerate)

# #character count
# print('len(str) = ', len(str))

# a="shubham"
# b=","

# c=b.join(a)

# print(c)

# a=set()

# a.update([1,4,3,1,34,1,34,234])

# print(a)

# d= {7:'c',1:'a',2:'b',3:'d',4:'e'}

# d[6]='f'

# print(d)

# d.pop(3)

# print(d)

# l=[1,2,3,4,5,6]

# l.pop(4)

# print("LIST",l)

# print(d.values())

# for i in d.values():
#     print(i)

# lis=[x**2 for x in range(0,10)]

# print("LIST",lis)

# print(sorted(l))


# f= open('python.txt')

# f.read(6)

# with open('python.txt','w') as f:
#     f.write("Hi I am shubham")

# f= open('python.txt')

# print(f.read())

# f.tell()

# f.seek(0)

# f.readline()

import os

print(os.getcwd())

os.chdir('D:\GIT\Python')

print(os.getcwd())

print(os.listdir())

os.mkdir('TEST')

os.listdir()

os.remove('TEST')

os.listdir()

a=[1,2,3,0]

for i in a:
    try:
        b=5/i
        print(b)
    except:
        print("NO")
    finally:
        print("HIIIII")

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

A


