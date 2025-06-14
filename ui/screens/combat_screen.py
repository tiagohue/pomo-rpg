import time
from data.repository import get_random_enemy, load_data
from ui.components import clear_terminal, display_status
from utils import throw_fate_dices   

def display_combat_menu():
    print("Combat Menu:")
    print("1 - Attack enemy")
    print("2 - Escape")
    return input()

def combat_screen():
    data = load_data()

    enemy = get_random_enemy()
    enemy_physical_stress = enemy["stress"]["physical"]
    enemy_mental_stress = enemy["stress"]["mental"]

    print(f"You found a {enemy["name"]}!")
    time.sleep(1)

    while True:
        clear_terminal()
        display_status()

        print("[todo: display monster]")

        answer = display_combat_menu()
        match answer:
            case "1":
                print("Your roll:")
                char_roll = throw_fate_dices()
                time.sleep(1)

                print("Added bonus:")
                char_result = char_roll + data["skills"]["fight"]
                print(f"{char_roll} + {data["skills"]["fight"]} = {char_result}")
                time.sleep(1)

                print("Enemy roll:")
                enemy_roll = throw_fate_dices()
                time.sleep(1)

                print("Added bonus:")
                enemy_result = enemy_roll + enemy["skills"]["fight"]
                print(f"{enemy_roll} + {enemy["skills"]["fight"]} = {enemy_result}")
                time.sleep(1)
                
            case "2":
                break
            case _:
                print("Please select a valid option!")
        
        time.sleep(1)
        
