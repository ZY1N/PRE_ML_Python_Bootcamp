import random

def endscreen(turns, magicnumber):
    if(magicnumber == 42):
        print("The answer to the ultimate question of life, the universe and everything is 42.")
    else:
        print("Congratulations, you've got it!")
    if(turns == 1):
        print("Congratulations! You got it on your first try!")
    else:
        print(f'You won in {turns} attempts!')
    exit()

def main():
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")
    magicnumber = random.randrange(1, 100, 1)
    turns = 1
    while(1):
        guess = input("What's your guess between 1 and 99?\n")
        if(guess.isnumeric()):
            guess = int(guess)
            if(guess > magicnumber):
                print("Too high!")
            elif(guess < magicnumber):
                print("Too low!")
            else:
                endscreen(turns, magicnumber)
        elif(guess == "exit"):
            print("Goodbye!")
            break
        else:
            print("That's not a number.")
        turns += 1

if(__name__ == "__main__"):
    main()