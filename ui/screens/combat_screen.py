import time
from data.repository import get_random_enemy, load_data, save_data, update_xp
from ui.components import clear_terminal, display_status, display_stresses
from utils import throw_fate_dices   

def display_combat_menu():
    print("Combat Menu:")
    print("1 - Attack enemy")
    print("2 - Escape")
    return input()

def combat_screen():
    enemy = get_random_enemy()
    enemy_physical_stress = enemy["stress"]["physical"]
    enemy_mental_stress = enemy["stress"]["mental"]
    char_defeated = False

    print(f"You found a {enemy["name"]}!")
    time.sleep(1)

    while True:
        data = load_data()
        
        clear_terminal()
        display_status()
        display_stresses()

        print("[todo: display monster]\n")

        answer = display_combat_menu()
        match answer:
            case "1":
                # Char attack:
                print("Your attack roll:")
                char_attack_roll = throw_fate_dices()

                char_attack_result = char_attack_roll + data["skills"]["fight"]
                print(f"(+ {data["skills"]["fight"]}) = {char_attack_result}")
                time.sleep(2)

                print("Enemy defence roll:")
                enemy_defence_roll = throw_fate_dices()

                enemy_defence_result = enemy_defence_roll + enemy["skills"]["fight"]
                print(f"(+ {enemy["skills"]["fight"]}) = {enemy_defence_result}")
                time.sleep(2)

                char_damage = char_attack_result - enemy_defence_result

                if char_damage > 0:
                    enemy_physical_stress -= char_damage
                    print(f"You dealt {char_damage} damage to the {enemy["name"]}!")
                else:
                    print(f"You did not dealt damage to the {enemy["name"]}...")
            
                time.sleep(1)

                if enemy_physical_stress <= 0:
                    print("You defeated the enemy!")
                    print(f"And gained {enemy["xp"]} xp point!")
                    update_xp(enemy["xp"])

                    break
                                
                # Enemy attack:
                print("\nNow the enemy will attack:\n")
                time.sleep(1)

                print("Enemy attack roll:")
                enemy_attack_roll = throw_fate_dices()

                enemy_attack_result = enemy_attack_roll + enemy["skills"]["fight"]
                print(f"(+ {enemy["skills"]["fight"]}) = {enemy_attack_result}")
                time.sleep(2)

                print("Your defence roll:")
                char_defence_roll = throw_fate_dices()

                char_defence_result = char_defence_roll + data["skills"]["fight"]
                print(f"(+ {data["skills"]["fight"]}) = {char_defence_result}")
                time.sleep(2)

                enemy_damage = enemy_attack_result - char_defence_result
                
                if enemy_damage > 0:
                    data["stress"]["physical"][0] -= enemy_damage
                    print(f"{enemy["name"]} dealt {enemy_damage} damage to you!")
                else:
                    print(f"{enemy["name"]} did not dealt damage to you...")
            
                time.sleep(1)

                if data["stress"]["physical"][0] <= 0:
                    print("You have been defeated...")
                    input("Press enter to continue...")

                    data["stress"]["physical"][0] = 1
                    char_defeated = True

            case "2":
                break
            case _:
                print("Please select a valid option!")
        
        time.sleep(1)

        save_data(data)
        
        if (char_defeated):
            return char_defeated
