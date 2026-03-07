#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import sin, cos, exp, pi
from scipy import integrate
import matplotlib.pyplot as plt

# User input function

user_function = input("Enter a function f(x)= ")

# Start and end values

a = 0
b = pi

xx = np.random.uniform(a, b, 100)     # generate 100 x values from a to b

n = len(xx)                # Number of values
Sum = 0                   # Sum starts from 0

# Monte Carlo integration function
try:
    for i in range(n):
        x = xx[i]
        user = eval(user_function)
        Sum += user
    
    MC = ((b-a)/n) * Sum
    print(f"Integral of function f(x) = {user_function} is {MC:.6f}")
    
except NameError as e:
    print("\nERROR: Unknown function or variable!")
    print("HOW TO FIX: Use only  sin, cos, exp, pi")
    print(f"Details: {e}")
    
except SyntaxError as e:
    print("\nERROR: Incorrect syntax in function!")
    print("HOW TO FIX: Check for missing or extra symbols like commas, parentheses, etc.")
    print(f"Details: {e}")

except TypeError as e:
    print("\nERROR: Function not recognised or wrong type of operation!")
    print("HOW TO FIX: Ensure correct form of operation (e.g. x**2 instead of x^2)")
    print("Use only  sin, cos, exp, pi")

except ZeroDivisionError as e:
    print("\nERROR: Dividing by zero!")
    print("HOW TO FIX: Check that the denominator is not zero before performing the division.")

except Exception as e:
    print(f"\nUnexpected ERROR: {e}")


# In[ ]:




