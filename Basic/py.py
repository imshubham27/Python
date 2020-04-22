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

# import os

# print(os.getcwd())

# os.chdir('D:\GIT\Python')

# print(os.getcwd())

# print(os.listdir())

# os.mkdir('TEST')

# os.listdir()

# os.remove('TEST')

# os.listdir()

# a=[1,2,3,0]

# for i in a:
#     try:
#         b=5/i
#         print(b)
#     except:
#         print("NO")
#     finally:
#         print("HIIIII")

# class Parrot:

#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def dance(self):
#         return self.name

# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)

# # access the class attributes
# print("Blu is a {}".format(blu.species))
# print("Woo is also a {}".format(woo.species))

# print(blu.dance())

# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))

# def diagonalDifference(arr):
#     # Write your code here
#     c=0
#     d=0
#     i=len(arr)
#     print(i)
#     for a in range(i):
#         for b in range(i):
#             if a==b:
#                 c=arr[a][b]
#             if (a+b)==(i-1):
#                 d=arr[a][b]
#     print(c)
#     print(d)
#     diff=c-d
#     diff=abs(diff)            
#     return diff

# a = [[1, 2, 3], [5,6,1], [7, 8, 9]]
# x=diagonalDifference(a)
# print(x)

# def staircase(n):
#     for i in range(1,n+1):
#             a=n-i
#             print("{}{}".format(" "*a,"#"*i))

# staircase(6)

# from itertools import permutations 

# def miniMaxSum(arr):
#     perm=a=[]
#     perm = list(permutations(arr, 3))
#     for i in range(len(perm)):
#         a.append(sum(perm[i]))
#     b=max(a)
#     c=min(a)
#     print("{} {}".format(c,b))

# miniMaxSum([1,2,3,4])

# def birthdayCakeCandles(ar):
#     d=max(ar)
#     e=ar.count(d)
#     print(e)

# birthdayCakeCandles([3,2,1,3])

# def timeConversion(s): 
#     # Checking if last two elements of time 
#     # is AM and first two elements are 12 
#     if s[-2:] == "AM" and s[:2] == "12": 
#         return "00" + s[2:-2] 
          
#     # remove the AM     
#     elif s[-2:] == "AM": 
#         return s[:-2] 
      
#     # Checking if last two elements of time 
#     # is PM and first two elements are 12    
#     elif s[-2:] == "PM" and s[:2] == "12": 
#         return s[:-2] 
          
#     else: 
          
#         # add 12 to hours and remove PM 
#         return str(int(s[:2]) + 12) + s[2:8] 

# print(timeConversion("04:59:59AM"))

# Complete the kaprekarNumbers function below.
# def kaprekarNumbers(p, q):
#     r=0
#     x=""
#     for i in range(p,q):
#         b=i*i
#         c=len(str(b))
#         leng=len(str(i))
#         # print(leng)
#         # print(c)
#         if(len(str(b))==1):
#             d=b
#             e="0"
#         else:
#             # print(str(b)+ "   "+ str(i))
#             d=(str(b)[c-leng:c])
#             e=str(b)[:c-leng]
#         # print("L DIGITS",int(e))
#         # print("R digits",(int(d)))
#         if(int(e)+int(d)==i):
#             x=x+str(i)+" "
#             r=r+1
#     if(r==0):
#         print("INVALID RANGE")
#     else:
#         print(x)

# kaprekarNumbers(1,99999)

# list1=[4,2,2,1,1]

# for i in list1:
#     if (list1.count(i)==1):
        
#         break
# print(i)

# l=[1,2,3,0,0,4,5,0,6]
# l.remove(0)
# l.remove(0)
# l.pop(5)
# print(l)

    # def maxSubArray(self, nums: List[int]) -> int:
    #     l=[]
    #     s=[]
    #     for i in range(1,len(nums)+1):
    #         a=list(permutations(nums,i))
    #         l.extend(a)
            
    #     for i in range(len(l)):
    #         s.append(sum(l[i]))
            
    #     return max(s)

# a=s=[]
# for j in range(len(nums)):
#     for i in range(len(nums)+1):
#         if(i>j):
#             a=nums[j:i]
#             s.append(sum(a))

# print(s)

from itertools import permutations
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
b=[]
c=[]

# i=strs[0]
# sel=(list(permutations(i,len(i)))
# print ("".join(sel[0]))
for i in range(len(strs)):
    d=[]
    sel=list(permutations(strs[i],len(strs[i])))
    for j in range(len(sel)):
        a=""
        a="".join(sel[j])
        # print("AAA",a)
        b.append(a)
    print("BBB",b)
    d.append(strs[i])
    x=i+1
    for x in range(len(strs)):
        if strs[i+1] in b:
            d.append(strs[i+1])
            strs.remove(strs[i+1])
    c.append(d)
    b=[]
    print("CCC",c)
    








