import time
import threading
import ui.components as components

def wait_cancel(cancel_event):
    while not cancel_event.is_set():
        key = input()
        if key.strip() == "1":
            cancel_event.set()

def run_pomodoro(minutes):
    time_max = minutes * 60

    print("Press 1 to cancel pomodoro...")
    cancel_event = threading.Event()
    threading.Thread(target=wait_cancel, args=(cancel_event, ), daemon=True).start()

    for passed in range(0, time_max + 1, 1):
        if cancel_event.is_set():
            input("Pomodoro canceled!")
            return False
        components.draw_time_progress_bar(passed, time_max)
        time.sleep(1)

    print("\nPomodoro completed!")
    return True