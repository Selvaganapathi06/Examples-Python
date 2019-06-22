#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sample list and print

bicycles = ["trek", "redline","hero"]
print(bicycles)


# In[2]:


#accessing first element in the list
print(bicycles[0])


# In[4]:


#Apply title()
print(bicycles[0].title())


# In[5]:


#replace element values
bicycles[0] = "Honda"
print(bicycles)


# In[6]:


#append
bicycles.append("ranger")
print(bicycles)


# In[7]:


#insert
bicycles.insert(1,"shine")
print(bicycles)


# In[8]:


#delete from a list
bicycles.pop()
print(bicycles)


# In[9]:


#delete specific element from a list
bicycles.pop(1)
print(bicycles)


# In[11]:


#sorting
cars = ["audi","bmw","benz","toyota"]
cars.sort()
print(cars)


# In[ ]:




