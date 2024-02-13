import pyautogui
import time

def add_click_manual(actions):
    coords = get_coordinates()
    actions.append(('click', *coords))
    actions.append(('pause', 0.1))
    input("Pulsa cualquier tecla para continuar... ")


def add_click_auto(actions):
    pass


def add_pause(actions):
    tiempo = float(input("Introduce la duración de la pausa (en segundos): "))
    actions.append(('pause', tiempo))

    print("Pausa añadida correctamente.\n")
    input("Pulsa cualquier tecla para continuar... ")


def add_keyboard_input(actions):
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

    print("Tecla añadida correctamente.\n")
    input("Pulsa cualquier tecla para continuar... ")


def add_text(actions):
    string = input("Introduce el texto o la cadena que quieras repetir en la secuencia:")

    for character in string:
        actions.append(('key', character))
        actions.append(('pause', 0.1))

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
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAlmacenando coordenadas...")
        return [x, y]
    