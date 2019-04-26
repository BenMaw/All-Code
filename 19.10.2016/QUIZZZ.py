target = 12
guesses = 0
userChoice = int(input(“Guess the number: ”))
while userChoice != target:
    guess = guess + 1
    if userChoice >= target:
        print(“Guess higher!”)
    else:
        print(“Guess lower!”)
print(“It took you” , guesses, “guesses”)







# input()