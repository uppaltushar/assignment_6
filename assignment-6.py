#1
"""
def square(r):
    return r**2
r=int(input("enter"))

a=square(r)
area=4*3.14*a
print(area)
#2

def perfect(num):
    s=0
    for i in range(1,num):
        if(num%i==0):
            s=s+i
    if(s==num):
        print(num)
for i in range(1,1001):
    perfect(i)

#3
def table(n):
    for i in range(1,11):
        a=n*i
        print(n,'*',i,'=',a)
n=int(input("enter"))

p=table(n)
"""
#4
a=int(input("enter a"))
b=int(input("enter b"))

def fun(b):
    
    if(b==0):
        return 1
    else:
        return a*fun(b-1)
    
print(fun(b))
