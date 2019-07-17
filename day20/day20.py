#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Class completed example
class Car:
    """represent a car"""
    def __init__(self,make,model,year):
        """initilize attribute to describe the car"""
        self.make = make
        self.model = model
        self.year = year
    def describe(self):
        """returned a neatly formatted name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
mynewcar = Car('audi','a4','2019')
print(mynewcar.describe())


# In[2]:


#setting default values
class Car:
    """represent a car"""
    def __init__(self,make,model,year,meter):
        """initilize attribute to describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.meter = 0
    def describe(self):
        """returned a neatly formatted name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    def meter_read(self):
        """returned a neatly formatted name"""
        print(f"This is meter reading: {self.meter}")
        
mynewcar = Car('audi','a4','2019',20)
print(mynewcar.describe())
print(mynewcar.meter_read())


# In[ ]:




