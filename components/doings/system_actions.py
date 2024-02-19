import subprocess
from components.terminal_controller import clear_terminal


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
            with open(output_file, 'w') as file:
                file.write(result.stdout)
            print(f"Salida guardada en: {output_file}")
        else:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

