#!/usr/bin/env python
# coding: utf-8

# In[4]:


#looping through dictionaries
un = {'uname':'first','first':'selva','last':'gana',
     }
for key,value in un.items():
    print(f"\nkey :{key}")
    print(f"value: {value}")


# In[5]:


#looping through dictionaries only in key

un = {'uname':'first','first':'selva','last':'gana',
     }
for keyvalue in un.keys():
    print(f"\nkey :{keyvalue}")


# In[8]:


#looping through dictionaries only in value
un = {'uname':'first','first':'selva','last':'gana',
     }
for onlyval in un.values():
    print(f"\nvalue: {onlyval}")


# In[ ]:




