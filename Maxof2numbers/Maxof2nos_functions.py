#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Write a function find a maximum of two numbers

def max2num(a,b):
    if a == b:
        print("both are equal")
    elif a > b:
        print("num1 is big", a)
    else:
        print("num2 is big",b)
        
if __name__=="__main__":

    
    num1 = int(input("Enter a first number: "))
    num2 =int(input("Enter a second number: "))
    max2num(num1,num2)
    
    


# In[ ]:




