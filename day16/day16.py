#!/usr/bin/env python
# coding: utf-8

# In[3]:


#default value in function prameters
def greet(pname, animal ='dog'):
    print(f"my pet name is: {pname}")
    print(f"my pet name is: {pname} and animal type: {animal}")
greet("babulu")


# In[4]:


#default value in function prameters and passing arguments
def greet(pname, animal ='dog'):
    print(f"my pet name is: {pname}")
    print(f"my pet name is: {pname} and animal type: {animal}")
greet("babulu", "horse")


# In[6]:


#function parameter error scenarios
def greet(pname, animal):
    print(f"my pet name is: {pname}")
    print(f"my pet name is: {pname} and animal type: {animal}")
greet("babulu")


# In[8]:


#function used return a value in dictionary format
def func(fname,lname):
    """function used return a value in dictionary format"""
    msg = {'firstname':fname,'lastname':lname}
    print(msg)
func("selva","ganapathi")


# In[10]:


#passing a for loop in function
def greet(names):
    """passing a for loop in function"""
    for x in names:
        print(f"hello,{x.title()}")
cusnames = ['selva','gana','pathi']
greet(cusnames)


# In[13]:


#Passing arbitary no of arguments
def make_pizza(*topping):
    print(topping)
make_pizza("chicken pizza","veg pizza","egg pizza")


# In[ ]:




