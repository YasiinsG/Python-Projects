import sys
import random
import time



def menu():
    print ("Hello , Welcome to the celebrity dogs game")# Welcome message displayed.
    print ("1: Play Game or 2: Quit")# Displays options to user.
    userInput = int(input("Enter either '1' or '2' for one of the options above:  "))# Provides choice to user of playing game or leaving game.
    if userInput == (2):
        print ("Goodbye")
        sys.exit()# If 2 is chosen then appropriate message is displayed and the user exits the game.
    if userInput == (1):
        print ("You will now enter the game...")
        gameSelection()# If 1 is chosen then appropriate message is displayed and the user is directed to choose the amount of cards they would like to play with.
    else:
        print("Pick an appropriate option")
        menu()# If option is not 1 or 2 then appropriate message is displayed and the user is returned back to the menu.

def gameSelection():
    userNumCards = int(input("How many cards would you like to play with (between 4 and 30):  "))
    if userNumCards < 4 or userNumCards > 30:
        print("Pick an appropriate number of cards")
        gameSelection()
    if userNumCards %2 != 0:
        print("Please pick an even number")
        gameSelection()
    else:
        time.sleep(2)
        file = open("dogs.txt","r")
        global dogs
        dogs = []
        dogNames = []
        for x in range(userNumCards):
            dogNames.append(file.readline().strip())
        for x in range(userNumCards):
            dog = []
            dog.append(dogNames[x])
            exerciseNum = random.randint(1,5)
            dog.append(exerciseNum)
            
            intelligenceNum = random.randint(1,100)
            dog.append(intelligenceNum)
            
            friendlinessNum = random.randint(1,10)
            dog.append(friendlinessNum)
            
            droolNum = random.randint(1,10)
            dog.append(droolNum)

            dogs.append(dog)
            random.shuffle(dogs)
        
        unc=int(userNumCards/2)
        playerCards = (dogs[0:unc])
        computerCards = (dogs[unc :userNumCards + 1])
        game(playerCards, computerCards)

def game(playerCards, computerCards):
    print("\nHOW TO PLAY THE GAME")
    time.sleep(3)
    print("Firstly, you will be shown the NAME of your card,")
    time.sleep(3)
    print("You will then see along side the name FOUR numbers,")
    time.sleep(3)
    print("The first number is your dogs' EXERCISE, then its INTELLIGENCE, then its FRIENDLINESS and lastly its DROOL,")
    time.sleep(5)
    print("They are all measured differently:\nExercise:   1 - 5\nIntelligence:   1 - 100\nFriendliness:   1 - 10\nDrool:   1 - 10,")
    time.sleep(5)
    print("Aim to get the HIGHER number in EXERCISE, INTELLIGENCE and FRIENDLINESS,")
    time.sleep(3)
    print("Aim for a LOWER number in DROOL,")
    time.sleep(3)
    print("The game will now start... \n \n \n")
    time.sleep(3)

    turn = 'p'
    while len(playerCards) != 0 and len(computerCards) != 0:
        print("This is your card:\nName: ",playerCards[0][0],"\nExercise: ",playerCards[0][1],"\nIntelligence: ",playerCards[0][2],"\nFriendliness: ",playerCards[0][3],"\nDrool: ",playerCards[0][4],"\n")
        if turn == 'p':
            choice = int(input("Choose from between the options below: \n1(for exercise), \n2(for intelligence), \n3(for friendliness), \n4(for drool) \n"))
        else:
            print("It is the computer's turn \n")
            choice = random.randint(1,4)
            time.sleep(5)
            print("The computer has chosen : " , choice, "\n" )
            time.sleep(3)
        if choice == (1):
            if(playerCards[0][1]) > (computerCards[0][1]):
                print("You have won the round \nThe computer's card was:   " , computerCards[0], "\n \n")
                playerCards.append(playerCards[0])
                playerCards.append(computerCards[0])
                del computerCards[0]
                del playerCards[0]
                turn = 'p'

            elif(playerCards[0][1]) == (computerCards[0][1]):
                print("You have drawn! - So you win!")
                playerCards.append(playerCards[0])
                playerCards.append(computerCards[0])
                del computerCards[0]
                del playerCards[0]
                turn = 'p'

            else:
                print("You have lost the round \nThe computer's card was:   " , computerCards[0], "\n \n")
                computerCards.append(computerCards[0])
                computerCards.append(playerCards[0])
                del playerCards[0]
                del computerCards[0]
                turn = 'c'

        elif choice == (2):
            if(playerCards[0][2]) > (computerCards[0][2]):
                print("You have won the round \nThe computer's card was:   " , computerCards[0], "\n \n")
                playerCards.append(playerCards[0])
                playerCards.append(computerCards[0])
                del computerCards[0]
                del playerCards[0]
                turn = 'p'

            elif(playerCards[0][2]) == (computerCards[0][2]):
                print("You have drawn! - So you win!")
                playerCards.append(playerCards[0])
                playerCards.append(computerCards[0])
                del computerCards[0]
                del playerCards[0]
                turn = 'p'

            else:
                print("You have lost the round \nThe computer's card was:   " , computerCards[0], "\n \n")
                computerCards.append(computerCards[0])
                computerCards.append(playerCards[0])
                del playerCards[0]
                del computerCards[0]
                turn = 'c'

        elif choice == (3):
            if(playerCards[0][3]) > (computerCards[0][3]):
                print("You have won the round \nThe computer's card was:   " , computerCards[0], "\n \n")
                playerCards.append(playerCards[0])
                playerCards.append(computerCards[0])
                del computerCards[0]
                del playerCards[0]
                turn = 'p'

            elif(playerCards[0][3]) == (computerCards[0][3]):
                print("You have drawn! - So you win!")
                playerCards.append(playerCards[0])
                playerCards.append(computerCards[0])
                del computerCards[0]
                del playerCards[0]
                turn = 'p'

            else:
                print("You have lost the round \nThe computer's card was:   " , computerCards[0], "\n \n")
                computerCards.append(computerCards[0])
                computerCards.append(playerCards[0])
                del playerCards[0]
                del computerCards[0]
                turn = 'c'

        elif choice ==(4):
            if(playerCards[0][4]) < (computerCards[0][4]):
                print("You have won the round \nThe computer's card was:   " , computerCards[0], "\n \n")
                playerCards.append(playerCards[0])
                playerCards.append(computerCards[0])
                del computerCards[0]
                del playerCards[0]
                turn = 'p'

            elif(playerCards[0][4]) == (computerCards[0][4]):
                print("You have drawn! - So you win!")
                playerCards.append(playerCards[0])
                playerCards.append(computerCards[0])
                del computerCards[0]
                del playerCards[0]
                turn = 'p'

            else:
                print("You have lost the round \nThe computer's card was:   " , computerCards[0], "\n \n")
                computerCards.append(computerCards[0])
                computerCards.append(playerCards[0])
                del playerCards[0]
                del computerCards[0]
                turn = 'c'

        else:
            print("Choose an appropriate option \n")

    if len(playerCards) == 0:
        print("You have lost...")
        menu()
    else:
        print("You have won! \n You will now be returned to the menu...")
        menu()






menu()
