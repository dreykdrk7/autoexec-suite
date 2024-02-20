from components.menus import select_and_configure_action
from components.terminal_controller import clear_terminal
from components.config import actions


def view_actions():
    clear_terminal()

    if not actions:
        print("No hay acciones definidas.")
    else:
        for i, action in enumerate(actions, start=1):
            print(f"{i}. {action['type']} - {action['args']}")
    input("Presiona <Intro> para continuar...")


def modify_actions_order():
    global actions

    view_actions()
    try:
        action_number = int(input("Número de la acción a mover (índice): ")) - 1
        new_position = int(input("Nueva posición para la acción (índice): ")) - 1

        if 0 <= action_number < len(actions) and 0 <= new_position < len(actions):
            action = actions.pop(action_number)
            actions.insert(new_position, action)
            print("Acción movida correctamente.")
        else:
            print("Número de acción o nueva posición fuera de rango.")
    except ValueError:
        print("Por favor, introduce números válidos.")
    input("Presiona <Intro> para continuar...")


def modify_action():
    global actions

    view_actions()
    try:
        action_number = int(input("Número de la acción a modificar (índice): ")) - 1

        if 0 <= action_number < len(actions):
            new_action = select_and_configure_action()
            if new_action:
                actions[action_number] = new_action
                print("Acción modificada correctamente.")
        else:
            print("Número de acción fuera de rango.")
    except ValueError:
        print("Por favor, introduce un número válido.")
    input("Presiona <Intro> para continuar...")


def delete_action():
    global actions

    view_actions()
    try:
        action_number = int(input("Número de la acción que deseas eliminar (índice): ")) - 1

        if 0 <= action_number < len(actions):
            del actions[action_number]
            print("Acción eliminada correctamente.")
        else:
            print("Número de acción fuera de rango.")
    except ValueError:
        print("Por favor, introduce un número válido.")
    input("Presiona <Intro> para continuar...")

