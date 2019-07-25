#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Exception Handling

#ex1 before exception handling

print("Enter two no i will divide them")
print("Enter q for quit")
while True:
    fi = input("Enter your first no: ")
    if fi =="q":
        break
    se = input("Enter your second no: ")
    if se =="q":
        break
    ans = int(fi)/int(se)
    print(ans)


# In[3]:


#ex1 after exception handling

print("Enter two no i will divide them")
print("Enter q for quit")
while True:
    fi = input("Enter your first no: ")
    if fi =="q":
        break
    se = input("Enter your second no: ")
    if se =="q":
        break
    try:
        ans = int(fi)/int(se)
    except ZeroDivisionError:
        print("Dont try to divide by number zero")        
    else:
        print(ans)
        


# In[4]:


#without exception handling 
a ="selva.txt"
b =open(a,"r")
c = b.read()


# In[5]:


#without exception handling 
a ="selva.txt"
try:
    b =open(a,"r")
    c = b.read()
except FileNotFoundError:
    print("Please specify correct system file path")
else:
    print(c)


# In[ ]:




