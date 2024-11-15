import subprocess
import time
import keyboard
import random

try:
    import keyboard
except ImportError:
    print("Please wait, installing keyboard...")
    subprocess.run(["pip", "install", "keyboard"])
    import keyboard

welcome_message = """
- - - - - - - - - - - - - - - - - - - -
/$$      /$$           /$$                                                     /$$                      /$$$$$$              /$$                      /$$$$$$  /$$$$$$$$ /$$   /$$       /$$                                                        
| $$  /$ | $$          | $$                                                    | $$                     /$$__  $$            | $$                     /$$__  $$| $$_____/| $$  /$$/      | $$                                                        
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$    /$$$$$$       | $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$       | $$  \ $$| $$      | $$ /$$/       | $$$$$$$  /$$   /$$        /$$$$$$$  /$$$$$$  /$$$$$$/$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/   /$$__  $$      | $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$      | $$$$$$$$| $$$$$   | $$$$$/        | $$__  $$| $$  | $$       /$$_____/ |____  $$| $$_  $$_  $$|
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$        | $$    | $$  \ $$      | $$__  $$| $$  | $$  | $$    | $$  \ $$      | $$__  $$| $$__/   | $$  $$        | $$  \ $$| $$  | $$      |  $$$$$$   /$$$$$$$| $$ \ $$ \ $$|
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$  | $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$      | $$  | $$| $$      | $$\  $$       | $$  | $$| $$  | $$       \____  $$ /$$__  $$| $$ | $$ | $$|
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$        |  $$$$/|  $$$$$$/      | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/      | $$  | $$| $$      | $$ \  $$      | $$$$$$$/|  $$$$$$$       /$$$$$$$/|  $$$$$$$| $$ | $$ | $$|
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/         \___/   \______/       |__/  |__/ \______/    \___/   \______/       |__/  |__/|__/      |__/  \__/      |_______/  \____  $$      |_______/  \_______/|__/ |__/ |__/|
                                                                                                                                                                                                    /$$  | $$                                           
                                                                                                                                                                                                   |  $$$$$$/                                           
                                                                                                                                                                                                    \______/                                             
- - - - - - - - - - - - - - - - - - - -
"""

print(welcome_message)

slots = {1: "", 2: "", 3: ""}
selected_slot = 1
recording = False
recorded_keys = []

def save_recording(slot, name):
    slots[slot] = name

def delete_recording(slot):
    slots[slot] = ""
    print(f"Recording in Slot {slot} deleted.")

def simulate_random_keys():
    keys = ['w', 'a', 's', 'd']
    while keyboard.is_pressed('RePag'):
        random.shuffle(keys)
        for key in keys:
            keyboard.press_and_release(key)

def main():
    global recording, recorded_keys, selected_slot

    while True:
        if keyboard.is_pressed('RePag'):
            print("Activated - Turn off with 'RePag'")
            simulate_random_keys()

        if keyboard.is_pressed('insert'):
            selected_slot += 1
            if selected_slot > 3:
                selected_slot = 1
            print(f"Selected Slot: {selected_slot} - Recording: {slots[selected_slot]}")

        if keyboard.is_pressed('inicio'):
            print(f"Selected Slot: {selected_slot} - Recording: {slots[selected_slot]}")

        if keyboard.is_pressed('AvPag'):
            if not recording:
                recording = True
                recorded_keys = []
                print("Recording... Press 'AvPag' again to stop and save.")
            else:
                recording = False
                print("Recording stopped. Enter a name for the recording:")

                name = input("name: ")
                save_recording(selected_slot, name)
                print(f"Recording saved in Slot {selected_slot} with name: {name}")

        if keyboard.is_pressed('delete'):
            delete_recording(selected_slot)

        if recording:
            pressed_key = keyboard.read_event(suppress=True)
            if pressed_key.event_type == keyboard.KEY_DOWN:
                recorded_keys.append(pressed_key.name)

if __name__ == "__main__":
    main()

#---------

