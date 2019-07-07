#!/usr/bin/env python
# coding: utf-8

# In[4]:


#while loop continuous
count = 1
while count <=5:
    print(count)
    count+=1
    


# In[7]:


#while loop continuous without next line
count = 1
while count <=5:
    print(count, end =" ")
    count+=1
    


# In[15]:


#User choose the letter when to quit
prompt = "\n tell me something and it will be repeat it"
prompt += "\n Enter 'quit' to end the program: "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


# In[16]:


#User choose the letter when to quit
pro = "\n tell me something and it will be repeat it"
pro += "\n Enter 'quit' to end the program: "
message = ""
while message != 'quit':
    message = input(pro)
    print(message)


# In[18]:


#Function
#Defining function in python
def greet_user():
    print("hello selvaganapathi")
greet_user()


# In[22]:


#doc string
#function with parameters
#passing input as arguments
def greet(name):
    """Basic function definition and argument via input passing"""
    print(name.title())
    print(f"hello, {name.title()}")
greet("selvaganapathi")


# In[ ]:




