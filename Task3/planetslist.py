#!/usr/bin/env python
# coding: utf-8

# In[1]:


# First Method (FINAL)
masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

names = ['Sun', 'Jupiter', 'Saturn', 'Neptune', 
         'Uranus', 'Earth', 'Venus', 'Mars', 
         'Mercury', 'Moon', 'Pluto']

MoonMass = masses[-2] 

NewMasses = [] # New empty list with filtered masses

for mass in masses:
    if mass >= MoonMass:
        NewMasses.append(mass) # add to new list
        
print(NewMasses)

MassesList = masses[slice(6, None, 1)] # slicing the list
print(MassesList)

Sum = sum(MassesList)
Length = len(MassesList)

print(f"Average mass is {Sum/Length:.4e}")

