import requests
import random
import math
import os

words = ['parroting', 'pecans', 'envelopments', 'popgun', 'waterjets', 'nitrify', 'ilks', 'synapsing', 'politesses', 'surplusages']

def play():
    logo = """
            _     ____  _      _____ _      ____  _        _____ ____  _      _____
            / \ /|/  _ \/ \  /|/  __// \__/|/  _ \/ \  /|  /  __//  _ \/ \__/|/  __/
            | |_||| / \|| |\ ||| |  _| |\/||| / \|| |\ ||  | |  _| / \|| |\/|||  \  
            | | ||| |-||| | \||| |_//| |  ||| |-||| | \||  | |_//| |-||| |  |||  /_ 
            \_/ \|\_/ \|\_/  \|\____\\_/  \|\_/ \|\_/  \|  \____\\_/ \|\_/  \|\____\
                                                                                    
        """
    chosen_word = random.choice(words)
    str = ["_"]*len(chosen_word)
    b = True
    c = True
    lives = math.ceil(len(chosen_word)/3)
    while(b and lives != 0):
        os.system('cls')
        if(c):
            print(logo)
            print(f"{str}\tYou have {lives} lives")
        else:
            print(logo)
            print(f"You have guessed wrong and lost one life(Lives - {lives})\n{str}")
            c = True
        print(chosen_word)
        ch = input("\nGuess the words -> ")
        if(len(ch)>0):
            ch = ch[0]
        if ch not in chosen_word:
                lives = lives - 1
                c = False
        else:
            for i in range(0,len(chosen_word)):
                if(chosen_word[i] == ch):
                    str[i] = ch
        if "_" not in str:
            b = False
            os.system('cls')
            print(logo)
            print(f"{str} was the word and you guessed it right,")
            print("You Won!")
            return
    os.system('cls')
    print(logo)
    print("You have lost, try again")
    

os.system('cls')
play()