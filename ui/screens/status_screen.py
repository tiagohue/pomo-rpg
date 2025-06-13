from data.repository import load_data
from ui.components import clear_terminal, display_character, display_status

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
    print(f"Physical Stress: {data["stress"]["physical"][0]}/{data["stress"]["physical"][1]}")
    print(f"Mental Stress: {data["stress"]["mental"][0]}/{data["stress"]["mental"][1]}")
    print()

    answer = status_menu()