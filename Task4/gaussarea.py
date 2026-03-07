#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from matplotlib import pyplot as plt
from math import sqrt, pi, isclose
from scipy.integrate import quad

# Calling environment

A = float(input("Enter a value for A: "))
x0 = float(input("Enter a value for x0: "))
sig = float(input("Enter a value for sigma: "))
z0 = float(input("Enter a value for z0: "))

x_min = float(input("Enter a value for x_min: "))
x_max = float(input("Enter a value for x_max: "))

# Gaussian

def gauss(x, A, x0, sigma, z0):
   return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

Area, error = quad(gauss, x_min, x_max, args=(A, x0, sig, z0))

print(f"The area from {x_min} to {x_max} is {Area:.2f}")

# Plot of the curve

plt.figure(figsize=(8,6))

X_gauss = np.linspace(-10, 10, 200)
Y_gauss = gauss(X_gauss, A, x0, sig, z0)

plt.plot(X_gauss, Y_gauss, color='red', lw=2, label='Gaussian function')

# Integration Area

X = np.linspace(x_min, x_max, 200)
Y = gauss(X, A, x0, sig, z0)

plt.fill_between(X, Y, alpha=0.2, color='purple', label=f'Integrated area: {Area:.2f}')

plt.xlabel('x', fontsize=12)
plt.ylabel('gauss(x, A, x0, sigma, z0)', fontsize=12)
plt.title('Area under a Gaussian', fontsize=12)

plt.legend()

plt.grid()
plt.show()


# In[ ]:




