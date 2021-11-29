#                               GAME

import random

Low = int(input('ENTER THE LOWEST RANGE: '))
High = int(input('ENTER THE HIGHEST RANGE: '))

print('\nguess range is from ',Low,' to',High )

n = random.randint(Low,High)
guess = None

while n != guess:
    
    guess = int(input("Enter an integer: "))
    
    if guess < n:
        print ("guess is low","\nguess= ",guess)
       
    elif guess > n:
        print ("guess is high","\nguess= ",guess)
        break

    else:
        print ("you guessed it!","\nguess= ",guess)
    print('\n') 
 
