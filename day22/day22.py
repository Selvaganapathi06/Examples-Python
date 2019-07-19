#!/usr/bin/env python
# coding: utf-8

# In[1]:


#with out module
x = int(input("Enter X: "))
y = int(input("Enter y: "))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
ans1 = add(x,y)
ans2 = sub(x,y)
ans3 = mul(x,y)
print(ans1)
print(ans2)
print(ans3)


# In[7]:


#module
import mathlo
x = int(input("Enter X: "))
y = int(input("Enter y: "))
ans1 = mathlo.add(x,y)
ans2 = mathlo.sub(x,y)
ans3 = mathlo.mul(x,y)
print(ans1)
print(ans2)
print(ans3)


# In[2]:


#with module
import numpy as np
x = int(input("Enter X: "))
y = int(input("ENter Y: "))
vec1 = np.array([x,y])
vec2 = np.array([-x,-y])

