import random

#You will get a random number between 1-9
NumInt = random.randrange(1, 9)

#This line tells you how many chanes you have
chanceCount=0

print("Print a number between 1 and 9")
print("you have 5 chances")

while chanceCount < 5:
    guess = int(input("Enter your guess: "))
    chanceCount = chanceCount + 1

    if guess < NumInt:
        print("Too low! Guess a number higher than ", guess)
        
    if guess > NumInt:
        print("Too high! Guess a number lower than ", guess)

    if guess == NumInt:
        print("You win!!!")
        break

    if not chanceCount < 5:
        print("You lose! The number is ", NumInt)
        