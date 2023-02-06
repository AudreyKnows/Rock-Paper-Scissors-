import random
import time

print("Welcome to Audrey's Classic Rock, Paper, Scissors's game!")

time.sleep(3)

print("Ready to play?")

time.sleep(3)

player = input("Alright! Pick your choice? 'rock, 'paper, 'scissors':")

time.sleep(3)

computer = random.choice(['rock', 'paper', 'scissors'])


print(f"player: {player}")
print(f"computer: {player}")

time.sleep(2)

if player == computer:
  print(" Great minds, think alike? It's a tie!")
elif player == 'rock' and computer == 'scissors':
  print("You Win!!")
elif player == 'paper' and computer == 'rock':
  print("You Win!")
elif player == 'scissors' and computer == 'paper':
  print("You Win!")
elif player == 'rock' and computer == 'rock':
  print("It's a Tie")
else:
  print("Sorry, You Lost! Try Again")

  


      
  
        



