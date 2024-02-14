import argparse
import os
from components.config import SEQUENCE_PATH
from components.terminal_controller import rename_terminal, clear_terminal
from components.menus import main
from components.manager import load_sequence, execute_actions

def parse_arguments():
    parser = argparse.ArgumentParser(description='Automatiza secuencias de acciones.')
    parser.add_argument('--file', type=str, help='Carga un archivo de secuencia específico.')
    parser.add_argument('--n', type=int, default=1, help='Establece el número de iteraciones para la secuencia.')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    clear_terminal()
    rename_terminal()
    
    if args.file is not None:
        file_path = os.path.join(SEQUENCE_PATH, args.file)
        load_sequence(file_path)
        execute_actions(args.n)
    else:
        main()
