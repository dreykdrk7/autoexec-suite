import pyautogui
import time

print("Presiona Ctrl-C para terminar")

try:
    while True:
        # Obtén y muestra las coordenadas actuales del cursor del ratón.
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nListo.")
