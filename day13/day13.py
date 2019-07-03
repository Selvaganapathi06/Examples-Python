#!/usr/bin/env python
# coding: utf-8

# In[1]:


#getting dynamic input 
hei = input("enter your height in cm :")
hei1 = int(hei)
if hei1 >= 120:
    print("\n eligible for taking ticket in bus")
else:
    print("\n not eligible for taking ticket")


# In[3]:


#Modulas operator
a =4%2
b = 3%1
c = 11%4

print(a)
print(b)
print(c)


# In[6]:


#odd or even
num = input("Enter your no: ")
num1 = int(num)
if num1%2 == 0:
    print(f"\n the value {num1} is even number.")
else:
    print(f"\n the value {num1} is odd number.")


# In[7]:


#while loop
cur_val = 1
while cur_val <= 20:
    print(cur_val)
    cur_val = cur_val + 1


# In[ ]:




