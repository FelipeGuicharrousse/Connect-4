import socket

connect4_ip = 'localhost'  # IP Servidor connect4
connect4_port = 8001  # Puerto Servidor connect4 

intermediario_ip = 'localhost'  # IP cliente
intermediario_tcp_port = 8000  # Puerto Cliente

# Socket UDP para Servidor connect4
udp_connect4_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Socket TCP para Cliente
tcp_cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_cliente_socket.bind((intermediario_ip, intermediario_tcp_port))
tcp_cliente_socket.listen(1)

print(f"Servidor intermediario esperando conexiones en {intermediario_ip}:{intermediario_tcp_port}...")

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
