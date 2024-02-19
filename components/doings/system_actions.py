import subprocess
import os
from components.terminal_controller import clear_terminal
from components.config import OUTPUT_COMMANDS_PATH


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

