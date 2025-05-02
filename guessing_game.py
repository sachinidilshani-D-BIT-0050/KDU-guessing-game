<<<<<<< HEAD
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
=======
>>>>>>> e03cd43f9870f9877c131805402ac6cd80b52da6
import random 
number = random.randint(1, 100) 
print("Guess a number between 1 and 10") 
guess = int(input()) 
if guess == number: 
    print("You win!") 
else: 
    print(f"Wrong! The number was {number}")