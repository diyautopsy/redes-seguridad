# socket permite trabajar con conexiones de red desde Python
import socket

# Devuelve la IP que usa este equipo para salir a la red
def ip_local():
    # Socket UDP sobre IPv4. UDP no establece conexión, por eso no se envía nada
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # connect en UDP solo le pregunta al sistema por qué interfaz saldría hacia ese destino
        s.connect(("8.8.8.8", 80))
        # getsockname() devuelve (IP local, puerto): nos quedamos con la IP
        return s.getsockname()[0]
    # Sin red disponible se usa la dirección de loopback
    except OSError:
        return "127.0.0.1"
    # El socket se cierra siempre, haya o no error
    finally:
        s.close()

# Nombre del equipo en la red
nombre = socket.gethostname()
print("Equipo:", nombre)
print("IP local:", ip_local())