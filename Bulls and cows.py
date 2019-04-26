import random  # imports the random number#
lives = 7
cows = 0
bulls = 0
total = 0
int1 = 0
if int1 == 0:
    int1, int2, int3, int4 = random.sample(range(10), 4)
#str(int1)
#str(int2)
#str(int3)
#str(int4)
#int1 * 1000 + int2 * 100 + int3 * 10 + int4 == int(total)

int1 = str(int1)
int2 = str(int2)
int3 = str(int3)
int4 = str(int4)

numbers = [int1, int2, int3, int4]

print (int1, int2, int3, int4)
guess = input("enter a number")

i = 0
while i != 3:
    if guess[i] == total[i]:
        bulls += 1
    i += 1


lives -= 1
print("cows =", cows)
print("bulls =", bulls)
print("lives =", lives)
if guess == total:
   print("you win")
   print("it took you ", 7-lives, "guesses")
if lives == 0:
   print("you lost")
# iterate through the array/string/whatevs counting the number of times each shows up
# you need to then go through and compare positions: array[0] == guess[0]


