import time 
start_time = time.time() 
import random 
number = random.randint(1, 100) 
print("Guess a number between 1 and 10") 
guess = int(input())
while True: 
    # (paste existing code here) 
    print("Play again? (y/n)") 
    if input().lower() != 'y': 
        break


import random
number = random.randint(1, 50)
print("Guess a number between 1 and 10")
guess = int(input())
if guess < number:
 print("Too low!")
elif guess > number:
 print("Too high!")


import random 
number = random.randint(1, 100) 
print("Guess a number between 1 and 10") 
guess = int(input()) 
if guess == number: 
    print("You win!") 
else: 
    print(f"Wrong! The number was {number}")
print(f"Time taken: {time.time() - start_time:.2f}s")
     