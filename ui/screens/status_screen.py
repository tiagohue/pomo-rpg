from data.repository import load_data
from ui.components import clear_terminal, display_character, display_status, display_stresses

def status_menu():
    print("Status Menu:")
    print("press enter - Exit")
    return input()

def status_screen():
    clear_terminal()
    display_status()
    display_character()
    data = load_data()
    print("Skills:")
    for skill in data["skills"]:
        print(f"{data["skills"][skill]} : {skill}")

    print()
    display_stresses()
    print()

    answer = status_menu()