#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, tan, log, log10
from scipy.integrate import quad

# Start and end values

a = float(input("Enter starting value: "))
b = float(input("Enter ending value: "))

# x ranges from a to b

x = np.linspace(a, b, 100)

# User input function

user = input("Enter a function f(x)=")

# Function to evaluate user input function

def integral(x, a, b):
    y = eval(user)
    return y

# Calculates integral

I = quad(integral, a, b, args=(a,b))

print(f"Integral of f(x) is {I}")

