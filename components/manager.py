import json
import os
import pyautogui
from components.terminal_controller import clear_terminal
from config import SEQUENCE_PATH, actions


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
            load_sequence(os.path.join(SEQUENCE_PATH, files[selected_index]))
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
            actions = json.load(file)
        input(f"Secuencia cargada desde '{file_path}'.")
    except Exception as e:
        input(f"Error al cargar la secuencia: {e}")


def start_sequence():
    clear_terminal()

    if len(actions) < 2:
        input("La secuencia de acciones está vacía o contiene menos de 2 elementos.\nPor favor, añade más acciones antes de comenzar.")
        return

    try:
        iterations = int(input("Introduce el número de veces que se va a repetir la secuencia (0 para infinito): "))
        if iterations == 0:
            print("Presiona Ctrl+C para detener la ejecución.")
            while True:
                execute_actions(actions, 1)
        else:
            execute_actions(actions, iterations)
    except ValueError:
        print("Por favor, introduce un número válido.")
    except KeyboardInterrupt:
        print("\nEjecución cancelada antes de comenzar.")


def execute_actions(actions, iterations):
    try:
        for _ in range(iterations):
            for action in actions:
                action_type, *args = action

                if action_type == 'click':
                    x, y = args
                    pyautogui.click(x, y)
                    print(f"Click realizado en ({x}, {y}).")

                elif action_type == 'key':
                    key = args[0]
                    pyautogui.press(key)
                    print(f"Tecla '{key}' presionada.")

                elif action_type == 'write':
                    text = args[0]
                    pyautogui.write(text)
                    print(f"Escribiendo texto: {text}")

                else:
                    print(f"Acción '{action_type}' no reconocida.")

    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")
