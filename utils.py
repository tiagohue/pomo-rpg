import os
from random import randint
from playsound import playsound

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALARM_FILE = os.path.join(BASE_DIR, "sounds", "alarm.wav")

def play_alarm():
    playsound(ALARM_FILE)

def throw_fate_dices():
    sum = 0
    for i in range(4):
        rand = randint(-1, 1)
        if rand == -1:
            print(f"[-] ", end="")
        elif rand == 0:
            print(f"[ ] ", end="")
        else:
            print(f"[+] ", end="")
        sum += rand
    
    print(f"= {sum}")
    return sum