#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Using Parent class
class Mom:
    var1 = "I am your mom"
class Dad:
    var2 ="I am your dad"
#Child class
class Child(Mom,Dad):
    var3 = "I am your son"
cobj = Child()
print(cobj.var1)
print(cobj.var2)
print(cobj.var3)

