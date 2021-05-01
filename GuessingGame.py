import random

print('This is a guessing game, in this game a random number between 1 and 100 will be generated, you will try to guess this number, if your guess is within 10 values of the number, then the program will print out "warm"')
print('If your guess is not within 10 values of the number then the program will print out "Cold". When you guess the number, the program will print out the number of tries it took for you to guess the number ')

num = random.randint(1,101)
guesses = [0]


while True:
    
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
        
    break


while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
    
    guesses.append(guess)
    
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')