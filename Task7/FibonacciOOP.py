#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    
    def __init__(self):
        self.first = 0
        self.second = 1

    def Nth_term(self, N):
        a = self.first
        b = self.second
        
        for i in range(N-1):
            a, b = b, a + b    # Updates both numbers simultaneously
        return a

    def Divisible(self, N, M):
        results = []
        
        a = self.first
        b = self.second
        
        for i in range(N-1):
            if a % M == 0:
                results.append(a)

            a, b = b, a + b 
            
        return results

fib = Fibonacci()

# TEST

N = 100
M = 7

print(f"""N={N} and M={M}: 

The {N}th term is: {fib.Nth_term(N)} 

All Fibonacci numbers less than {N}th term that can be divided by {M} are: 
{fib.Divisible(N, M)}""")
            

