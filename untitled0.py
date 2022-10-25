# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:01:09 2019

@author: Suranjit's_Laptop
"""
#a=eval(input())
#b=eval(input())
#sum=divmod(a,b)
#print(sum)

#import matplotlib.pyplot as plt
#x,y=[1,2,3,4,5], [1,2,3,4,6]
#plt.plot(x,y)



#a=[3,43,5,6,7,8,9,23,4]
#a.sort()
#print(a)

#a=[3,43,5,6,7,8,9,23,4]
#sorted(a)
#print(a)

#a=[2,2,4,3,67,87,90,12,43,45]
#print("5" in a)
#f=[]
#for x in range(5):
#    if x%2==0:
#        f.append(x)
#        print(f)


"""
zip and unzip
H=[1,2,3]
I=[4,5,6]
r=zip(H, I)
print(tuple(r))
for x,y in zip(H,I):
    print(x,y)
"""


"""
Fibnacci serie
a=eval(input())
x,y=0,1
print(x)
for i in range (1,a):
    print(y)
    x,y=y,x+y """
"""Fibnacci number cheek
    """
"""a=eval(input())
x,y=0,1
print(x)
while y<a:
    print(y)
    x,y=y,x+y
    a=a+1
    """
"""#factorial series
a=eval(input())
fact=1
for i in range(1,a+1):
    fact=fact*i
    print(fact)
factorial cheek    
a=eval(input())
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
"""
"""
#prime number
x=eval(input())
if(x>1):
    i=2;
    while i<x:
        if (x%i==0):
            print(x, 'not prime')
            break
        i=i+1
    else:
        print(x, 'prime number')
else:
    print(x, 'not prime')
    """
"""#prime number
x=eval(input())
if(x>1):
    for i in range(2,x):
        if(i%x==0):
            print(x, 'not prime')
            break
    else:
        print(x, 'prime number')
else:
    print(x, 'not prime')
    """
"""#namota
a=eval(input())
for i in range(1,a+1):
    print(a,"*",i,"=",a*i)
"""
"""#namota
a=eval(input())
i=1
while i<11:
    print(a,"*",i,"=",a*i)
    i=i+1
"""
#for i in range(65,91):
#    print(chr(i),end=" ")
#    if(i-1)%10==0:
#        print()

"""x=eval(input())
sum=0
for i in range (1,x+1):
    sum=sum+i
print(sum)

a=eval(input())
for i in range(1,a+1):
    print(a,"*",i,"=",a*i)
"""
"""a=eval(input())   
for n in range(a):
    for i in range(n):
        print("*",end=" ")
    print('\n')
    """
"""a=eval(input())   
for row in range(1,a+1):
    for column in range(row,0,-1):
        print(column,end=' ')
    print('\n')
    """
#a=eval(input())   
#for n in range(a,0,-1):
#    for i in range(n):
#        print("*",end=" ")
#    print('\n')
    
#string=input("")
#print(string.count('s',0,1000))
#print(string.count('a',0,1000))
 
#palimdrom 
#a=eval(input())
#temp=a
#rev=0    
#while a>0:
#    dig=a%10
#    rev=rev*10+dig
#    a=a//10
#if(temp==rev):
#    print('palinmdrom')
#else:
#    print(' not palinmdrom')

#class firstclass:
#    a=10
#    def firstclassmethod(self,x):
#        a=x
#        return a
#ob=firstclass()
#p=ob.firstclassmethod(30)
#print(p)
#    
#class secondclass:
#    a=10
#    def secondmethod(self):
#        self.b=20
#        print(self.b,secondclass.a)
#ob=secondclass()
#ob.a=20
#secondclass.b=50
#ob.secondmethod()
#class Person:
#    def __int__(self,fname,lname,id):
#        self.fristname=fname
#        self.lastname=lname
#        self.id=id
#ob=Person('Suranjit','biswas',509)
#print(ob.fristname)
#print(ob.lastname)
#print(ob.id)
#inheritance
#class thirdClass():
#    a=10
#    def __int__(self,x=15):
#        self.b=x
#    def thirdmethod(self):
#        self.c=15
#        print(self.a,self.b,self.c)
#class fourthclass(thirdclass):
#    def __init__(self,y=25):
#        super().__init__()
#        self.d=y
#    def fourthmethod(self):
#        print(self.a,self.b,self.d)
#ob.fourthclass()
#ob.fourthmethod()
#ob.thridmethod()
#exception
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("Devision by zero")

#* print kora
#size=7
#m=(2*size)-2
#for i in range(0,size):
#    for j in range(0,m):
#        print(end=" ")
#    m=m-1
#    for j in range(0,i+1):
#        print('* ',end=" ")
#    print(" ")

# even odd cheek
#x=eval(input("Enter The NUmber"))
#x=y=z=12
#x="bangladesh"
#print (x)
    
 #positive
#a=eval(input("Enter the Number:"))
#if(a>0):
#    print("Number Positive");
#elif(a==0):
#    print("number Zero");
#else:
#    print("number Negative");
 
 
# lear year cheek   
#a=eval(input())
#if (a%4==0 and a%100==0 and a%400==0):
#    print("this year is leap year");
#else:
#    
#    print("this year is not leap year");   

    
# This program adds two numbers

#num1 = 1.5
#num2 = 6.3
#
## Add two numbers
#sum = float(num1) + float(num2)
#
## Display the sum
#print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  


#num = input()
#if (num % 2 == 0):
#    print("Even Number")
#else:
#    print("Odd Number")  
 
  


    
 
    
    

