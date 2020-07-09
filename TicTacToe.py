import os
import time
import random

base = [""," "," "," "," "," "," "," "," "," "]

def print_base():
    print("   |   |   ")
    print(" "+base[1]+" | "+base[2]+" | "+base[3]+" ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+base[4]+" | "+base[5]+" | "+base[6]+" ")
    print("   |   |   ")
    print("---|---|---")
    print(" "+base[7]+" | "+base[8]+" | "+base[9]+" ")
    print("   |   |   ")

def is_winner(base,coin):
    if(base[1]==coin and base[2]==coin and base[3]==coin) or \
            (base[4] == coin and base[5] == coin and base[6] == coin) or \
            (base[7] == coin and base[8] == coin and base[9] == coin) or \
            (base[1] == coin and base[4] == coin and base[7] == coin) or \
            (base[2] == coin and base[5] == coin and base[8] == coin) or \
            (base[3] == coin and base[6] == coin and base[9] == coin) or \
            (base[1] == coin and base[5] == coin and base[9] == coin) or \
            (base[3] == coin and base[5] == coin and base[7] == coin):
        return True
    else:
        return False

def is_base_full(base):
    if " " in base:
        return False
    else:
        return True

while True:
    os.system("clear")
    print_base()

    choice = input("Please choose from 1 to 9 for X : ")
    choice = int(choice)

    if base[choice]==" ":
       base[choice]="X"
    else:
        print("That space is already in use.")
        time.sleep(1)

    if is_winner(base,"X"):
        os.system("clear")
        print_base()
        print("X wins")
        break

    os.system("clear")
    print_base()

    if is_base_full(base):
        print("Tie")
        break

    choice = input("Please choose from 1 to 9 for O : ")
    choice = int(choice)

    if base[choice] == " ":
        base[choice] = "O"
    else:
        print("That space is already in use.")
        time.sleep(1)

    if is_winner(base, "O"):
        os.system("clear")
        print_base()
        print("O wins")
        break

    os.system("clear")
    print_base()

    if is_base_full(base):
        print("Tie")
        break
