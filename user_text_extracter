import datetime
import json
import os
import time
import pyperclip
from pynput import mouse, keyboard
import platform
import subprocess

# Output file
OUTPUT_FILE = "hover_output.json"
os.makedirs("screenshots", exist_ok=True)

# Platform check
IS_WINDOWS = platform.system() == "Windows"

# Get active window title
def get_active_window_title():
    try:
        if IS_WINDOWS:
            import win32gui
            hwnd = win32gui.GetForegroundWindow()
            return win32gui.GetWindowText(hwnd).strip()
        else:
            script = 'tell application "System Events" to get name of (processes where frontmost is true)'
            output = subprocess.check_output(['osascript', '-e', script]).decode().strip()
            return output
    except Exception as e:
        return f"[WindowError: {e}]"

# Simulate Ctrl+A, Ctrl+C and get clipboard content
def extract_focused_text():
    kb = keyboard.Controller()
    # Select All
    with kb.pressed(keyboard.Key.ctrl):
        kb.press('a')
        kb.release('a')
    time.sleep(0.1)
    # Copy
    with kb.pressed(keyboard.Key.ctrl):
        kb.press('c')
        kb.release('c')
    time.sleep(0.2)
    return pyperclip.paste().strip()

# On right-click press
def on_click(x, y, button, pressed):
    if button.name == 'right' and pressed:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        window_title = get_active_window_title()
        try:
            foctext = extract_focused_text()
            if not foctext:
                print("⚠ No text copied.")
                return
        except Exception as e:
            foctext = f"[Clipboard Error: {e}]"

        entry = {
            "timestamp": timestamp,
            "active_window": window_title,
            "foctext": foctext
        }

        try:
            if os.path.exists(OUTPUT_FILE):
                with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            else:
                logs = []

            logs.append(entry)

            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2)

            print(f"✅ Logged at {timestamp}")
        except Exception as e:
            print(f"❌ Error logging: {e}")

# Start mouse listener
print("🖱️ Right-click to extract page text as foctext... Ctrl+C to stop.")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
import datetime
import json
import os
import time
import pyperclip
from pynput import mouse, keyboard
import platform
import subprocess

# Output file
OUTPUT_FILE = "hover_output.json"
os.makedirs("screenshots", exist_ok=True)

# Platform check
IS_WINDOWS = platform.system() == "Windows"

# Get active window title
def get_active_window_title():
    try:
        if IS_WINDOWS:
            import win32gui
            hwnd = win32gui.GetForegroundWindow()
            return win32gui.GetWindowText(hwnd).strip()
        else:
            script = 'tell application "System Events" to get name of (processes where frontmost is true)'
            output = subprocess.check_output(['osascript', '-e', script]).decode().strip()
            return output
    except Exception as e:
        return f"[WindowError: {e}]"

# Simulate Ctrl+A, Ctrl+C and get clipboard content
def extract_focused_text():
    kb = keyboard.Controller()
    # Select All
    with kb.pressed(keyboard.Key.ctrl):
        kb.press('a')
        kb.release('a')
    time.sleep(0.1)
    # Copy
    with kb.pressed(keyboard.Key.ctrl):
        kb.press('c')
        kb.release('c')
    time.sleep(0.2)
    return pyperclip.paste().strip()

# On right-click press
def on_click(x, y, button, pressed):
    if button.name == 'right' and pressed:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        window_title = get_active_window_title()
        try:
            foctext = extract_focused_text()
            if not foctext:
                print("⚠ No text copied.")
                return
        except Exception as e:
            foctext = f"[Clipboard Error: {e}]"

        entry = {
            "timestamp": timestamp,
            "active_window": window_title,
            "foctext": foctext
        }

        try:
            if os.path.exists(OUTPUT_FILE):
                with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            else:
                logs = []

            logs.append(entry)

            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2)

            print(f"✅ Logged at {timestamp}")
        except Exception as e:
            print(f"❌ Error logging: {e}")

# Start mouse listener
print("🖱️ Right-click to extract page text as foctext... Ctrl+C to stop.")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
