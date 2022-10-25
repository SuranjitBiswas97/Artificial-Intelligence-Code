# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:21:02 2019

@author: User-PC
"""

class secondClass:
    def secondMethod(self):
        print(secondClass.var1,self.var2)
ob=secondClass()
secondClass.var1=20
ob.var2=50
ob.secondMethod()