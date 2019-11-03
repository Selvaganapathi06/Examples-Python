#!/usr/bin/env python
# coding: utf-8

# In[2]:


#If statement example1:
sport = input("Enter yuor favorte sport: ").upper()
team = input("Enter your favorte team: ").upper()
if sport == 'HOCKEY':
    print("Go Ahead Hockey")
    if team == 'SANKAR BOYS':
        print("Good luck team to get a cup")


# In[8]:


#If statement example2
sport = input("Enter yuor favorte sport: ").upper()
team = input("Enter your favorte team: ").upper()
sportsistennis = False
if sport == 'TENNIS':
    sportsistennis = True
teamiscsk=False
if team == 'CSK':
    teamiscsk=True
if sportsistennis and teamiscsk:
    print("Good luck csk to winning a cup")


# In[9]:


#If statement example3
sport = input("Enter yuor favorte sport: ").upper()
team = input("Enter your favorte team: ").upper()
if sport == 'CRICKET' and (team =='CSK' or team =='KKR'):
    print("Good luck team to winning a cup")
    

