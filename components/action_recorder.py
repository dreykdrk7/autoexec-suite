import pyautogui
import threading
from time import sleep
from datetime import datetime
from pynput.mouse import Listener as MouseListener
from components.terminal_controller import clear_terminal, position_terminal, minimize_terminal, restore_terminal
from components.autoincremental_manager import save_value as save_autoincremental_value

def add_click_manual(actions):
    clear_terminal()
    position_terminal(corner=True, center=False)

    coords = get_coordinates()
    actions.append(('click', *coords))
    actions.append(('pause', 0.1))

    clear_terminal()
    position_terminal(corner=False, center=True)
    print(f"Click añadido en ({coords[0]}, {coords[1]})")
    input("Pulsa cualquier tecla para continuar... ")


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


def add_keyboard_input(actions):
    clear_terminal()

    explanatory_text = """
    Ejemplos de teclas aceptadas:
    - "enter", "esc", "space", "tab"
    - Teclas de dirección: "up", "down", "left", "right"
    - Modificadores: "ctrl", "alt", "shift"
    - Función: "f1", "f2", ..., "f12"
    Escribe el nombre de la tecla tal como aparece en la lista para añadirla.
    """

    print(explanatory_text)
    key = input("Introduce la tecla que se enviará: ")
    actions.append(('key', key))
    actions.append(('pause', 1))

    print("Tecla añadida correctamente.\n")
    input("Pulsa cualquier tecla para continuar... ")


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
        actions.append(('click', x, y))
        actions.append(('pause', 0.1))
        print(f"Click añadido en ({x}, {y})")
        return False


def wait_click_and_log(actions):
    with MouseListener(on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, actions)) as listener:
        listener.join()
