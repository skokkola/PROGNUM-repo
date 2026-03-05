#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import sin, cos, tan, log, log10
from scipy.integrate import quad

# Start and end values

a = float(input("Enter starting value: "))
b = float(input("Enter ending value: "))

# Generate 100 x values from a to b

x = np.random.uniform(a, b, 100)

# User input function

user_function = input("Enter a function f(x)=")

# Evaluate user input into mathematical form

def function(x):
    y = eval(user_function)
    return y

Function = function(x)

n = len(x) # Number of values

Sum = 0  # Sum starts from 0

# Sums the values of the function together

for i in range(1, n):
        Sum += Function[i]

# Monte Carlo function

MC = ((b-a)/n)*Sum

print(f"Integral of function f(x)={user_function} is {MC:.3f}")


# In[ ]:




