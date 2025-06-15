import time
from data.repository import load_data, save_data
from ui.components import clear_terminal, display_status, display_stresses
from utils import throw_fate_dices

def camp_menu():
    print("Camp Menu:")
    print("1 - Try camping")
    print("2 - Exit")
    return input()

def camp_screen():
    data = load_data()

    clear_terminal()
    display_status()
    display_stresses()

    print("You found a room perfect for camping!")
    print("You will get a bonus of (+2) to camp here!")
    print(r'''
   .(
  /%/\
 (%(%))
.-'..`-.
`-'.'`-'
    ''')

    answer = camp_menu()
    match answer:
        case "1":
            char_roll = throw_fate_dices()

            char_result = char_roll + data["skills"]["camp"]
            print(f"(+ {data["skills"]["camp"]}) = {char_result}")
            time.sleep(2)
            
            char_result += 2
            print(f"{char_result - 2} + 2 (bonus) = {char_result}")
            time.sleep(2)

            # todo: make the difficulty increase based on the tower floor
            difficulty = 1
            print(f"Difficulty level: {difficulty}")
            time.sleep(2)

            if char_result <= difficulty:
                print("Oh no! You couldn't camp in peace...")
                time.sleep(2)
            else:
                remaining_physical = data["stress"]["physical"][1] - data["stress"]["physical"][0]
                remaining_mental = data["stress"]["mental"][1] - data["stress"]["mental"][0]
                
                print("Oh yea! You camped in peace! And restored:")
                
                if char_result > remaining_physical:
                    data["stress"]["physical"][0] += remaining_physical
                    print(f"{remaining_physical} physical stress points.")
                else:
                    data["stress"]["physical"][0] += char_result
                    print(f"{char_result} physical stress points.")

                if char_result > remaining_mental:
                    data["stress"]["mental"][0] += remaining_mental
                    print(f"{remaining_mental} mental stress points.")
                else:
                    data["stress"]["mental"][0] += char_result
                    print(f"{char_result} mental stress points.")

                input("Press enter to continue...")

        case "2":
            return
        case _:
            input("Please select a valid option!")

    save_data(data)
    time.sleep(1)