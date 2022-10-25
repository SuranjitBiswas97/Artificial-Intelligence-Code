# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:41:33 2019

@author: User-PC
"""

class person:
    def __init__(self,fname=None,lname=None,id=0):
        self.firstName=fname
        self.lastName=lname
        self.id=id
        
    def printer(self):
        print(self.firstName,self.lastName,self.id)
        
ob=person()
ob.printer()
ob2=person('Suranjit','Ray',509)
ob2.printer()