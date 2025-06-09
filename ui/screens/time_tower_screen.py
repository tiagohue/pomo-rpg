from ui.screens.combat_screen import combat_screen
from ui.components import clear_terminal, display_status


def time_tower_menu():
    print("Time Tower Menu:")
    print("1 - Go to next room")
    print("2 - Exit")
    return input()

def enter_random_room():
    # todo: randomize the next room
    combat_screen()

def time_tower_screen():
    enter_random_room()

    while True:
        clear_terminal()
        display_status()
        answer = time_tower_menu()
        match answer:
            case "1":
                enter_random_room()
            case "2":
                break
            case _:
                input("Please select a valid option!")