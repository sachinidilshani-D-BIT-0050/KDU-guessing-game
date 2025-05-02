<<<<<<< HEAD
import random 
number = random.randint(1, 100) 
print("Guess a number between 1 and 10") 
guess = int(input())
while True: 
    # (paste existing code here) 
    print("Play again? (y/n)") 
    if input().lower() != 'y': 
        break
=======
<<<<<<< HEAD
import random
number = random.randint(1, 10)
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
>>>>>>> fa2e419f286324e3b7bc1a9b5796019ef5d0a227
