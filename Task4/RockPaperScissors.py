#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

player = str(input("Choose Rock (R), Paper (P) or Scissors (S): " ))  # Input players choice

game = np.array(['Rock', 'Paper', 'Scissors'])       # Array of choices
indx = np.random.randint(0, len(game), 1)            # Index of the choices
print(f"Opponents choice: {game[indx]}")

# If player chooses Rock (R)

if player == "R" and game[0]:
    print("You TIE")
elif player == "R" and game[1]:
    print("You LOSE")
elif player == "R" and game[2]:
    print("You WIN")

# If player chooses Paper (P)

elif player == "P" and game[0]:
    print("You WIN")
elif player == "P" and game[1]:
    print("You TIE")
elif player == "P" and game[2]:
    print("You LOSE")

# If player chooses Scissors (S)

elif player == "S" and game[0]:
    print("You LOSE")
elif player == "P" and game[1]:
    print("You WIN")
else:
    print("You TIE")


# In[ ]:




