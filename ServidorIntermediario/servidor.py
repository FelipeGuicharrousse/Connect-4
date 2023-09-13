import socket
from juego import *

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

# Comenzar la partida:
filas, columnas = 6, 6
tablero = crear_tablero(filas, columnas)

#================================================================================================================
# Aqui deberiamos iniciar la comunicacion entre los servidores
#

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

respuesta_connect4 = 'hola como estas\n yo bien gracias\n'
print(retornar_tablero(tablero))
# Enviar la respuesta al cliente TCP
cliente_socket.sendall(retornar_tablero(tablero).encode())

# Cerrar la conexión TCP con el cliente
cliente_socket.close()
#================================================================================================================================




#
# El juego esta aqui
#
jugador_actual = JUGADOR_1
while True:
    # Imprimir el tablero:
    cliente_socket, cliente_addr = tcp_cliente_socket.accept()
    print(f"Conexión establecida con el cliente desde {cliente_addr[0]}:{cliente_addr[1]}")
    cliente_socket.sendall(retornar_tablero(tablero).encode())
    cliente_socket.close()
    imprimir_tablero(tablero)

    
    if jugador_actual == JUGADOR_1:
        # Avisar que es el turno del jugador
        cliente_socket, cliente_addr = tcp_cliente_socket.accept()
        print("Avisar que es el turno del jugador")
        mensaje = "1"
        cliente_socket.sendall(mensaje.encode())
        cliente_socket.close()

        # Mandar el texto para que la pantalla del jugador
        mensaje = f"Jugador: {COLOR_1} | CPU: {COLOR_2}\nTurno del jugador ({COLOR_1})"
        cliente_socket, cliente_addr = tcp_cliente_socket.accept()
        print("Mandar el texto para que la pantalla del jugador")
        cliente_socket.sendall(mensaje.encode())
        cliente_socket.close()

        # Recibir jugada del jugador (SOLO JUGADAS VALIDAS)
        # while True:
        cliente_socket, cliente_addr = tcp_cliente_socket.accept()
        columna = cliente_socket.recv(1024)
        print("Recibir jugada del jugador (SOLO JUGADAS VALIDAS)")
        cliente_socket.close()
            # if columna <= 0 or columna > len(tablero[0]):
            #     print("Columna no válida")
            # elif tablero[0][columna - 1] != ESPACIO_VACIO:
            #     print("Esa columna ya está llena")
            # else:
            #     return columna - 1
        columna = int(columna.decode())
        columna -= 1
    else:
        # Avisar que es el turno de cpu
        cliente_socket, cliente_addr = tcp_cliente_socket.accept()
        print("Avisar que es el turno de cpu")
        mensaje = "0"
        cliente_socket.sendall(mensaje.encode())
        cliente_socket.close()

        print("CPU pensando...")
        columna = obtener_columna_segun_cpu()
    pieza_colocada = colocar_pieza(columna, jugador_actual, tablero)
    if not pieza_colocada:
        print("No se puede colocar en esa columna")
    ha_ganado = comprobar_ganador(jugador_actual, tablero)
    empate = es_empate(tablero)
    if ha_ganado:
        # Avisar que alguien gano el juego
        cliente_socket, cliente_addr = tcp_cliente_socket.accept()
        print("Avisar que alguien gano el juego")
        mensaje = "1"
        cliente_socket.sendall(mensaje.encode())
        cliente_socket.close()

        # Mandar el texto de quien ha ganado el juego
        cliente_socket, cliente_addr = tcp_cliente_socket.accept()
        print("Mandar el texto de quien ha ganado el juego")
        mensaje = retornar_tablero(tablero)
        
        if jugador_actual == JUGADOR_1:
            mensaje = mensaje + "Felicidades Jugador. Has ganado"
        else:
            mensaje = mensaje + "Ha ganado el CPU"
        cliente_socket.sendall(mensaje.encode())
        imprimir_tablero(tablero)
        cliente_socket.close()
        break
    elif empate:
        # Avisar que se empato el juego
        cliente_socket, cliente_addr = tcp_cliente_socket.accept()
        print("Avisar que se empato el juego")
        mensaje = "1"
        cliente_socket.sendall(mensaje.encode())
        cliente_socket.close()

        # Mandar el texto de quien ha empatado el juego
        cliente_socket, cliente_addr = tcp_cliente_socket.accept()
        print("Mandar el texto de quien ha empatado el juego")
        cliente_socket.sendall(retornar_tablero(tablero).encode())
        cliente_socket.close()
        imprimir_tablero(tablero)
        print("Empate")
        break
    else:
        if jugador_actual == JUGADOR_1:
            jugador_actual = JUGADOR_2
        else:
            jugador_actual = JUGADOR_1