import json
import os
import pyautogui
from time import sleep
from pynput import keyboard
from components.terminal_controller import clear_terminal, minimize_terminal, restore_terminal
from components.autoincremental_manager import load_value, increment_value
from config import SEQUENCE_PATH, actions, running


def save_sequence():
    clear_terminal()

    if len(actions) < 2:
        input("La secuencia de acciones está vacía o contiene menos de 2 elementos.\nPor favor, añade más acciones antes de comenzar.")
        return

    print("Introduzca un nombre descriptivo de archivo para identificar la secuencia.\n")
    file_name = input("Se recomienda utilizar la nomenclatura camelCase (por ejemplo, abrirNavegador):\n").strip()
    file_name = "".join(c for c in file_name if c.isalnum() or c in (' ', '-')).rstrip()
    file_path = os.path.join(SEQUENCE_PATH, f"{file_name}.json")
    
    os.makedirs(SEQUENCE_PATH, exist_ok=True)
    
    try:
        with open(file_path, 'w') as file:
            json.dump(actions, file)
        input(f"Secuencia guardada como '{file_name}.json'")
    except IOError as e:
        input(f"Error al guardar la secuencia: {e}")


def select_sequence_file():
    clear_terminal()
    
    if not os.path.exists(SEQUENCE_PATH):
        input("No hay secuencias guardadas para cargar.")
        return None
    
    files = [f for f in os.listdir(SEQUENCE_PATH) if f.endswith('.json')]
    if not files:
        input("No hay secuencias guardadas para cargar.")
        return None
    
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")
    
    choice = input("Seleccione el archivo de secuencia por su número (o 'cancelar' para salir): ")
    if choice.lower() == 'cancelar':
        return None
    
    try:
        selected_index = int(choice) - 1
        if selected_index >= 0 and selected_index < len(files):
            if load_sequence(os.path.join(SEQUENCE_PATH, files[selected_index])):
                input(f"Secuencia cargada desde '{file_path}'.")
            else:
                input(f"Error al cargar la secuencia desde '{file_path}'.")
        else:
            input("Selección no válida.")
            return None
    except ValueError:
        input("Por favor, introduzca un número.")
        return None


def load_sequence(file_path):
    global actions

    try:
        with open(file_path, 'r') as file:
            new_actions = json.load(file)
            actions.clear()
            actions.extend(new_actions)
        return True
    except Exception as e:
        print(f"Error al cargar la secuencia: {e}")
        return False


def start_sequence():
    global running
    running = True
    clear_terminal()

    if len(actions) < 2:
        input("La secuencia de acciones está vacía o contiene menos de 2 elementos.\nPor favor, añade más acciones antes de comenzar.")
        return

    try:
        iterations = int(input("Introduce el número de veces que se va a repetir la secuencia (0 para infinito): "))
        execute_actions(iterations)
    except ValueError:
        print("Por favor, introduce un número válido.")
    except KeyboardInterrupt:
        print("\nEjecución cancelada antes de comenzar.")


def on_press(key):
    global running
    if key == keyboard.Key.f2:
        running = False
        return False


def execute_actions(iterations):
    global running
    print("Pulsa F2 en cualquier momento para detener la ejecución del bucle.\nComenzamos!")
    sleep(5)
    minimize_terminal()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    try:
        if iterations == 0:
            while running:
                for action in actions:
                    if not running: break
                    perform_action(action)
        else:
            for _ in range(iterations):
                if not running: break
                for action in actions:
                    if not running: break
                    perform_action(action)
    finally:
        listener.stop()
    
    restore_terminal()
    input("Ejecución finalizada!\nPresione la tecla <Enter> para salir.")


def perform_action(action):
    action_type, *args = action
    if action_type == 'left_click':
        x, y = args
        pyautogui.click(x, y)
    elif action_type == 'double_click':
        x, y = args
        pyautogui.doubleClick(x, y)
    elif action_type == 'right_click':
        x, y = args
        pyautogui.click(x, y, button='right')
    elif action_type == 'key':
        key = args[0]
        pyautogui.press(key)
    elif action_type == 'write':
        text = args[0]
        pyautogui.write(text)
    elif action_type == 'pause':
        pause_seconds = args[0]
        sleep(pause_seconds)
    elif action_type == 'autoincrement':
        current_value = load_value()
        pyautogui.write(current_value)
        increment_value()
