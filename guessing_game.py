import random 
number = random.randint(1, 10) 
print("Guess a number between 1 and 10") 
guess = int(input())
while True: 
    # (paste existing code here) 
    print("Play again? (y/n)") 
    if input().lower() != 'y': 
        break