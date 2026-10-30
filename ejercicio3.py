# platform indica el sistema operativo; subprocess ejecuta comandos del sistema
import platform
import subprocess

# Envía un solo ping y devuelve True si el host respondió
def hacer_ping(host):
    # Windows usa -n (cantidad) y -w (espera en ms); Linux y macOS usan -c y -W (espera en s)
    if platform.system().lower() == "windows":
        comando = ["ping", "-n", "1", "-w", "1000", host]
    else:
        comando = ["ping", "-c", "1", "-W", "1", host]
    # try/except evita que el programa se cierre si ping tarda demasiado o no está instalado
    try:
        # Se ejecuta el comando sin mostrar su salida; timeout=5 corta la espera
        resultado = subprocess.run(comando, stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL, timeout=5)
        # Código de retorno 0 significa que el ping tuvo éxito
        return resultado.returncode == 0
    # Si tardó demasiado o el comando ping no existe, se considera que no responde
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False

# Programa principal
host = input("Host o IP a probar: ").strip()
if hacer_ping(host):
    print(host, "responde")
else:
    print(host, "no responde")