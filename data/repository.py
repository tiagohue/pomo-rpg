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

# remake the xp system later:
def update_xp(xp_gained):
    data = load_data()
    data['xp'] += xp_gained
    if data['xp'] >= data["level"] + 1:
        data['level'] += 1
        data['xp'] = 0
        print("🎉 Você subiu de nível!")
    save_data(data)

def get_random_enemy():
    data = json.load(open(ENEMIES_FILE, 'r'))
    return data["slime"]