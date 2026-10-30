# statistics calcula el promedio; time mide los intervalos[cite: 10]
import socket
import statistics
import time

host = input("Host: ").strip()
puerto = int(input("Puerto (ej. 443): "))
# Cantidad de pruebas a realizar[cite: 10]
intentos = 5
# Aqui se guardan los tiempos de las conexiones exitosas[cite: 10]
tiempos = []
perdidos = 0

# En cada intento se mide cuánto tarda en establecerse la conexión TCP[cite: 10]
for i in range(intentos):
    inicio = time.perf_counter()
    try:
        # create_connection resuelve el nombre y conecta; si falla lanza OSError[cite: 10]
        with socket.create_connection((host, puerto), timeout=2):
            ms = (time.perf_counter() - inicio) * 1000
            tiempos.append(ms)
            print("Intento {}: {:.1f} ms".format(i + 1, ms))
    # Sin respuesta o conexión rechazada: se cuenta como intento perdido[cite: 10]
    except OSError:
        perdidos += 1
        print("Intento {}: sin respuesta".format(i + 1))
    # Pausa corta entre intentos[cite: 10]
    time.sleep(0.5)

# Si todos los intentos fallaron no hay tiempos para calcular[cite: 10]
if tiempos:
    print("Min {:.1f} ms Máx {:.1f} ms Prom {:.1f} ms".format(
        min(tiempos), max(tiempos), statistics.mean(tiempos)))
# Porcentaje de intentos sin respuesta[cite: 10]
print("Pérdida: {:.0f}%".format(perdidos / intentos * 100))