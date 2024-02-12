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


def add_keyboard_input(actions):
    key = input("Introduce la tecla que se enviará: ")
    actions.append(('key', key))


def add_text(actions):
    string = input("Introduce el texto o la cadena que quieras repetir en la secuencia:")

    for character in string:
        actions.append(('key', character))
        actions.append(('pause', 0.1))

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
    