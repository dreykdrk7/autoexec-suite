from components.terminal_controller import clear_terminal, position_terminal, minimize_terminal, restore_terminal
from components.actions import add_click_auto, add_click_manual, add_pause, add_keyboard_input, add_text
from components.manager import save_sequence, load_sequence, start_sequence
from config import HIDDEN_HEIGHT, HIDDEN_WIDTH, TERMINAL_HEIGHT, TERMINAL_WIDTH, actions


def show_main_menu():
    print("\nMenú Principal:")
    print("1. Crear nueva configuración de secuencia")
    print("2. Guardar secuencia actual")
    print("3. Cargar secuencia desde archivo")
    print("4. Iniciar ejecución")
    print("5. Salir")


def show_sequence_menu():
    print("\nMenú de Generación de Secuencia:")
    print("1. Añadir click automático (no sirve sobre cuadros de texto)")
    print("2. Añadir click manual (para donde no funcione el click automático)")
    print("3. Añadir pausa")
    print("4. Añadir entrada de teclado")
    print("5. Añadir entrada de texto")
    print("6. Detener generador de secuencia")


def main():
    try:
        while True:

            clear_terminal()
            show_main_menu()

            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                record_new_sequence()
            elif opcion == '2':
                print("Guardando secuencia actual...")
                save_sequence()
            elif opcion == '3':
                print("Cargando secuencia")
                load_sequence()
            elif opcion == '4':
                print("Iniciando la ejecucion de la secuencia")
                start_sequence()
            elif opcion == '5':
                print("Cerrando la aplicación. :)")
                break
            else:
                input("Opción no válida. Por favor, utilice una de las opciones disponibles.")
    except KeyboardInterrupt:
        print("\nFinalizando la ejecución del programa. :)")


def record_new_sequence():
    global actions

    while True:
        clear_terminal()
        show_sequence_menu()

        opcion = input("Selecciona una opción: ")
        print(actions)
        if opcion == '1':
            clear_terminal()
            position_terminal(corner=True)

            add_click_auto()
        elif opcion == '2':
            clear_terminal()
            position_terminal(corner=True, center=False)

            add_click_manual(actions)
            position_terminal(corner=False, center=True)
        elif opcion == '3':
            clear_terminal()
            add_pause(actions)
        elif opcion == '4':
            clear_terminal()
            add_keyboard_input(actions)
        elif opcion == '5':
            clear_terminal()
            add_text(actions)
        elif opcion == '6':
            break
        else:
            input("Opción no válida. Intente de nuevo.")
