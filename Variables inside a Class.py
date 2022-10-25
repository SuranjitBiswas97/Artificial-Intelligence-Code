# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:12:49 2019

@author: User-PC
"""

class secondClass:
    var1=10
    def secondMethod(self):
        self.var2=20
        print(secondClass.var1,self.var2)
ob=secondClass()
ob.secondMethod()