from components.terminal_controller import clear_terminal, position_terminal
from components.action_recorder import add_click_auto, add_left_click, add_double_click, add_right_click, add_pause, add_simple_keyboard_input, add_compound_keyboard_input, add_text, add_autoincremental_number, generate_text_with_datetime
from components.extra_settings import configure_fixed_pause, configure_telegram_bot
from components.manager import save_sequence, select_sequence_file, start_sequence
from components.doings.system_actions import add_command_action
from components.config import *


def show_main_menu():
    print("\nMenú Principal:")
    print("1. Crear nueva configuración de secuencia")
    print("2. Configurar parámetros adicionales")
    print("3. Guardar secuencia actual")
    print("4. Cargar secuencia desde archivo")
    print("5. Iniciar ejecución")
    print("6. Salir")


def show_sequence_menu():
    print("\nMenú de Generación de Secuencia:")
    print("1. Añadir click automático (no sirve sobre cuadros de texto)")
    print("2. Añadir click izquierdo (sirve para cualquier pixel visible)")
    print("3. Añadir doble click")
    print("4. Añadir click derecho")
    print("5. Añadir pausa")
    print("6. Añadir entrada de teclado (tecla simple)")
    print("7. Añadir combinación de teclas (personalizable)")
    print("8. Añadir texto")
    print("9. Añadir número autoincremental (solo 1 por secuencia)")
    print("10. Añadir texto estático con fecha y hora (útil para nombres de archivo)")
    print("11. (CMD) Ejecutar comando desde la terminal")
    print("12. Detener generador de secuencia")


def show_additional_settings_menu():
    print("\nMenú de Ajustes:")
    print("1. Configurar pausa fija entre acciones")
    print("2. Configurar bot de Telegram para enviar capturas de pantalla")
    print("X. Volver al menú principal")


def main():
    try:
        while True:
            # clear_terminal()
            position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_SMALL_HEIGHT])
            show_main_menu()

            option = input("Selecciona una opción: ")
            if option == '1':
                record_new_sequence()
            elif option == '2':
                additional_settings_menu()
            elif option == '3':
                save_sequence()
            elif option == '4':
                select_sequence_file()
            elif option == '5':
                start_sequence()
            elif option == '6':
                print("Cerrando la aplicación. :)")
                break
            else:
                input("Opción no válida. Por favor, utilice una de las opciones disponibles.")
    except KeyboardInterrupt:
        print("\nFinalizando la ejecución del programa. :)")


def record_new_sequence():
    global actions

    try:
        while True:
            clear_terminal()
            position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_MEDIUM_HEIGHT])
            show_sequence_menu()

            option = input("Selecciona una opción: ").lower()
            if option == '1':
                add_click_auto(actions)
            elif option == '2':
                add_left_click(actions)
            elif option == '3':
                add_double_click(actions)
            elif option == '4':
                add_right_click(actions)
            elif option == '5':
                add_pause(actions)
            elif option == '6':
                add_simple_keyboard_input(actions)
            elif option == '7':
                add_compound_keyboard_input(actions)
            elif option == '8':
                add_text(actions)
            elif option == '9':
                add_autoincremental_number(actions)
            elif option == '10':
                generate_text_with_datetime(actions)
            elif option == '11' or option == 'cmd':
                add_command_action(actions)
            elif option == '12':
                break
            else:
                input("Opción no válida. Intente de nuevo.")
    except KeyboardInterrupt:
        print("\nFinalizando la ejecución del programa. :)")


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
            elif option.upper() == 'X':
                break
            else:
                input("Opción no válida. Por favor, intenta de nuevo.")
    except KeyboardInterrupt:
        print("\nFinalizando la ejecución del programa. :)")

