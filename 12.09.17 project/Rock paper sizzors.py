playing = True
if playing is True:
    playing = False
    player1points = 0
    player2points = 0
    player1 = str(input("player1 guess")).lower()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    player2 = str(input("player2 guess")).lower()
    x = 0
    while x != 4:
        x+=1
        if player1 == "rock" & player2 == "scissors":
            print("player one wins")
            player1points += 1
        if player1 == "scissors" & player2 == "paper":
            print("player one wins")
            player1points += 1
        if player1 == "paper" & player2 == "rock":
            print("player one wins")
            player1points += 1

        if player2 == "rock" & player1 == "scissors":
            print("player two wins")
            player2points += 1
        if player2 == "scissors" & player1 == "paper":
            print("player two wins")
            player2points += 1
        if player2 == "paper" & player1 == "rock":
            print("player two wins")
            player2points += 1

        if player1 == player2:
            x -= 1
            print("draw")

        if x == 3:
            if player1points > player2points:
                print("player 1 wins the game")
            elif player2points > player1points:
                print("player 2 wins the game")
            input("Again").lower()
            if input == "yes":
                playing = True
            elif input == "no":
                quit()
