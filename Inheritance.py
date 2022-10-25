# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:56:15 2019

@author: User-PC
"""

class thirdClass():
    a=10
    def __init__(self,x=15):
        self.b=x
    def thirdMethod(self):
        self.c=15
        print(self.a,self.b,self.c)
class fourthClass(thirdClass):
    def __init__(self,y=25):
        super().__init__()
        self.d=y
    def fourthMethod(self):
        print(self.a,self.b,self.d)
ob=fourthClass()
ob.fourthMethod()
ob.thirdMethod()