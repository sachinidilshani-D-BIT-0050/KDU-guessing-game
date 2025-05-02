import random 
number = random.randint(1, 75) 
print("Guess a number between 1 and 10") 
guess = int(input()) 
if guess == number: 
    print("You win!") 
else: 
    print(f"Wrong! The number was {number}")

print(f"Time taken: {time.time() - start_time:.2f}s")
