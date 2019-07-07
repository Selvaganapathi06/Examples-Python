#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Positional arguments
def describe(animaltype,petname):
    """Display positional arguments"""
    print(f"i have a {animaltype}")
    print(f"i have a {animaltype}'s name as {petname}")
describe("dog","jimmy")


# In[4]:


#keyword arguments
def describe(animaltype,petname):
    """Display positional arguments"""
    print(f"i have a {animaltype}")
    print(f"i have a {animaltype}'s name as {petname}")
describe(animaltype="dog",petname="jimmy")


# In[5]:


#return the value from a function
def fullname(fname,lname):
    """return value from a function"""
    fullname = f"{fname} {lname}"
    return fullname.title()
msg = fullname ("selva","ganapathi")
print(msg)


# In[ ]:




