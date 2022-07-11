#Treasure Island
print("Welcome to Treasure Island. \n Your mission is to find treasure obviously.\n")
leri = input("Where do you want to start(left/right)?\n")
if leri == "left":
    swwa = input("Do you want to swim or wait?\n")
    if swwa == "swim":
        RBY = input("Which door do you want to go through(red/blue/yellow)?\n")
        if RBY == "red":
            print("Burned by fire, Game over!!!!!!!")
        elif RBY == "blue":
            print("Eaten by beasts, Game over!!!!!!!!!!")
        elif RBY == "yellow":
            print("YOU WIN!!!!!!!!")
        else:
            print("Game over")
    elif swwa == "wait":
        print("Attacked by trout, Game over\n")
    else:
        print("Attacked by trout, Game over\n")
elif leri == "right":
    print("Fall into hole. Game over.\n")
else:
    print("Fall into hole. Game over.\n")