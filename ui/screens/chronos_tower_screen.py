from random import randint
import time
from data.repository import load_data, save_data
from ui.screens.camp_screen import camp_screen
from ui.screens.combat_screen import combat_screen
from ui.components import clear_terminal, display_status, display_stresses


def chronos_tower_menu():
    print("Chronos Tower Menu:")
    print("1 - Go to next room")
    print("2 - Try to rest [todo]")
    print("3 - Exit")
    return input()

def enter_random_room():
    data = load_data()
    data["pomos"] -= 1
    save_data(data)
    
    # randomize the next room
    rand = randint(1, 4)

    if rand in range(1, 3):
        # room with monsters
        return combat_screen()
    else:
        camp_screen()

def try_to_rest():
    # todo: test if player rested well or was interrupted by enemies
    print("todo")
    time.sleep(1)

def time_tower_screen():
    enter_random_room()

    while True:
        clear_terminal()
        display_status()
        display_stresses()
        answer = chronos_tower_menu()
        match answer:
            case "1":
                if enter_random_room():
                    break
            case "2":
                try_to_rest()
            case "3":
                break
            case _:
                input("Please select a valid option!")