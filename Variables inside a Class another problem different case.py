# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:24:06 2019

@author: User-PC
"""

class secondClass:
    var1=10
    def secondMethod(self):
        self.var2=10
        print(self.var1,secondClass.var2)
ob=secondClass()
ob.var1=20
secondClass.var2=50
ob.secondMethod()