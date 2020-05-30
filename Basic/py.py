import config
import os

print(os.getcwd())

def func(*names):
    print(names)
    t=(1,2,3,4)
    print(t[0])    
    t={1,2,3,4,5,21,1,2}
    print(t)



func("shubham","sharma")

print(config.a)

str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

a="shubham"
b=","

c=b.join(a)

print(c)

a=set()

a.update([1,4,3,1,34,1,34,234])

print(a)

d= {7:'c',1:'a',2:'b',3:'d',4:'e'}

d[6]='f'

print(d)

d.pop(3)

print(d)

l=[1,2,3,4,5,6]

l.pop(4)

print("LIST",l)

print(d.values())

for i in d.values():
    print(i)

lis=[x**2 for x in range(0,10)]

print("LIST",lis)

print(sorted(l))


f= open('python.txt')

f.read(6)

with open('python.txt','w') as f:
    f.write("Hi I am shubham")

f= open('python.txt')

print(f.read())

f.tell()

f.seek(0)

f.readline()

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
    
    def dance(self):
        return self.name

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print(blu.dance())

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

def diagonalDifference(arr):
    # Write your code here
    c=0
    d=0
    i=len(arr)
    print(i)
    for a in range(i):
        for b in range(i):
            if a==b:
                c=arr[a][b]
            if (a+b)==(i-1):
                d=arr[a][b]
    print(c)
    print(d)
    diff=c-d
    diff=abs(diff)            
    return diff

a = [[1, 2, 3], [5,6,1], [7, 8, 9]]
x=diagonalDifference(a)
print(x)

def staircase(n):
    for i in range(1,n+1):
            a=n-i
            print("{}{}".format(" "*a,"#"*i))

staircase(6)

from itertools import permutations 

def miniMaxSum(arr):
    perm=a=[]
    perm = list(permutations(arr, 3))
    for i in range(len(perm)):
        a.append(sum(perm[i]))
    b=max(a)
    c=min(a)
    print("{} {}".format(c,b))

miniMaxSum([1,2,3,4])

def birthdayCakeCandles(ar):
    d=max(ar)
    e=ar.count(d)
    print(e)

birthdayCakeCandles([3,2,1,3])

