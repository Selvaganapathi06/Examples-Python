#!/usr/bin/env python
# coding: utf-8

# In[5]:


#super class and sub class
class Parent:
    var1 = "building the console"
    var2 = "take care of front end"
Parentobj = Parent()
Parentobj.var2



# In[10]:


#super class and sub class
class Parent:
    var1 = "building the console"
    var2 = "take care of front end"
Parentobj = Parent()
Parentobj.var2
class Child(Parent):
    var3 = "take care of back end"
childobj = Child()
childobj.var1
childobj.var2


# In[12]:


#Constructor
class New:
    def __init__(self):
        print("i am doing good")
        print("i am well")
newobj = New()


# In[ ]:




