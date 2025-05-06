#Stone, Paper, Scissors

import random
game = ["stone", "paper", "scissors"]

 

x = input("Enter your choice (stone/paper/scissors)(or type 'exit' to quit): ")

y = random.choice(game)

if(x == "stone" and y == "paper"):
   print("you lose")
elif(x == "stone" and y == "scissors"):
   print("you win")

elif(x == "paper" and y == "stone"):
   print("you win")
elif(x == "paper" and y == "scissors"):
   print("you lose")

elif(x == "scissors" and y == "stone"):
   print("you lose")
elif(x == "scissors" and y == "paper"):
   print("you win")
   
elif(x == y):
   print("draw")

elif(x == "exit"):
   print("Thanks for playing!")

else:
   print("Invalid output")
