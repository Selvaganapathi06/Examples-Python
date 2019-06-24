#!/usr/bin/env python
# coding: utf-8

# In[1]:


#slicing a list
colors = ["red","green","yellow","blue","orange"]
#print only first three colors
print(colors[0:3])


# In[2]:


colors = ["red","green","yellow","blue","orange"]
#print last three colors
print(colors[2:5])


# In[4]:


colors = ["red","green","yellow","blue","orange"]
#only mention starting 
print(colors[2:])
print(colors[:2])


# In[5]:


#slicing using for loop

colors = ["red","green","yellow","blue","orange"]

for x in colors[:2]:
    print(x)





# In[6]:


#copying list
my_lang = ["tamil","english","hindi"]
frien_lan = my_lang[:]
print(frien_lan)


# In[9]:


#add item fro list
my_lang.append("malayalam")
frien_lan.append("telgu")
print(my_lang)
print(frien_lan)


# In[ ]:




