import json
import os
import pyautogui
from time import sleep
from pynput import keyboard
from components.terminal_controller import clear_terminal, minimize_terminal, restore_terminal
from components.autoincremental_manager import load_value, increment_value
from components.config import SEQUENCE_PATH, actions, settings, running
from components.system_actions import execute_command, execute_screenshot


def reset_sequence():
    global actions, settings

    confirmation = input("¿Estás seguro de que quieres eliminar la secuencia en curso y reestablecer las configuraciones adicionales? (s/n): ").lower()
    if confirmation == 's':
        actions.clear()
        settings = {
            'fixed_pause': 1,
            'telegram_notifier': None,
        }
        print("Secuencia actual eliminada.")
    else:
        print("Eliminación cancelada.")
    input("Presiona <Intro> para continuar...")


def save_sequence():
    clear_terminal()

    if len(actions) < 2:
        print("La secuencia de acciones está vacía o contiene menos de 2 elementos.\nPor favor, añade más acciones antes de comenzar.")
        input("Presiona <Intro> para continuar...")
        return

    print("Introduzca un nombre descriptivo de archivo para identificar la secuencia.\n")
    file_name = input("Se recomienda utilizar la nomenclatura camelCase (por ejemplo, realizarLogin):\n").strip()
    file_name = "".join(c for c in file_name if c.isalnum() or c in (' ', '-')).rstrip()
    file_path = os.path.join(SEQUENCE_PATH, f"{file_name}.json")
    
    os.makedirs(SEQUENCE_PATH, exist_ok=True)
    
    try:
        with open(file_path, 'w') as file:
            sequence = {
                'settings': settings,
                'actions': actions
            }
            json.dump(sequence, file)
        print(f"Secuencia guardada como '{file_name}.json'")
    except IOError as e:
        print(f"Error al guardar la secuencia: {e}")
    input("Presiona <Intro> para continuar...")


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
            file_path = os.path.join(SEQUENCE_PATH, files[selected_index])
            if load_sequence(file_path):
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
    global settings, actions

    try:
        with open(file_path, 'r') as file:
            new_sequence = json.load(file)
            settings.clear()
            settings.update(new_sequence['settings'])
            actions.clear()
            actions.extend(new_sequence['actions'])
        return True
    except Exception as e:
        print(f"Error al cargar la secuencia: {e}")
        return False


def start_sequence():
    global running
    running = True
    clear_terminal()

    if len(actions) < 2:
        print("La secuencia de acciones está vacía o contiene menos de 2 elementos.")
        input("Por favor, añade más acciones antes de comenzar.")
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
    minimize_terminal()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    try:
        if iterations == 0:
            while running:
                for action in actions:
                    if not running: break
                    perform_action(action)
                    pause_if_required()
        else:
            for _ in range(iterations):
                if not running: break
                for action in actions:
                    if not running: break
                    perform_action(action)
                    pause_if_required()
    finally:
        listener.stop()
    
    restore_terminal()
    print("Ejecución finalizada!")
    input("Presione la tecla <Enter> para salir.")


def perform_action(action):
    action_type = action['type']
    args = action['args']
    
    if action_type == 'left_click':
        pyautogui.click(*args)
    elif action_type == 'double_click':
        pyautogui.doubleClick(*args)
    elif action_type == 'right_click':
        pyautogui.rightClick(*args)
    elif action_type == 'key':
        pyautogui.press(args[0])
    elif action_type == 'compound_key':
        pyautogui.hotkey(*args[0].split('+'))
    elif action_type == 'write':
        pyautogui.write(args[0])
    elif action_type == 'pause':
        sleep(float(args[0]))
    elif action_type == 'run_command':
        execute_command(*args)
    elif action_type == 'autoincrement':
        current_value = load_value()
        pyautogui.write(current_value)
        increment_value()
    elif action_type == 'screenshot':
        execute_screenshot(*args)


def pause_if_required():
    fixed_pause = settings.get('fixed_pause', 0)
    if fixed_pause > 0:
        sleep(fixed_pause)

