import time
import ui.utils as utils
from gamification import load_data

def countdown(minutes):
    time_max = minutes * 60

    data = load_data()

    for passed in range(0, time_max + 1, 1):
        utils.draw_time_progress_bar(passed, time_max)
        time.sleep(1)
    print("\nPomodoro completed!")

def run_pomodoro():
    countdown(25)
    return True