def timeConversion(s): 
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if s[-2:] == "AM" and s[:2] == "12": 
        return "00" + s[2:-2] 
          
    # remove the AM     
    elif s[-2:] == "AM": 
        return s[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif s[-2:] == "PM" and s[:2] == "12": 
        return s[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(s[:2]) + 12) + s[2:8] 

print(timeConversion("04:59:59AM"))

Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    r=0
    x=""
    for i in range(p,q):
        b=i*i
        c=len(str(b))
        leng=len(str(i))
        # print(leng)
        # print(c)
        if(len(str(b))==1):
            d=b
            e="0"
        else:
            # print(str(b)+ "   "+ str(i))
            d=(str(b)[c-leng:c])
            e=str(b)[:c-leng]
        # print("L DIGITS",int(e))
        # print("R digits",(int(d)))
        if(int(e)+int(d)==i):
            x=x+str(i)+" "
            r=r+1
    if(r==0):
        print("INVALID RANGE")
    else:
        print(x)

kaprekarNumbers(1,99999)

list1=[4,2,2,1,1]

for i in list1:
    if (list1.count(i)==1):
        
        break
print(i)

l=[1,2,3,0,0,4,5,0,6]
l.remove(0)
l.remove(0)
l.pop(5)
print(l)

    def maxSubArray(self, nums: List[int]) -> int:
        l=[]
        s=[]
        for i in range(1,len(nums)+1):
            a=list(permutations(nums,i))
            l.extend(a)
            
        for i in range(len(l)):
            s.append(sum(l[i]))
            
        return max(s)

a=s=[]
for j in range(len(nums)):
    for i in range(len(nums)+1):
        if(i>j):
            a=nums[j:i]
            s.append(sum(a))

print(s)

from itertools import permutations
strs=["compilations","bewailed","horology","lactated","blindsided","swoop","foretasted"]
b=[]
c=[]
y=len(strs)
i=0
while(i<y):
    d=[]
    sel=list(permutations(strs[i],len(strs[i])))
    for j in range(len(sel)):
        a=""
        a="".join(sel[j])
        # print("AAA",a)
        b.append(a)
    # print("BBB",b)
    d.append(strs[i])
    strs.remove(strs[i])
    y=y-1
    x=0
    # print("STRS!",strs)
    while(x<y):
        # print("XXX",x)
        # print("YYYY",y)
        # print("STRS@",strs[x])
        if strs[x] in b:
            d.append(strs[x])
            strs.remove(strs[x])
            x=x-1
            y=y-1
            # print("XAFTER",x)
            # print("D",d)
            # print("STRS AFTER",strs)
        x=x+1
    c.append(d)
    b=[]
    print("CCC",c)
for i in c:
    print(i)

S="oi###mupo##rszty#s#xu###bxx##dqc#gdjz"
T="oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz"
S=list(S)
i=0
y=len(S)
while i<y:
    if S[i]=="#" and i!=0:
        S.remove(S[i])
        S.remove(S[i-1])
        i=i-2
        y=y-2
    elif S[i]=="#" and i==0:
        S.remove(S[i])
        i=i-1
        y=y-1
    i=i+1
S=''.join(S)
T=list(T)
i=0
y=len(T)
while i<y:
    if T[i]=="#" and i!=0:
        T.remove(T[i])
        T.remove(T[i-1])
        i=i-2
        y=y-2
    elif T[i]=="#" and i==0:
        T.remove(T[i])
        i=i-1
        y=y-1
    i=i+1
T=''.join(T)
print(S)
print(T)
if T==S:
    print (True)
else:
    print (False)

from functools import reduce 
nums=[1,2,3,4]
c=[]
for i in range(len(nums)):
    # print("II",i)
    d=nums.copy()
    z=d.remove(d[i])
    # print("ZZ",z)
    # print("DD",d)
    a=reduce((lambda x, y: x * y), d) 
    # print("AA",a)
    c.append(a)
    # print(c)
return c
s="(*))"
a=s.count('(')
b=s.count(')')
c=s.count('*')
s=list(s)
i=0
# print(s)
y=len(s)
while (i<y):
    print(i)
    if s[i]=="*" and s[i-1]=="(" and s[i+1]==")":
        s[i]=""
        s[i-1]=""
        s[i+1]="" 
        i=i-2
        y=y-3
    i=i+1
    print(s)
print(s)

if (a+c==b) or (b+c==a):
    print(True)

for i in s:
    print(next(i))


T = [55,38,53,81,61,93,97,32,43,78]

d=[]
for i in range(len(T)-1):
    for j in range(i+1,len(T)-1):
        print("TJ",T[j])
        print("TI",T[i])
        if T[j]>T[i]:
            a=j-i
            print("AA",a)
            break
        else:
            a=0
    d.append(a)
    print("ABEFORE",a)
d.append(0)        
print(d)

T = [89,62,70,58,47,47,46,76,100,70]
Expected:[8,1,5,4,3,2,1,1,0,0]
def temp(a):
    # b=T.index(a)
    T.remove(a)
    # print("B",b)
    # i=b+1
    # print("II",i)
    for i in range(len(T)):
        if(T[i]>a):
            # print("CC",c)
            print("II",i)
            c=i+1
            break
        else:
            c=0
    print("C",c)
    return c

result = list(map(temp, T[:len(T)-1]) )
result.append(0)
print(result)



a=19
d=[]
def get_digit(num):
    if num < 10:
        d.append(num)
    else:
        get_digit(num // 10)
        d.append(num % 10)
while a!=1:
    get_digit(a)    
    a=(sum(i*i for i in d))
    print(a)
    if(a==1):
        flag=0
        break
    d=[]
if(flag==0):
    return(True)
else:
    return(False)

t=[1,2,1,2,1,3,2]
s=0
a=set(t)
print(t)
d=[]
for i in a:
    d.append(t.count(i))
print(d)
for i in d:
    s=s+ i//2
print(s)

    a=len(s)
    b=(n//a)+1
    print(b)
    s=s*b
    s=s[:n]
    c=s.count("a")
    return c


c="0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0 1 0 0 0"
c=list(c)
for i in range(100):
    c.remove(' ')
print(c)
s=0
i=0
k=(len(c))
while i<k-2:
    print("I BEFORE",i)
    if (c[i+1]+c[i+2]==0) or c[i+1]==1:
        s=s+1
        i=i+2
        print("I",i)
    elif c[i+1]==0:
        s=s+1
        i=i+1
    else:
        i=i+1
        pass
if(c[k-2]==1):
    print s
else:
    print (s+1)

a=[1,2321,3,412]
d=1       
l1=a[d:]
l2=a[:d]
l1.extend(l2)
c=str()
for i in l1:
    c=c+ str(i)+" "
print(c)


s=2131.121321
print(int(s))

n=98280 
k=84
def eva(x):
    
    if (x+k) in range(1,n+1) and (x+k) not in d:
        return (x+k)
    elif (x-k) in range(1,n+1) and (x-k) not in d: 
        return (x-k)
    else :
        return -1

d=list(map(eva,list(range(1,n+1))))
v=d.count(-1)
z=' '.join(str(x) for x in d)
if(v>0):
    print(-1)
    # return(str(-1))        
else:
    print(z)
    # return z

from functools import reduce
li="AAABBB"
li1=li[1:]
print(li1)
c=0
def chk(p,q):
    if p==q:
        return ""
    else:
        return p
d=list(map(chk,li1,li))
print(d)


from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 

import difflib
string1 = "a"
string2 = "abcd"
matches = difflib.SequenceMatcher(
    None, string1, string2).get_matching_blocks()
print(type(matches))
print(len(matches))
for match in matches:
    print(string1[match.a:match.a + match.size])

a=[312321313,4241143,4124143411,24343]
a=(a[-1::-1])
a=' '.join(str(x) for x in a)
print(a)

t=99
b=1
d=1.5
def timer(a):
    global i
    global b
    global d
    # print("A",a)
    if((a-1)==0 or (b-1)==0):
        # d=a
        # i=i+1
        d=int(2*d)
        b=d
        # print("B",b)
        return (b)
    else:
        # global b
        b=b-1
        return (b)
c=list(map(timer,range(1,t+1)))
print(c[t-1])

s="shubham"
print('\n'.join(s))

l=[1,2,3,4,5,6,7,8,9]
b=next(map(lambda a:1 if a==3 else -1,l))
print(b)

test=[1,2,3,6,58,78,50,651,36,79,1009]
print(next( filter(lambda x:1 if x%5==0 else -1,test) ))

next( x for x in test if x%5==0 )

k=40
arr=[13, 91 ,5 ,100, 5, 12,5 ,79 ,99, 87, 59, 65 ,62 ,73 ,93 ,73 ,63,65 ,59, 46 ,67, 35 ,22 ,55 ,50, 53, 38 ,79 ,75 ,44, 95 ,53, 5 ,73, 44 ,94 ,95, 21, 60 ,2, 32, 48, 72 ,13 ,91, 74, 79, 99 ,17 ,31 ,53, 20, 88 ,17, 54, 47, 56, 79, 23, 49, 95, 81, 9 ,50, 12, 20, 45, 82, 44, 82, 93 ,15, 73, 51, 65, 96, 4, 77, 37, 41, 30, 11, 65 ,100 ,62, 51, 64 ,48 ,12, 11, 68, 81, 46, 37 ,10 ,46, 75, 82, 21, 23]
arr.sort()

print(arr)
print()

def chk1(a):
    c=list(map(lambda x:1 if (a<x) and (a+x)%k==0 else -1,arr))
    return c.count(1)
d=list(map(chk1,arr))
print(sum(d))

from itertools import permutations 
perm = list(permutations(arr, 2))
# print(perm) 
d=list(map(lambda x: 1 if(x[0]<x[1] and (x[0]+x[1])%k==0) else -1,perm))
print(d.count(1))
# return d.count(1)
# return sum(d)

from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 



i=c=0
a=len(s)%m
print("A",a)
s=s[:len(s)-a]
print("S",s)
while(i!=len(s)-(m-1)):
    e=[]
    e=s[i:i+m]
    print("I",i)
    print("E",e)
    if(sum(e)==d):
        c=c+1
    i=i+1
print(c)

a=input()

a=[1,2,3,4,5]
a.pop(1)
print(a)

import string 
test_list = list(string.ascii_lowercase) 
print(test_list)

a=1243
a=list(str(a))
print(a)


n=110110015
a=list(str(n))
a=[int(x) for x in a]
print(a)
# print(a)
# c=0
a=list(filter(lambda a: a != 0, a))
print(a)
print(sum(list(map(lambda x:1 if(n%x==0) else 0,a))))

p=[21 ,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 1 ,2 ,3, 4, 5 ,6 ,7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18 ,19, 20]
d=[p.index(p.index(x)+1)+1 for x in range(1,len(p)+1)]
d=[str(x) for x in d]
d="".join(d)
d=[1,3123,4341,132]
d=[str(x) for x in d]
print('\n'.join(d))

a=[0,-1,2,1]
k=3
d=list(map(lambda x:1 if(x<=0) else -1,a))
if(d.count(1)>=k):
    print("NO")
else:
    print("YES")

a=[1,5,3,6,2,5,3]
a=list( dict.fromkeys(a) )
print(a)

a="shubhamshubham"
a=list(a)
b=list((set(a)))
# b=''.join(b)
print(b)

[a.remove(x) for x in b]
print(a)
def chk(z):
    if z in b:
        return 0
    else:
        return 1
d=list(map(chk,a))
print(sum(d)+len(b))



s=set("shubham")
b=set("sharma")
print(s.symmetric_difference(b))

a=[1,2,3,4,1,2]
d=[x-2 for x in a]
print(d)
print(a.index(2))

a=[1,2,3,3,3,7,7,5]
print(set(a))

d={1:1,3:3,4:3,5:1}
print(d[3])

# function to return key for any value 
def get_key(val): 
	for key, value in my_dict.items(): 
		if val == value: 
			return key 

	return "key doesn't exist"

# Driver Code 

my_dict ={"java":100, "python":100, "c":11} 

print(get_key(100)) 
print(get_key(11)) 

a=[1,2,3,1,2,3,4,5]
d={a.count(x):x for x in a}
print(d)

from itertools import combinations_with_replacement 
d=[]
a=1
b=2
d=[1,2]
perm=list(combinations_with_replacement(d,3))
print(perm)

from itertools import product
arrays = [(1),(2)]
cp = list(product(*arrays))
print(cp)


a=dict()
print(a)
a[0]="HI"
print(a)

data =dict()
data['a'] = 1 
print (data)

print("{} and {}".format(1,2))

a=input()
b=input()
c=input()
b=b.split()
c=c.split()
b=[int(x) for x in b]
c=[int(x) for x in c]

def chk(p,q):
    if(p>q or p==q):
        return 0
    else:
        return 1

z=list(map(chk,b,c))
if(sum(z)==0):
    print('Yes')
else:
    print('No')


i=0
def solve(A):
    A=sorted(A)
    def chk(a):
        global i
        if (len(A)-i-1)==a:
            i=i+1
            return 1
        else:
            i=i+1
            return 0
    z=list(map(chk,A))
    # print(sum(z))
    if(sum(z)==0):
        return (-1)
    else:
        return (1) 

l=[ -1, -2, 0, 0, 0, -3 ]
a=solve(l)
print(a)



i=0
class Solution:
    def solve(self,A):
        A=sorted(A)
        def chk(a):
            global i
            if (len(A)-i-1)==a:
                i=i+1
                return 1
            else:
                i=i+1
                return 0
        z=list(map(chk,A))
        print(sum(z))
        if(sum(z)>0):
            return (1)
        else:
            return (-1) 

a=('1','2')
a=list(a)
a=[int(x) for x in (a)]
print(a)

for j in range(5):
    print(j)
    j=j+2

import math
def encryption(s):
    p=""
    s=s.strip()
    a=(int(math.sqrt(len(s))))
    #To check whether the number is perfect square root or not
    if int(a + 0.5) ** 2 == len(s):
        b=a
    else:
        b=a+1
    for i in range(b):
        j=0
        k=""
        while((i+j)<len(s)):
            print("I+J",i+j)
            k=k+s[i+j]
            j=j+a
        p=p + k + " "
    return(p.lstrip())

print(encryption("iffactsdontfittotheorychangethefacts"))

i=3
b=4
# Complete the strangeCounter function below.
def strangeCounter(t):
    def chk(a):
        global i
        global b
        if(b==1):
            i=i*2
            b=i
            return b
        else:
            b=b-1
            return b
    z=list(map(chk,range(1,t+1)))
    # print(z)
    return(z[t-1])

from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
xi=[2,1,4,21]
sum = list(map(lambda x, y: x + y, li,xi) )
print (sum) 

s=[(1,2),(1,2)]
print(set(s))

# A Python program to print all  
# permutations using library function 
from itertools import combinations
  
# Get all permutations of [1, 2, 3] 
perm = combinations([2, 3],2) 
  
# Print the obtained permutations 
for i in list(perm): 
    print(i)

from itertools import product
x=[2,3]
print([p for p in product(x, repeat=2)])

a='1001'

print(list(int(a))

a=['5','23']
b='\n'.join(a)
print(b)

a=[1,2,3]
a[3] is None

# Python 3
from functools import reduce

numbers = [1,2]
xi=[2,3]

def custom_sum(first, second):
    return first + second

a=1
b=2
A=[a,b]
print(A)
