from components.terminal_controller import clear_terminal


def configure_fixed_pause(settings):
    clear_terminal()

    print(f'''El valor actual para la pausa entre acciones es: {settings['fixed_pause']}
    
    Nota: Esta pausa se ejecutará tras cada acción definida en la secuencia.
    
    Valora no introducir un valor demasiado elevado.
    ''')

    sleep_time = int(input("Establece una pausa fija entre acciones (en segundos): "))
    settings['fixed_pause'] = sleep_time

    print("Pausa modificada correctamente.\n")
    input("Pulsa cualquier tecla para continuar... ")


def configure_telegram_bot():
    pass