import random
print("Number Guessing Game")
print("Guess a number (between 1 to 9)")

actualNumber=random.randint(1,9)

chances=5
while(chances>0):
    chances=chances-1
    guessedNumber=int(input("Enter your guess :- "))
    if(guessedNumber<actualNumber):
        print("Your guess was too low : Guess a higher number") 

    elif(guessedNumber>actualNumber):
        print("Your guess was too high : Guess a lower number") 
    else:
        print("Your Guess Was Correct!")

        break

if(chances==0):
    print("You Lost !")


