import pyautogui
import threading
from time import sleep
from datetime import datetime
from pynput.mouse import Listener as MouseListener
from components.config import *
from components.terminal_controller import clear_terminal, position_terminal, minimize_terminal, restore_terminal
from components.autoincremental_manager import save_value as save_autoincremental_value

def perform_action_with_coords(action_type, actions):
    clear_terminal()
    position_terminal(corner=True, center=False)

    coords = get_coordinates()
    if action_type == 'left_click':
        actions.append(('left_click', *coords))
    elif action_type == 'double_click':
        actions.append(('double_click', *coords))
    elif action_type == 'right_click':
        actions.append(('right_click', *coords))
    actions.append(('pause', 0.5))

    clear_terminal()
    position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_SMALL_HEIGHT])

    click_type = "Doble click" if action_type == 'double_click' else "Click"
    click_button = " derecho" if action_type == 'right_click' else ""
    print(f"{click_type}{click_button} añadido para las coordenadas -> X:{coords[0]}, Y:{coords[1]}")
    input("Pulsa cualquier tecla para continuar... ")


def add_left_click(actions):
    perform_action_with_coords('left_click', actions)


def add_double_click(actions):
    perform_action_with_coords('double_click', actions)


def add_right_click(actions):
    perform_action_with_coords('right_click', actions)


def add_click_auto(actions):
    clear_terminal()
    minimize_terminal()
    sleep(1)

    thread = threading.Thread(target=lambda: wait_click_and_log(actions))
    thread.start()
    thread.join()

    restore_terminal()
    input("Pulsa cualquier tecla para continuar... ")


def add_pause(actions):
    clear_terminal()

    tiempo = float(input("Introduce la duración de la pausa (en segundos): "))
    actions.append(('pause', tiempo))

    print("Pausa añadida correctamente.\n")
    input("Pulsa cualquier tecla para continuar... ")


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


def add_action_with_pause(actions, action_type, action_value):
    actions.append((action_type, action_value))
    actions.append(('pause', 1))
    print(f"Entrada {'simple' if action_type == 'key' else 'compuesta'} añadida correctamente.\n")
    input("Pulsa cualquier tecla para continuar... ")
    position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_MEDIUM_HEIGHT])


def add_keyboard_input(actions):
    clear_terminal()
    print_explanatory_text()

    key = input("Introduce la tecla que se enviará: ")
    add_action_with_pause(actions, 'key', key)


def add_compound_keyboard_input(actions):
    clear_terminal()
    print_explanatory_text()

    compound_key = input("Introduce la combinación de teclas que se enviará: ")
    add_action_with_pause(actions, 'compound_key', compound_key)


def add_text(actions):
    clear_terminal()

    string = input("Introduce el texto o la cadena que quieras repetir en la secuencia:\n")
    actions.append(('write', string))
    actions.append(('pause', 1))

    print("Texto añadido correctamente.\n")
    input("Pulsa cualquier tecla para continuar... ")


def add_autoincremental_number(actions):
    clear_terminal()

    start_value = input("Introduce el valor inicial del número autoincremental (0 para cargar el valor del archivo): \n")
    try:
        start_value = int(start_value)

        if start_value != 0:
            save_autoincremental_value(start_value)

        actions.append(('autoincrement', 0))
        input("Número autoincremental añadido.")
    except ValueError:
        input("Por favor, introduce un número válido.")


def generate_text_with_datetime(actions):
    clear_terminal()
    
    print("Nota: Al generar nombres de archivo, evita los siguientes caracteres: \n" +
          "< > : \" / \\ | ? * y cualquier carácter no imprimible.\n" +
          "En sistemas Unix/Linux, evita también el uso de ':'.\n")
    
    base_text = input("Introduce el texto base (la parte estática, por ejemplo, 'Reporte_'): \n")
    datetime_format = input("Introduce el formato de fecha y hora (por ejemplo, '%H-%M-%S_%d-%m-%Y'): \n")
    post_text = input("Introduce el texto adicional posterior a la fecha y hora \npor ejemplo, la extensión del archivo, deja en blanco si no es necesario): \n")
    
    try:
        current_datetime = datetime.now().strftime(datetime_format)
        full_text = f"{base_text}{current_datetime}{post_text}"

        actions.append(('write', full_text))
        input(f"Texto generado y añadido: {full_text}\nPresiona Enter para continuar...")
    except ValueError as e:
        input(f"Error en el formato de fecha y hora: {e}\nPresiona Enter para continuar...")


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


def on_click(x, y, button, pressed, actions):
    if pressed:
        actions.append(('left_click', x, y))
        actions.append(('pause', 0.1))
        print(f"Click añadido en ({x}, {y})")
        return False


def wait_click_and_log(actions):
    with MouseListener(on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, actions)) as listener:
        listener.join()
