import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10) # This function will create a random number

isGuessRight = False #Track whether your user has guessed your number

while isGuessRight != True:
    
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))