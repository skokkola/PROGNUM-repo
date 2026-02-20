#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import sqrt
a=float(input("Enter value for a: "))
b=float(input("Enter value for b: "))
c=float(input("Enter value for c: "))
D=b**2-4*a*c
if D==0:
    x=(-b)/(2*a)
    print(f"There is only ONE solution, which is x={x:.3f}")
elif D<0:
    print("There is NO solution")
else:
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print(f"There are TWO solutions, which are x1={x1:.3f} and x2={x2:.3f}")

