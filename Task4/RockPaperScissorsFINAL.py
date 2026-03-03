#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

player = str(input("Choose Rock (R), Paper (P) or Scissors (S)" ))  # Input players choice

game = np.array(['Rock', 'Paper', 'Scissors'])       # Array of choices
indx = np.random.randint(0, len(game), 1)            # Index of the choices
print(f"Opponents choice: {game[indx]}")

# If player chooses Rock (R)

if player == "R" and game[indx] == 'Rock':
    print("You TIE")
elif player == "R" and game[indx] == 'Paper':
    print("You LOSE")
elif player == "R" and game[indx] == 'Scissors':
    print("You WIN")

# If player chooses Paper (P)

elif player == "P" and game[indx] == 'Rock':
    print("You WIN")
elif player == "P" and game[indx] == 'Paper':
    print("You TIE")
elif player == "P" and game[indx] == 'Scissors':
    print("You LOSE")

# If player chooses Scissors (S)

elif player == "S" and game[indx] == 'Rock':
    print("You LOSE")
elif player == "P" and game[indx] == 'Paper':
    print("You WIN")
else:
    print("You TIE")


# In[ ]:




