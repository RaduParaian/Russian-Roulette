import random
import time

import vs_2p
import vs_3p
import vs_4p
import vs_5p
import vs_6p
import vs_computer

from vs_2p import vs_2p_func
from vs_3p import vs_3p_func


with open("revolver_art.txt") as f:
    print(f.read())
    time.sleep(2)

print("\n------- Welcome to Russian Roulette -------")
time.sleep(2)

mode_choose = True
while mode_choose == True:
    print("Do you want to play against friends (2 - 6 players) or against computer?")
    time.sleep(2)
    print("2, 3, 4, 5, 6, or c")
    time.sleep(2)
    mode = input("Mode: ").lower()
    time.sleep(2)

    if mode == "2":
        mode_choose = False
        vs_2p_func()
    elif mode == "3":
        mode_choose = False
        vs_3p_func()
    elif mode == "4":
        mode_choose = False
    elif mode == "5":
        mode_choose = False
    elif mode == "6":
        mode_choose = False
    elif mode == "c":
        mode_choose = False
    else:
        print("\nInvalid choice, type '2', '3', '4', '5', '6', or 'c'")
        time.sleep(2)