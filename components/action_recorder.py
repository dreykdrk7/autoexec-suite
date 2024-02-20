import pyautogui
import threading
from time import sleep
from datetime import datetime
from pynput.mouse import Listener as MouseListener
from components.config import *
from components.terminal_controller import clear_terminal, position_terminal, minimize_terminal, restore_terminal
from components.autoincremental_manager import save_value as save_autoincremental_value


def perform_action_with_coords(action_type):
    clear_terminal()
    
    position_terminal(corner=True, center=False)
    coords = get_coordinates()
    position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_SMALL_HEIGHT])

    click_type = "Doble click" if action_type == 'double_click' else "Click"
    click_button = " derecho" if action_type == 'right_click' else ""
    print(f"{click_type}{click_button} añadido para las coordenadas -> X:{coords[0]}, Y:{coords[1]}")
    input("Presiona <Intro> para continuar...")
    return {
        'type': action_type,
        'args': list(coords)
    }


def add_left_click():
    perform_action_with_coords('left_click')


def add_double_click():
    perform_action_with_coords('double_click')


def add_right_click():
    perform_action_with_coords('right_click')


def add_pause():
    clear_terminal()

    while True:
        try:
            sleep_time = float(input("Introduce la duración de la pausa (en segundos): "))
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    print("Pausa añadida correctamente.")
    input("Presiona <Intro> para continuar...")
    return {
        'type': 'pause',
        'args': [sleep_time]
    }


def print_explanatory_text():
    position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_TALL_HEIGHT])

    explanatory_text = """
    Ejemplos de teclas y combinaciones aceptadas:

    Teclas simples:
    - "enter", "esc", "space", "tab", "del", "insert"
    - Teclas de dirección: "up", "down", "left", "right"
    - Teclas de modificación: "ctrl", "alt", "shift"
    - Teclas de función: "f1", "f2", ..., "f12"
    
    Combinaciones de teclas:
    - Separa las teclas con '+'. Por ejemplo: "ctrl+c", "alt+f4", "ctrl+shift+esc"
    - Algunas combinaciones útiles: "ctrl+v" (pegar), "ctrl+c" (copiar), "ctrl+z" (deshacer)
    
    Teclas especiales:
    - "home", "end", "pageup", "pagedown"
    - "capslock", "numlock", "scrolllock"
    - "printscreen", "pause", "break"
    
    Nota: Asegúrate de usar el nombre correcto de la tecla como se espera en pyautogui.
    """
    print(explanatory_text)


def add_simple_keyboard_input():
    clear_terminal()
    print_explanatory_text()

    while True:
        key = input("Introduce la tecla que se enviará (ej. 'a', 'enter'): ")

        if is_valid_key(key):
            action = add_keyboard_input('key', key)
            print(f"Entrada simple '{key}' añadida correctamente.\n")
            input("Presiona <Intro> para continuar...")
            return action
        else:
            print("La tecla introducida no es válida o no está soportada.")


def is_valid_key(key):
    valid_keys = set(pyautogui.KEYBOARD_KEYS)
    return key.strip().lower() in valid_keys


def add_compound_keyboard_input():
    clear_terminal()
    print_explanatory_text()

    while True:
        compound_key = input("Introduce la combinación de teclas que se enviará (ej. 'ctrl+c'): ")

        if is_valid_compound_key(compound_key):
            action = add_keyboard_input('compound_key', compound_key)
            print(f"Entrada compuesta '{compound_key}' añadida correctamente.\n")
            input("Presiona <Intro> para continuar...")
            return action
        else:
            print("La combinación de teclas introducida no es válida o no está soportada.")

def is_valid_compound_key(compound_key):
    valid_keys = set(pyautogui.KEYBOARD_KEYS)
    keys = compound_key.split('+')
    return all(key.strip().lower() in valid_keys for key in keys)


def add_keyboard_input(action_type, action_value):
    return {
        'type': action_type,
        'args': [action_value.lower()]
    }






def add_text():
    clear_terminal()
    string = input("Introduce el texto o la cadena que quieras repetir en la secuencia:\n")

    print("Texto añadido correctamente.")
    input("Presiona <Intro> para continuar...")
    return {
        'type': 'write',
        'args': [string]
    }


def add_autoincremental_number():
    clear_terminal()

    while True:
        start_value = input("Introduce el valor inicial del número autoincremental (0 para cargar el valor del archivo): \n")
        try:
            start_value = int(start_value)
            break
        except ValueError:
            print("No introdujo un número válido.")
            input("Presiona <Intro> para intentar de nuevo...")

    if start_value != 0:
        save_autoincremental_value(start_value)
    
    print("Número autoincremental añadido.")
    input("Presiona <Intro> para continuar...")
    return {
        'type': 'autoincrement',
        'args': [0]
    }


def generate_text_with_datetime():
    clear_terminal()

    print("Nota: Evita usar caracteres especiales en nombres de archivo como:\n" +
          "< > : \" / \\ | ? * y cualquier carácter no imprimible.\n" +
          "En sistemas Unix/Linux, evita también ':'.\n")

    base_text = input("Texto base (ej. 'Reporte_'): \n")
    
    datetime_format = input("Introduce el formato de fecha y hora (deja en blanco para usar '%d-%m-%Y_%H-%M-%S'): \n")
    if not datetime_format:
        datetime_format = "%d-%m-%Y_%H-%M-%S"
    
    post_text = input("Texto adicional posterior a la fecha y hora (ej. extensión del archivo, deja en blanco si no es necesario): \n")

    try:
        current_datetime = datetime.now().strftime(datetime_format)
        full_text = f"{base_text}{current_datetime}{post_text}"
        print(f"Texto generado: {full_text}")
    except ValueError as e:
        print(f"Error en el formato de fecha y hora: {e}\nInténtalo de nuevo.")
        return None

    input("Presiona <Intro> para continuar...")
    return {
        'type': 'write',
        'args': [base_text, datetime_format, post_text]
    }


def get_coordinates():
    print("Presiona Ctrl-C cuando hayas posicionado el cursor")

    try:
        while True:
            x, y = pyautogui.position()
            positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nAlmacenando coordenadas...")
        return [x, y]

