from data.repository import update_pomos
from pomodoro import run_pomodoro
from ui.screens.status_screen import status_screen
from ui.screens.time_tower_screen import time_tower_screen
from ui.components import clear_terminal, display_character, display_status
from utils import play_alarm

def main_menu():
    print("Main Menu:")
    print("1 - Start pomo")
    print("2 - See status")
    print("3 - Enter time tower")
    print("4 - Exit")
    return input()

def main_screen():
    while True:
        clear_terminal()
        display_status()
        display_character()
        menu_answer = main_menu()

        match menu_answer:
            case "1":
                if run_pomodoro(25):
                    play_alarm()
                    update_pomos()
            case "2":
                status_screen()
            case "3":
                time_tower_screen()
            case "4":
                print("👋 Ok. See you later, adventurer!")
                break
            case _:
                input("Please select a valid option!")
