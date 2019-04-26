import random
import os
import string

count = 0
l = 0


def intValidation():
    while True:
        userInput = input("Enter your choice")
        try:
            val = int(userInput)
            break
        except ValueError:
            print("That's not an integer!")
    return val


def main():
    while True:
        print(
            "Welcome to the program.\n1. Run Program\n2. Change Settings\n3. Quit\n4. Generate Random 8 digit number.\n5. Shut down Computer\n6. End loop\n7. Random Character from String\n8. Length of an input")
        checked = intValidation()

        if checked == 1:
            print(checked)
            print("Running now")

        if checked == 2:
            print(checked)
            print("Settings are not here rip you")

        if checked == 3:
            print(checked)
            quit()

        if checked == 4:
            print(checked)
            number = random.randint(1, 99999999)
            print(number)

        if checked == 5:
            print(checked)
            os.system('shutdown -r')

        if checked == 6:
            print(checked)
            return welcome()

        if checked == 7:
            print(checked)
            print("Doesn't work rn.")

        if checked == 8:
            print(checked)
            userInput = input("Type something please:")
            print(len(userInput))
            count = 0
            l = 0
            while count != len(userInput):
                if userInput[l] == "A":
                    print("There is a capital A in this string.")
                count = count + 1
                l = l + 1


def welcome():
    print("Welcome to the program. Type menu to get to the menu, and quit to stop the program!")
    option1 = input()
    if option1 == "menu":
        main()
    if option1 == "quit":
        quit()
    else:
        print("That's not correct. Start again.")
        quit()


welcome()
