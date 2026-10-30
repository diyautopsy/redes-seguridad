# ipaddress maneja direcciones y redes y hace los cálculos de subneteo
import ipaddress

# El usuario escribe la red con su prefijo, por ejemplo 192.168.10.0/26
entrada = input("Red en formato CIDR (ej. 192.168.10.0/26): ")
try:
    # strict=False acepta una IP de host (192.168.10.130/26) y calcula la red a la que pertenece
    red = ipaddress.ip_network(entrada, strict=False)
# ValueError indica que el texto no es una dirección o un prefijo válido
except ValueError:
    print("Dirección no válida")
    raise SystemExit(1)

# Datos que la biblioteca calcula directamente
print("Red:", red.network_address)
print("Máscara:", red.netmask)
print("Prefijo: /" + str(red.prefixlen))
print("Broadcast:", red.broadcast_address)

# Las redes /31 y /32 no tienen hosts útiles para asignar a equipos
if red.num_addresses < 4:
    print("Sin hosts útiles")
else:
    # Hosts útiles = 2^h - 2: se descuentan la dirección de red y el broadcast
    print("Hosts útiles:", red.num_addresses - 2)
    # Primer host = red + 1; último host = broadcast - 1
    print("Primer host:", red.network_address + 1)
    print("Último host:", red.broadcast_address - 1)