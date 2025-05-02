<<<<<<< HEAD
import random
number = random.randint(1, 50)
print("Guess a number between 1 and 10")
guess = int(input())
if guess < number:
 print("Too low!")
elif guess > number:
 print("Too high!")
=======
import random 
number = random.randint(1, 10) 
print("Guess a number between 1 and 10") 
guess = int(input()) 
if guess == number: 
    print("You win!") 
else: 
    print(f"Wrong! The number was {number}")
>>>>>>> 86ca4c2b73e1f999dd82fea5c6afd4c6fde8f4af
