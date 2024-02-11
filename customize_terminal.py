import subprocess

titulo = "Auto Navigator"
ancho = 1000  # Ancho deseado de la terminal
alto = 500   # Alto deseado de la terminal

# Establecer el título de la terminal
print(f"\033]0;{titulo}\007", end='', flush=True)

def ajustar_tamaño_terminal(ancho, alto):
    try:
        # Obtén el ID de la ventana activa
        window_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode('utf-8').strip()
        # Ajusta el tamaño
        subprocess.run(["xdotool", "windowsize", window_id, str(ancho), str(alto)])
    except subprocess.CalledProcessError as e:
        print("No se pudo ajustar el tamaño de la ventana de la terminal")

# Ajustar el tamaño de la terminal
ajustar_tamaño_terminal(ancho, alto)
