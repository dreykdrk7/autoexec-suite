import subprocess
import os
import platform
from config import *

def clear_terminal():
    os_name = platform.system()     # Check the operating system
    if os_name == "Windows":        # Clear command for Windows
        os.system("cls")
    else:                           # Clear command for Unix/Linux/MacOS
        os.system("clear")


def rename_terminal():
    print(f"\033]0;{APPLICATION_NAME}\007", end='', flush=True)

def get_screen_dimensions():
    output = subprocess.check_output("xdotool getdisplaygeometry", shell=True).decode('utf-8').strip()
    screen_width, screen_height = map(int, output.split())
    return screen_width, screen_height


def position_terminal(corner=True, center=False, hidden_size=[HIDDEN_WIDTH, HIDDEN_HEIGHT], visible_size=[TERMINAL_WIDTH, TERMINAL_HEIGHT]):
    screen_width, screen_height = get_screen_dimensions()

    try:
        window_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode('utf-8').strip()
        if corner:
            # Position in the bottom right corner and adjust to hidden_size
            subprocess.run(["xdotool", "windowmove", window_id, str(screen_width), str(screen_height)])
            subprocess.run(["xdotool", "windowsize", window_id] + list(map(str, hidden_size)))
        elif center:
            # Center the window and adjust to visible_size
            x = (screen_width - visible_size[0]) // 2
            y = (screen_height - visible_size[1]) // 2
            subprocess.run(["xdotool", "windowmove", window_id, str(x), str(y)])
            subprocess.run(["xdotool", "windowsize", window_id] + list(map(str, visible_size)))
    except subprocess.CalledProcessError as e:
        print("Could not adjust the terminal window")


def minimize_terminal():
    try:
        window_id = subprocess.check_output(["xdotool", "search", "--name", f"{APPLICATION_NAME}"]).decode('utf-8').strip()
        subprocess.run(["xdotool", "windowminimize", window_id])
    except subprocess.CalledProcessError as e:
        print("Could not minimize terminal window")


def restore_terminal():
    try:
        window_id = subprocess.check_output(["xdotool", "search", "--name", f"{APPLICATION_NAME}"]).decode('utf-8').strip()
        subprocess.run(["xdotool", "windowactivate", window_id])
    except subprocess.CalledProcessError as e:
        print("Could not restore terminal window")
