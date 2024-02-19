import subprocess
import os
import pyautogui
from datetime import datetime
from components.terminal_controller import clear_terminal
from components.config import OUTPUT_COMMANDS_PATH, SCREENSHOTS_PATH


def add_command_action(actions):
    clear_terminal()

    command = input("Introduce el comando a ejecutar: ")
    save = input("¿Deseas guardar la salida en un archivo? (s/n): ").lower().startswith('s')
    
    file_name = ""
    if save:
        file_name = input("Nombre del archivo donde se guardará la salida del comando: ")

    actions.append({
        'type': 'run_command',
        'args': [command, save, file_name]
    })
    if save:
        print(f"Comando a ejecutar: {command}")
        print(f"Se guardará la salida del comando en el archivo: {file_name}")
    else:
        print(f"Comando a ejecutar: {command}")
        print("-> No se va a guardar la salida del comando.")
    input("Pulsa cualquier tecla para continuar... ")


def execute_command(command, save_output=False, output_file=""):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        if save_output and output_file:
            full_output_path = os.path.join(OUTPUT_COMMANDS_PATH, output_file)
            output_dir = os.path.dirname(full_output_path)
            
            if not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)
            
            with open(full_output_path, 'a') as file:
                file.write(result.stdout)
            print(f"Salida guardada en: {full_output_path}")
        else:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")


def add_screenshot_action(actions):
    clear_terminal()

    base_file_name = input("Introduce el nombre del archivo para guardar la captura de pantalla (sin extensión): ")
    add_timestamp = input("¿Deseas añadir la fecha y hora al nombre del archivo? (s/n): ").lower().startswith('s')

    timestamp_format = ""
    if add_timestamp:
        # Solicita el formato del timestamp o usa un valor por defecto si se deja en blanco
        timestamp_format = input("Introduce el formato de fecha y hora (deja en blanco para usar '%H-%M-%S_%d-%m-%Y'): ")
        if not timestamp_format:
            timestamp_format = "%H-%M-%S_%d-%m-%Y"

    actions.append({
        'type': 'screenshot',
        'args': [base_file_name, timestamp_format]  # Guarda el nombre base y el formato del timestamp
    })

    print(f"Acción de captura de pantalla programada: {base_file_name} con formato de timestamp '{timestamp_format}'")
    input("Pulsa <Intro> para continuar... ")


def execute_screenshot(base_file_name, timestamp_format):
    timestamp = datetime.now().strftime(timestamp_format) if timestamp_format else ""
    file_name = f"{base_file_name}{timestamp}.png"
    full_screenshot_path = os.path.join(SCREENSHOTS_PATH, file_name)

    screenshot_dir = os.path.dirname(full_screenshot_path)
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir, exist_ok=True)

    pyautogui.screenshot(full_screenshot_path)
    print(f"Captura de pantalla guardada en: {full_screenshot_path}")


