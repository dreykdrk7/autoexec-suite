import os
from components.config import AUTOINCREMENTAL_PATH


def load_value():
    try:
        with open(AUTOINCREMENTAL_PATH, 'r') as file:
            return file.read().strip()
    except (FileNotFoundError, ValueError):
        return str(0)


def save_value(counter):
    with open(AUTOINCREMENTAL_PATH, 'w') as file:
        file.write(str(counter))


def increment_value():
    counter = int(load_value())
    counter += 1
    save_value(counter)
    return str(counter)


def reset_counter(value=0):
    save_counter(value)
