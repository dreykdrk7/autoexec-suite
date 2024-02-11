import subprocess
import os
import platform

def clear_terminal():
    os_name = platform.system()     # Check the operating system
    if os_name == "Windows":        # Clear command for Windows
        os.system("cls")
    else:                           # Clear command for Unix/Linux/MacOS
        os.system("clear")


def get_screen_dimensions():
    output = subprocess.check_output("xdotool getdisplaygeometry", shell=True).decode('utf-8').strip()
    screen_width, screen_height = map(int, output.split())
    return screen_width, screen_height


def position_terminal(corner=True, center=False, hidden_size=[400, 100], visible_size=[1000, 500]):
    screen_width, screen_height = get_screen_dimensions()
    try:
        window_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode('utf-8').strip()
        if corner:
            # Position in the bottom right corner and adjust to hidden_size
            x = screen_width - hidden_size[0]
            y = screen_height - hidden_size[1]
            subprocess.run(["xdotool", "windowmove", window_id, str(x), str(y)])
            subprocess.run(["xdotool", "windowsize", window_id] + list(map(str, hidden_size)))
        elif center:
            # Center the window and adjust to visible_size
            x = (screen_width - visible_size[0]) // 2
            y = (screen_height - visible_size[1]) // 2
            subprocess.run(["xdotool", "windowmove", window_id, str(x), str(y)])
            subprocess.run(["xdotool", "windowsize", window_id] + list(map(str, visible_size)))
    except subprocess.CalledProcessError as e:
        print("Could not adjust the terminal window")
