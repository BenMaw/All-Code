###########################################
# Name   choose_number
# what   this generates a computer generated numeber between 1 - 100
#        this returns the computer generated number
#
#
###########################################


import random
import time


def choose_number():
    c_number = random.randint(1, 100)
    print(c_number)
    return c_number


###########################################
# Name   users_number
# what   this gets a user generated number
#        this returns the user generated number
#
#
###########################################
def users_number():
    u_number = input("Guess a number, yer salty sausage")
    return u_number


###########################################
# Name   validate
# what   this checks if the numbers are too big or too small or equal to the generated number
#        this will return the victory condition
#
#
###########################################
def validate(guess, actual):
    guess = int(guess)
    if guess == actual:
        print("Arghh, ye Got Me Treasure")
        victory = True
        return victory
    elif guess > actual:
        print("Argh, Too Big Yer Sea Dog")
    elif guess < actual:
        print("Arggh, Ye number is too small")


def main():
    while True:
        if True:
            actual = choose_number()
            loop = True
            while loop is True:
                guess = users_number()
                win = validate(guess, actual)
                if win is True:
                    for i in range(20):
                        print("You win !!")
                        time.sleep(1)
                        loop = False


main()
