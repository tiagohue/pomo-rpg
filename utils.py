import os
import platform
from random import randint
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALARM_FILE = os.path.join(BASE_DIR, "sounds", "alarm.wav")

def play_alarm():
    system = platform.system()

    if "ANDROID_ROOT" in os.environ or "com.termux" in sys.executable:
        # todo: make the sound work for termux
        # subprocess.run(["termux-media-player", "play", ALARM_FILE])
        
        return
    else:
        from playsound import playsound
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
    
    print(f"= {sum}", end=" ")
    return sum