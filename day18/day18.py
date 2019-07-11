#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Basic Class
class ClassName:
    def create(self,name):
        self.name = name
    def displayname(self):
        return self.name
    def savename(self):
        print(f"hello, {self.name}")
myobj =  ClassName()
myobj.create("selvaganapathi")
myobj.displayname()
myobj.savename()


# In[3]:


#simple ex1
class Exam1:
    x=5
myobj = Exam1()
print(myobj.x)


# In[12]:


#example of init()
class IniMeth:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def writ(self):
        print(f"Name: {self.name}.")
        print(f"Age: {self.age}.")
        
p = IniMeth("selva",18)
print(f"my name is {p.name}.")
print(f"my age is {p.age}.")
p.writ()


# In[13]:


#modify object properties
class IniMeth:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def writ(self):
        print(f"Name: {self.name}.")
        print(f"Age: {self.age}.")
        
p = IniMeth("selva",18)
p.writ()
p.age =28
print(p.age)


# In[ ]:




