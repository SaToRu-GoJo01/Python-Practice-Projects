import random
import os
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
logo = """
     _____   ____   _____ _  __  _____        _____  ______ _____     _____  _____ _____  _____ _____  ____  _____   _____ 
    |  __ \ / __ \ / ____| |/ / |  __ \ /\   |  __ \|  ____|  __ \   / ____|/ ____|_   _|/ ____/ ____|/ __ \|  __ \ / ____|
    | |__) | |  | | |    | ' /  | |__) /  \  | |__) | |__  | |__) | | (___ | |      | | | (___| (___ | |  | | |__) | (___  
    |  _  /| |  | | |    |  <   |  ___/ /\ \ |  ___/|  __| |  _  /   \___ \| |      | |  \___ \\\___ \| |  | |  _  / \___ \ 
    | | \ \| |__| | |____| . \  | |  / ____ \| |    | |____| | \ \   ____) | |____ _| |_ ____) |___) | |__| | | \ \ ____) |
    |_|  \_\\\____/ \_____|_|\_\ |_| /_/    \_\_|    |______|_|  \_\ |_____/ \_____|_____|_____/_____/ \____/|_|  \_\_____/
    """
    
while(True):
    print(logo)
    print("\t\tROCK PAPER SCISSORS GAME")
    print("Press 0, 1, and 2 to choose rock, paper , and scissors respectively")
    userChoice = int(input())
    print("YOUR CHOICE->")
    # print("YOU CHOSE" + str(userChoice))
    if userChoice == 0:
        print(rock)
    elif userChoice == 1:
        print(paper)
    elif userChoice == 2:
        print(scissors)
    else:
        print("INVALID CHOICE")



    print("COMPUTER CHOSE->")
    computerChoice = random.randint(0,2)
    if computerChoice == 0:
        print(rock)
    elif computerChoice == 1:
        print(paper)
    elif computerChoice == 2:
        print(scissors)
    else:
        print("INVALID CHOICE BY COMPUTER")

    if userChoice == computerChoice:
        print("DRAW")
    elif userChoice == 0 and computerChoice == 2:
        print("YOU WON")
    elif userChoice == 2 and computerChoice == 1:
        print("YOU WON")
    elif userChoice == 1 and computerChoice == 0:
        print("YOU WON")
    else:
        print("YOU LOST, TRY AGAIN")


    run = input("DO YOU WANT TO PLAY AGAIN, PRESS '1' TO PLAY AND '0' TO END GAME\n")
    if run == '0':
        break
    clear_screen()
