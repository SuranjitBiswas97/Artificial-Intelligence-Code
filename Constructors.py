# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:31:17 2019

@author: User-PC
"""

class person:
    def __init__(self,fname,lname,id):
        self.firstName=fname
        self.lastName=lname
        self.id=id
        
ob=person('Suranjit','Ray',509)
print(ob.firstName)
print(ob.lastName)
print(ob.id)