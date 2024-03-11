import random
import time

def vs_3p_func():
    print("\nWhat is the first players name?")
    time.sleep(2)
    name1 = input("Name 1: ").capitalize()
    time.sleep(2)
    print("\nWhat is the second players name?")
    time.sleep(2)
    name2 = input("Name 2: ").capitalize()
    time.sleep(2)
    print("\nWhat is the third players name?")
    time.sleep(2)
    name3 = input("Name 3: ").capitalize()
    time.sleep(2)

    print("\nI will now load one bullet.\n")
    time.sleep(2)
    print("And spin the chamber.\n")
    time.sleep(2) 

    chambered_bullet = random.randint(1, 6)

    print(f"{name1}, first chamber")
    time.sleep(4)
    if chambered_bullet == 1:
        print("*BANG*")
        time.sleep(2)
        print(f"{name1} lost to the first chamber. {name2} and {name3}, you carry on.")
        time.sleep(3)
        exit()
    else:
        print("*click*")
        time.sleep(2)
        print(f"The bullet was in a different chamber. {name1}, is lucky.\n")
        time.sleep(3)
    
    print(f"{name2}, second chamber")
    time.sleep(4)
    if chambered_bullet == 2:
        print("*BANG*")
        time.sleep(2)
        print(f"{name2} lost to the second chamber. {name1} and {name3}, you carry on.")
        time.sleep(3)
        exit()
    else:
        print("*click*")
        time.sleep(2)
        print(f"The bullet was in a different chamber. {name2}, is lucky.\n")
        time.sleep(3)

    print(f"{name3}, third chamber")
    time.sleep(4)
    if chambered_bullet == 3:
        print("*BANG*")
        time.sleep(2)
        print(f"{name3} lost to the third chamber. {name1} and {name2}, you carry on.")
        time.sleep(3)
        exit()
    else:
        print("*click*")
        time.sleep(2)
        print(f"The bullet was in a different chamber. {name3}, is lucky.\n")
        time.sleep(3)

    print(f"{name1}, fourth chamber")
    time.sleep(4)
    if chambered_bullet == 4:
        print("*BANG*")
        time.sleep(2)
        print(f"{name1} lost to the fourth chamber. {name2} and {name3}, you carry on.")
        time.sleep(3)
        exit()
    else:
        print("*click*")
        time.sleep(2)
        print(f"The bullet was in a different chamber. {name1}, is lucky.\n")
        time.sleep(3)

    print(f"{name2}, fifth chamber")
    time.sleep(4)
    if chambered_bullet == 5:
        print("*BANG*")
        time.sleep(2)
        print(f"{name2} lost to the fifth chamber. {name1} and {name3}, you carry on.")
        time.sleep(3)
        exit()
    else:
        print("*click*")
        time.sleep(2)
        print(f"The bullet was in a different chamber. {name2}, is lucky.\n")
        time.sleep(3)

    print(f"{name3}, last chamber.")
    time.sleep(4)
    if chambered_bullet == 6:
        print("*BANG*")
        time.sleep(2)
        print(f"{name3} lost to the sixth chamber. {name1} and {name2}, you carry on.")
        time.sleep(3)
        exit()