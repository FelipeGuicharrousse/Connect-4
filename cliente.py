import socket

# Dirección IP y puerto del servidor
server_ip = 'localhost'  # Cambia esto a la IP de tu servidor
server_port = 8000  # Cambia esto al puerto que desees

# Mensaje a enviar al servidor
mensaje = "Hola, servidor!"

# Crear un socket TCP/IP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
cliente_socket.connect((server_ip, server_port))

# Enviar datos al servidor
cliente_socket.sendall(mensaje.encode())

# Esperar una respuesta del servidor
respuesta = cliente_socket.recv(1024)

print(f"Respuesta del servidor: {respuesta.decode()}")

# Cerrar la conexión
cliente_socket.close()
