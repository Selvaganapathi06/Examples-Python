#!/usr/bin/env python
# coding: utf-8

# In[4]:


#creating the class
class Dog:
    """simple dog class"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        """"simulating sitting response from a dog"""
        print(f"{self.name} is now siiting")
        
    def rollover(self):
        """simulating roll over command from the dog"""
        print(f"{self.name} is now roll over")
mydog = Dog("jimmy",6)
mydog.sit()
mydog.rollover()
print(f"my dog name is {mydog.name}")
print(f"my dog age is {mydog.age}")
    


# In[ ]:




