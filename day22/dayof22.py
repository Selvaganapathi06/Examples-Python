#!/usr/bin/env python
# coding: utf-8

# In[14]:


import greet
greet.greeting("selva")


# In[15]:


#module
import arith
x = int(input("Enter X: "))
y = int(input("Enter y: "))
ans1 = arith.add(x,y)
ans2 = arith.sub(x,y)
ans3 = arith.mul(x,y)
print(ans1)
print(ans2)
print(ans3)


# In[16]:


import arith as a
x = int(input("Enter X: "))
y = int(input("Enter y: "))
ans1 = a.add(x,y)
ans2 = a.sub(x,y)
ans3 = a.mul(x,y)
print(ans1)
print(ans2)
print(ans3)


# In[17]:


#builtin module
import platform
platform.system()


# In[22]:


#builtin module
import platform
x=dir(platform)
print(x)


# In[31]:


from perinfo import person
a=perinfo.person["name"]
b=perinfo.person["age"]
c=perinfo.person["city"]
print(a)
print(b)
print(c)

