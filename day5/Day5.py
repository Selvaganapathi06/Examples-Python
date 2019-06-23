#!/usr/bin/env python
# coding: utf-8

# In[2]:


#list using for loop

Students = ["Selva", "gana","pathi"]
for x in Students:
    print(x)


# In[3]:


#list using for loop and fstring
Students = ["Selva", "gana","pathi"]
for x in Students:
    print(f"{x.title()}, you are practizing daily")
print("Thank you very much")


# In[5]:


#Numeric list
a =list(range(1,6))
print(a)


# In[6]:


#numeric for loop
for x in range(1,11):
    print(x)


# In[7]:


#empty list assign value in dynamically
a = []
for x in range(1,16):
    val = x**2
    a.append(val)
print(a)


# In[ ]:




