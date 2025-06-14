import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, 'save.json')
ENEMIES_FILE = os.path.join(BASE_DIR, 'enemies.json')

def load_data():
    with open(SAVE_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(SAVE_FILE, 'w') as f:
        json.dump(data, f)

def update_pomos():
    data = load_data()
    data["pomos"] += 1
    save_data(data)

def update_xp(xp_gained):
    data = load_data()
    xp = data["xp"]
    level = data["level"]
    xp += xp_gained

    while xp >= level + 1:
        xp = xp - (level + 1)
        level += 1
        print(f"🎉 Congratulations! Now your level is {level}!")

    data["xp"] = xp
    data["level"] = level

    save_data(data)
    input("Press enter to continue...")

def get_random_enemy():
    data = json.load(open(ENEMIES_FILE, 'r'))
    return data["slime"]