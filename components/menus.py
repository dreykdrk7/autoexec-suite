from components.terminal_controller import clear_terminal, position_terminal
from components.action_recorder import add_left_click, add_double_click, add_right_click, add_pause, add_simple_keyboard_input, add_compound_keyboard_input, add_text, add_autoincremental_number, generate_text_with_datetime
from components.system_actions import add_command_action, add_screenshot_action
from components.extra_settings import configure_fixed_pause, configure_telegram_bot
from components.sequence_manager import reset_sequence, save_sequence, select_sequence_file, start_sequence
from components.sequence_editor import view_actions, modify_actions_order, modify_action, delete_action
from components.config import *


def show_main_menu():
    print("\nMenú Principal:")
    print("1. Crear nueva secuencia o añadir acciones")
    print("2. Configurar parámetros adicionales")
    print("3. Editar secuencia actual")
    print("4. Guardar secuencia actual")
    print("5. Cargar secuencia desde archivo")
    print("6. Iniciar ejecución")
    print("7. Eliminar secuencia actual")
    print("8. Salir")


def show_sequence_menu():
    print("\nMenú de Generación de Secuencia:")
    print("1. Añadir click izquierdo")
    print("2. Añadir doble click")
    print("3. Añadir click derecho")
    print("4. Añadir pausa")
    print("5. Añadir entrada de teclado (tecla simple)")
    print("6. Añadir combinación de teclas (personalizable)")
    print("7. Añadir texto")
    print("8. Añadir número autoincremental")
    print("9. Añadir texto estático con fecha y hora")
    print("10. Ejecutar comando desde la terminal")
    print("11. Realizar una captura de pantalla")
    print("12. Detener generador de secuencia")


def show_additional_settings_menu():
    print("\nMenú de Ajustes:")
    print("1. Configurar pausa fija entre acciones")
    print("2. Configurar bot de Telegram para enviar capturas de pantalla")
    print("3. Volver al menú principal")


def show_sequence_editor_menu():
    print("\nMenú de Edición de Secuencia:")
    print("1. Ver acciones actuales")
    print("2. Modificar orden de las acciones")
    print("3. Modificar una acción")
    print("4. Eliminar una acción")
    print("5. Regresar al Menú Principal")


def main_menu():
    try:
        while True:
            clear_terminal()
            position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_SMALL_HEIGHT])
            show_main_menu()

            option = input("Selecciona una opción: ")
            if option == '1':
                record_new_sequence()  # Crear o añadir a una secuencia existente
            elif option == '2':
                additional_settings_menu()  # Configurar parámetros adicionales
            elif option == '3':
                sequence_editor_menu()  # Editar secuencia actual (modificar, mover, eliminar acciones)
            elif option == '4':
                save_sequence()  # Guardar secuencia en un archivo
            elif option == '5':
                select_sequence_file()  # Cargar secuencia desde un archivo
            elif option == '6':
                start_sequence()  # Iniciar ejecución de la secuencia
            elif option == '7':
                reset_sequence()  # Eliminar secuencia actual
            elif option == '8':
                print("Cerrando la aplicación. :)")
                break
            else:
                print("Opción no válida. Por favor, utilice una de las opciones disponibles.")
    except KeyboardInterrupt:
        print("\nFinalizando la ejecución del programa. :)")


def record_new_sequence():
    global actions

    try:
        while True:
            new_action = select_and_configure_action()

            if new_action is not None:
                actions.append(new_action)
            else:
                print("Saliendo del generador de secuencias...")
                break
    except KeyboardInterrupt:
        print("\nFinalizando la edición de la secuencia de manera segura.")


def select_and_configure_action():
    clear_terminal()
    show_sequence_menu()

    while True:
        option = input("Selecciona una opción: ")
        
        if option in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            mapping = {
                '1': add_left_click,
                '2': add_double_click,
                '3': add_right_click,
                '4': add_pause,
                '5': add_simple_keyboard_input,
                '6': add_compound_keyboard_input,
                '7': add_text,
                '8': add_autoincremental_number,
                '9': generate_text_with_datetime,
                '10': add_command_action,
                '11': add_screenshot_action,
                '12': lambda: None
            }
            action_func = mapping.get(option)
            return action_func() if action_func else None
        else:
            print("Opción no válida. Intente de nuevo.")


def additional_settings_menu():
    global settings

    try:
        while True:
            clear_terminal()
            position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_SMALL_HEIGHT])
            show_additional_settings_menu()
            
            option = input("Selecciona una opción: ")
            if option == '1':
                configure_fixed_pause(settings)
            elif option == '2':
                configure_telegram_bot()
            elif option.upper() == '3':
                break
            else:
                input("Opción no válida. Por favor, intenta de nuevo.")
    except KeyboardInterrupt:
        print("\nFinalizando la ejecución del submenú. :)")


def sequence_editor_menu():
    while True:
        clear_terminal()
        show_sequence_editor_menu()

        option = input("Selecciona una opción: ")
        if option == '1':
            view_actions()
        elif option == '2':
            modify_actions_order()
        elif option == '3':
            modify_action()
        elif option == '4':
            delete_action()
        elif option == '5':
            break
        else:
            print("Opción no válida. Por favor, utilice una de las opciones disponibles.")
            input("Presiona <Intro> para continuar...")

