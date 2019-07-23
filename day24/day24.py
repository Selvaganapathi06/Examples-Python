#!/usr/bin/env python
# coding: utf-8

# In[1]:


#File Errors
f =r"D:\python30daystraining\day24\NewTextDocument.txt"
with open(NewTextDocument.txt) as fileobj:
    con = fileobj.read()
print(con)


# In[4]:


with open(r"D:\python30daystraining\day24\NewTextDocument.txt", "w") as fileobj:
    con = fileobj.write("I love programming language")
print(con)
f= r"D:\python30daystraining\day24\NewTextDocument.txt"

f1 =open(f,"r")
print(f1.read())

