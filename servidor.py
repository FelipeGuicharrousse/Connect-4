import socket

# Dirección IP y puerto del servidor
server_ip = 'localhost'  # Cambia esto a la IP de tu servidor
server_port = 8000  # Cambia esto al puerto que desees

# Crear un socket TCP/IP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección y puerto del servidor
servidor_socket.bind((server_ip, server_port))

# Escuchar conexiones entrantes (máximo 1 cliente en cola)
servidor_socket.listen(1)

print(f"Esperando una conexión en {server_ip}:{server_port}...")

# Aceptar una conexión entrante
cliente_socket, cliente_addr = servidor_socket.accept()
print(f"Conexión establecida desde {cliente_addr[0]}:{cliente_addr[1]}")

# Recibir datos del cliente
datos = cliente_socket.recv(1024)
print(f"Mensaje recibido del cliente: {datos.decode()}")

# Responder al cliente
respuesta = "Mensaje recibido correctamente"
cliente_socket.sendall(respuesta.encode())

# Cerrar la conexión con el cliente
cliente_socket.close()
