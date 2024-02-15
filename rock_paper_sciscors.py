import random
score = [0,0]
player_name = input("enter your name")
while True:
    choice = ["rock","paper","scissor"]
    user_input = input("Please enter your choice. Choices are"+str(choice) + "\n")
    print("\n")
    print("your selected" + user_input)
    if user_input not in choice:
        print (user_input + "is not a valid choice")
        break
    else:
        computer_input = random.choice(choice)
        print("computer chose" + computer_input)
    if user_input == computer_input:
        print("it is a draw")
        score[0]+= 0.5
        score[1]+= 0.5
    elif user_input == "rock" and computer_input == "scissor":
        score[0]+= 0
        score[1]+= 1
        print("you win")
    elif user_input == "paper" and computer_input == "rock":
        score[0]+= 0
        score[1]+= 1
        print(" you win")
    elif user_input == "scissor" and computer_input == "paper":
        score[0]+= 0
        score[1]+= 1
        print("you win")
    elif user_input == "scissor" and computer_input == "rock":
        score[0]+= 1
        score[1]+= 0
        print("you lost")
    elif user_input == "paper" and computer_input == "scissor":
        score[0]+= 1
        score[1]+= 0
        print("you lost")
    elif user_input == "rock" and computer_input == "paper":
        score[0]+= 1
        score[1]+= 0
    play_again = input("do you want to play again? (y/n)")
    if play_again != ("y"):
        print("exiting the game")
        print("Computer   "   +     player_name)
        print (str(score[0]) +"        " + str(score[1])) 
        break
    