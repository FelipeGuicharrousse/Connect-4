import socket

server_ip = 'localhost'  # IP Servidor Intermedio
server_port = 8000  # Puerto Servidor Intermedio

# Mensaje a enviar al servidor
mensaje = "Hola, servidor!"

# Socket TCP para Servidor Intermedio
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al Servidor Intermedio
cliente_socket.connect((server_ip, server_port))

# Enviar datos al servidor
cliente_socket.sendall(mensaje.encode())

# Esperar una respuesta del servidor
respuesta = cliente_socket.recv(1024)

print(f"Respuesta del servidor: {respuesta.decode()}")

# Cerrar la conexión
cliente_socket.close()
