from gamification import load_data, play_alarm, update_pomos
from pomodoro import run_pomodoro
from ui.screens.time_tower_screen import time_tower_screen
from ui.utils import clear_terminal, display_status

def main_menu():
    print("Main Menu:")
    print("1 - Start pomo")
    print("2 - Enter time tower")
    print("3 - Exit")
    return input()

def main_screen():
    while True:
        clear_terminal()
        display_status(load_data())
        menu_answer = main_menu()

        match menu_answer:
            case "1":
                if run_pomodoro():
                    play_alarm()

                    update_pomos()
                    
                    answer = " "
                    while answer != "n" and answer != "y":
                        answer = input("Do you want another pomodoro? (y/n) ")

                    if answer == "n":
                        print("👋 Ok. See you later, adventurer!")
                        break
            case "2":
                time_tower_screen()
            case "3":
                print("👋 Ok. See you later, adventurer!")
                break
            case _:
                input("Please select a valid option!")
