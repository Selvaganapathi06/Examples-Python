#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Read files
#ex1
f = open(r"D:\python30daystraining\day23\NewTextDocument.txt","r")
print(f.read())


# In[24]:


#Read files
#ex1
f = open(r"D:\python30daystraining\day23\NewTextDocument.txt","r")
print(f.read())


# In[19]:


#ex2
path=r"D:\python30daystraining\day23\NewTextDocument.txt"
f = open(path,"r")
print(f.read())


# In[20]:


#ex3
path=r"D:\python30daystraining\day23\NewTextDocument.txt"
f = open(path,"r")
print(f.read(20))


# In[22]:


#ex4
path=r"D:\python30daystraining\day23\NewTextDocument.txt"
f = open(path,"r")
print(f.readline())
print(f.readline())
print(f.readline())


# In[23]:


#ex5
path=r"D:\python30daystraining\day23\NewTextDocument.txt"
f = open(path,"r")
for x in f:
    print(x)


# In[12]:


#ex6
with open(r"D:\python30daystraining\day23\New Text Document.txt") as fobj:
    print(fobj.read())


# In[26]:


#ex7
f = open(r"D:\python30daystraining\day23\NewTextDocument.txt","r")
print(f.read())
f.close()


# In[30]:


#writing exisisting file
f = open(r"D:\python30daystraining\day23\NewTextDocument.txt","a")
f.write("addditional added value")
f.close()
f = open(r"D:\python30daystraining\day23\NewTextDocument.txt","r")
print(f.read())
f.close()


# In[32]:


#ex1
f = open(r"D:\python30daystraining\day23\NewTextDocument.txt","w")
f.write("addditional added value")
f.close()
f = open(r"D:\python30daystraining\day23\NewTextDocument.txt","r")
print(f.read())
f.close()


# In[33]:


#create a new file and add the value
f = open(r"D:\python30daystraining\day23\NewTextDocument12.txt","x")
f.write("addditional added value")
f.close()
f = open(r"D:\python30daystraining\day23\NewTextDocument12.txt","r")
print(f.read())
f.close()


# In[37]:


#remove a file
import os
os.remove(r"D:\python30daystraining\day23\NewTextDocument13.txt")


# In[39]:


#check if file already exsist
import os
if os.path.exists(r"D:\python30daystraining\day23\NewTextDocument14.txt"):
    os.remove(r"D:\python30daystraining\day23\NewTextDocument14.txt")
else:
    print("file not present")


# In[40]:


#ex1
import os
if os.path.exists(r"D:\python30daystraining\day23\NewTextDocument14.txt"):
    os.remove(r"D:\python30daystraining\day23\NewTextDocument14.txt")
else:
    print("file not present")

