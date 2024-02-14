from components.terminal_controller import clear_terminal
from components.action_recorder import add_click_auto, add_left_click, add_double_click, add_right_click, add_pause, add_keyboard_input, add_text, add_autoincremental_number, generate_text_with_datetime
from components.manager import save_sequence, select_sequence_file, start_sequence
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
    print("2. Añadir click izquierdo (sirve para cualquier pixel visible)")
    print("3. Añadir doble click")
    print("4. Añadir click derecho")
    print("5. Añadir pausa")
    print("6. Añadir entrada de teclado")
    print("7. Añadir texto")
    print("8. Añadir número autoincremental (solo 1 por secuencia)")
    print("9. Añadir texto estático con fecha y hora (útil para nombres de archivo)")
    print("10. Detener generador de secuencia")


def main():
    try:
        while True:
            clear_terminal()
            show_main_menu()

            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                record_new_sequence()
            elif opcion == '2':
                save_sequence()
            elif opcion == '3':
                select_sequence_file()
            elif opcion == '4':
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
        if opcion == '1':
            add_click_auto(actions)
        elif opcion == '2':
            add_left_click(actions)
        elif opcion == '3':
            add_double_click(actions)
        elif opcion == '4':
            add_right_click(actions)
        elif opcion == '5':
            add_pause(actions)
        elif opcion == '6':
            add_keyboard_input(actions)
        elif opcion == '7':
            add_text(actions)
        elif opcion == '8':
            add_autoincremental_number(actions)
        elif opcion == '9':
            generate_text_with_datetime(actions)
        elif opcion == '10':
            break
        else:
            input("Opción no válida. Intente de nuevo.")
