#!/usr/bin/env python
# coding: utf-8

# In[1]:


#tuples to access last element
x =(100,200,300)
print(x[2])


# In[2]:


#tuples negative indexing used to access last element
x =(100,200,300)
print(x[-1])


# In[6]:


#Using for loop in tuple
x =(100,200,300)
print("\noriginal value defined")
for y in x:
    print(y)
x =(400,500,600)
print("\nmodified value defined")
for y in x:
    print(y)


# In[8]:


#if statements
cars = ['audi','bmw','benz','toyota']
for x in cars:
    if x =="bmw":
        print(x.upper())
    else:
        print(x.title())
        


# In[9]:


car = "Audi"
car =="audi"


# In[10]:


car = "Audi"
car.lower() =="audi"


# In[11]:


# !=
req_topping = "bread"
if req_topping != "Laddu":
    print("get me laddu")


# In[ ]:




