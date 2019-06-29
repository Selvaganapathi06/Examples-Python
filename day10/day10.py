#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Printing dic value
board ={'color':'Red'}
print(f"The color of board: {board['color']}")


# In[3]:


#Modyfying dic value
board ={'color':'green'}
board['color'] = 'yellow'
print(f"The color of board: {board['color']}")


# In[5]:


#Deleting dic value
board ={'color':'green','points':10}
print(board)
del board['points']
print(board)


# In[6]:


#dic best practices
lan = {'selva':'c','gana':'c++','pathi':'python'
      }
fav_lan = lan['selva'].title()
print(f"selva fav language is : {fav_lan}")


# In[7]:


#key error
board ={'color':'green','points':10}
print(board['origin'])


# In[10]:


#key error
board ={'color':'green','points':10}
x = board.get('origin',1000)
print(x)


# In[ ]:




