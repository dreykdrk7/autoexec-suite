from pynput.mouse import Listener as MouseListener
import threading

acciones = []

def on_click(x, y, button, pressed):
    if pressed:
        global acciones
        acciones.append(('click', x, y))
        print(f"Click añadido en ({x}, {y})")
        # Detener el listener después de capturar el primer click
        return False  # Esto detiene el listener

def esperar_click_y_añadir():
    with MouseListener(on_click=on_click) as listener:
        listener.join()

def añadir_click():
    print("Haz click en cualquier lugar para capturar las coordenadas... ")
    # Iniciar el listener en un hilo separado para evitar bloquear el script
    thread = threading.Thread(target=esperar_click_y_añadir)
    thread.start()
    thread.join()  # Espera a que el hilo termine


print("Presiona Ctrl-C para terminar")

try:
    while True:
        añadir_click()
except KeyboardInterrupt:
    print("\nListo.")
