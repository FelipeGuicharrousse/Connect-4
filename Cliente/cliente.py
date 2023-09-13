import socket

server_ip = 'localhost'  # IP Servidor Intermedio
server_port = 8000  # Puerto Servidor Intermedio

# Mensaje a enviar al servidor
# mensaje = "Hola, servidor!"

condition = True

# Socket TCP para Servidor Intermedio
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al Servidor Intermedio
cliente_socket.connect((server_ip, server_port))

mensaje = input("Ingresa un numero: ")
# Enviar datos al servidor
cliente_socket.sendall(mensaje.encode())

# Esperar una respuesta del servidor
respuesta = cliente_socket.recv(1024)

print(f"Respuesta del servidor: \n{respuesta.decode()}")
# Cerrar la conexión
cliente_socket.close()  

while(condition):
    # Recibir el tablero
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((server_ip, server_port))
    respuesta = cliente_socket.recv(1024)
    print(respuesta.decode())
    cliente_socket.close()  

    # Verificar si es el turno del jugador
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((server_ip, server_port))
    turno_jugador = cliente_socket.recv(1024)
    cliente_socket.close() 

    if turno_jugador.decode() == "1":
        # Recibir texto en la pantalla
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((server_ip, server_port))
        mensaje = cliente_socket.recv(1024)
        cliente_socket.close()
        print(mensaje.decode())

        # Enviar jugada del jugador
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((server_ip, server_port))
        mensaje = input("Ingresa la columna para colocar la pieza: ")
        cliente_socket.sendall(mensaje.encode())
        cliente_socket.close()
    
    # Verificar si alguien ganó la partida
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((server_ip, server_port))
    ha_ganado = cliente_socket.recv(1024)
    cliente_socket.close() 

    if ha_ganado.decode() == "1":
        # Recibir el texto de victoria
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((server_ip, server_port))
        mensaje = cliente_socket.recv(1024)
        cliente_socket.close()
        print(mensaje.decode())
        break
    
    # Verificar si se ha empatado la partida
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((server_ip, server_port))
    empate = cliente_socket.recv(1024)
    cliente_socket.close() 

    if empate.decode() == "1":
        # Recibir el texto de empate
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((server_ip, server_port))
        mensaje = cliente_socket.recv(1024)
        cliente_socket.close()
        print(mensaje.decode())
        break
