import socket

# Dirección IP y puerto del servidor `connect4` en Go
connect4_ip = 'localhost'  # Cambia esto a la IP del servidor `connect4` en Go
connect4_port = 8001  # Cambia esto al puerto del servidor `connect4` en Go

# Dirección IP y puerto del servidor intermediario (TCP para el cliente)
intermediario_ip = 'localhost'  # Cambia esto a la IP de este servidor intermediario
intermediario_tcp_port = 8000  # Cambia esto al puerto TCP para el cliente

# Crear un socket UDP para comunicarse con `connect4` en Go
udp_connect4_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Crear un socket TCP para comunicarse con el cliente
tcp_cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_cliente_socket.bind((intermediario_ip, intermediario_tcp_port))
tcp_cliente_socket.listen(1)

print(f"Servidor intermediario (TCP para el cliente, UDP para `connect4`) esperando conexiones en {intermediario_ip}:{intermediario_tcp_port}...")

while True:
    # Aceptar una conexión TCP con el cliente
    cliente_socket, cliente_addr = tcp_cliente_socket.accept()
    print(f"Conexión establecida con el cliente desde {cliente_addr[0]}:{cliente_addr[1]}")

    # Recibir datos del cliente TCP
    datos_cliente = cliente_socket.recv(1024)
    print(f"Datos recibidos del cliente: {datos_cliente.decode()}")

    # Reenviar los datos al servidor `connect4` utilizando UDP
    udp_connect4_socket.sendto(datos_cliente, (connect4_ip, connect4_port))

    # Recibir la respuesta del servidor `connect4` en Go a través de UDP
    respuesta_connect4, _ = udp_connect4_socket.recvfrom(1024)
    print(f"Respuesta del servidor `connect4`: {respuesta_connect4.decode()}")

    # Enviar la respuesta al cliente TCP
    cliente_socket.sendall(respuesta_connect4)

    # Cerrar la conexión TCP con el cliente
    cliente_socket.close()
