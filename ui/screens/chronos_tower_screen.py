from random import randint
import time
from ui.screens.combat_screen import combat_screen
from ui.components import clear_terminal, display_status


def chronos_tower_menu():
    print("Chronos Tower Menu:")
    print("1 - Go to next room")
    print("2 - Try to rest")
    print("3 - Exit")
    return input()

def enter_random_room():
    # todo: randomize the next room
    rand = randint(1, 2)

    match rand:
        case 1:
            # room with monsters
            return combat_screen()
        case 2:
            # room perfect to camp
            print("todo")
            ''' use the campfire:
   .(
  /%/\
 (%(%))
.-'..`-.
`-'.'`-'
            '''
            time.sleep(1)
        case _:
            print("unespected error")

def try_to_rest():
    # todo: test if player rested well or was interrupted by enemies
    print("todo")

def time_tower_screen():
    enter_random_room()

    while True:
        clear_terminal()
        display_status()
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