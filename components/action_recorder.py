import pyautogui
from time import sleep
import threading
from pynput.mouse import Listener as MouseListener
from components.terminal_controller import clear_terminal, position_terminal, minimize_terminal, restore_terminal

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
