import os
from playsound import playsound

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALARM_FILE = os.path.join(BASE_DIR, "sounds", "alarm.wav")

def play_alarm():
    playsound(ALARM_FILE)