import subprocess
import time
import keyboard
import random

try:
    import keyboard
except ImportError:
    print("Please wait, installing keyboard...")
    subprocess.run(["pip", "install", "keyboard"])
    import keyboard

welcome_message = """
- - - - - - - - - - - - - - - - - - - -
/$$      /$$           /$$                                                     /$$                      /$$$$$$              /$$                      /$$$$$$  /$$$$$$$$ /$$   /$$       /$$                                                        
| $$  /$ | $$          | $$                                                    | $$                     /$$__  $$            | $$                     /$$__  $$| $$_____/| $$  /$$/      | $$                                                        
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$    /$$$$$$       | $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$       | $$  \ $$| $$      | $$ /$$/       | $$$$$$$  /$$   /$$        /$$$$$$$  /$$$$$$  /$$$$$$/$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/   /$$__  $$      | $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$      | $$$$$$$$| $$$$$   | $$$$$/        | $$__  $$| $$  | $$       /$$_____/ |____  $$| $$_  $$_  $$|
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$        | $$    | $$  \ $$      | $$__  $$| $$  | $$  | $$    | $$  \ $$      | $$__  $$| $$__/   | $$  $$        | $$  \ $$| $$  | $$      |  $$$$$$   /$$$$$$$| $$ \ $$ \ $$|
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$  | $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$      | $$  | $$| $$      | $$\  $$       | $$  | $$| $$  | $$       \____  $$ /$$__  $$| $$ | $$ | $$|
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$        |  $$$$/|  $$$$$$/      | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/      | $$  | $$| $$      | $$ \  $$      | $$$$$$$/|  $$$$$$$       /$$$$$$$/|  $$$$$$$| $$ | $$ | $$|
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/         \___/   \______/       |__/  |__/ \______/    \___/   \______/       |__/  |__/|__/      |__/  \__/      |_______/  \____  $$      |_______/  \_______/|__/ |__/ |__/|
                                                                                                                                                                                                    /$$  | $$                                           
                                                                                                                                                                                                   |  $$$$$$/                                           
                                                                                                                                                                                                    \______/                                             
- - - - - - - - - - - - - - - - - - - -
"""

print(welcome_message)

slots = {1: "", 2: "", 3: ""}
selected_slot = 1
recording = False
recorded_keys = []

def save_recording(slot, name):
    slots[slot] = name

def delete_recording(slot):
    slots[slot] = ""
    print(f"Recording in Slot {slot} deleted.")

def simulate_random_keys():
    keys = ['w', 'a', 's', 'd']
    while keyboard.is_pressed('RePag'):
        random.shuffle(keys)
        for key in keys:
            keyboard.press_and_release(key)
            time.sleep(0.1)

def main():
    global recording, recorded_keys, selected_slot

    while True:
        if keyboard.is_pressed('RePag'):
            print("Activated - Turn off with 'RePag'")
            simulate_random_keys()

        if keyboard.is_pressed('insert'):
            selected_slot += 1
            if selected_slot > 3:
                selected_slot = 1
            print(f"Selected Slot: {selected_slot} - Recording: {slots[selected_slot]}")

        if keyboard.is_pressed('inicio'):
            print(f"Selected Slot: {selected_slot} - Recording: {slots[selected_slot]}")

        if keyboard.is_pressed('AvPag'):
            if not recording:
                recording = True
                recorded_keys = []
                print("Recording... Press 'AvPag' again to stop and save.")
            else:
                recording = False
                print("Recording stopped. Enter a name for the recording:")
                name = input("name: ")
                save_recording(selected_slot, name)
                print(f"Recording saved in Slot {selected_slot} with name: {name}")

        if keyboard.is_pressed('delete'):
            delete_recording(selected_slot)

        if recording:
            pressed_key = keyboard.read_event(suppress=True)
            if pressed_key.event_type == keyboard.KEY_DOWN:
                recorded_keys.append(pressed_key.name)

if __name__ == "__main__":
    main()
