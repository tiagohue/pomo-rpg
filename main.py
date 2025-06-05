#!/usr/bin/env python3

from pomodoro import run_pomodoro
from gamification import update_pomos, load_data, play_alarm
from ui import display_status, clear_terminal

while True:
    clear_terminal()

    display_status(load_data())
    if run_pomodoro():
        play_alarm()

        update_pomos()
        
        answer = " "
        while answer != "n" and answer != "y":
            answer = input("Do you want another pomodoro? (y/n) ")
        
        if answer == "n":
            print("👋 Ok. See you later, adventurer!")
            break
