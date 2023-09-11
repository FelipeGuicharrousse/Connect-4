import random
from colorama import init, Fore, Style

init()

ESPACIO_VACIO = " "
COLOR_1 = "x"
COLOR_2 = "o"
JUGADOR_1 = 1
# La CPU también es el jugador 2
JUGADOR_2 = 2
CONECTA = 4
ESTA_JUGANDO_CPU = False


def solicitar_entero_valido(mensaje):
    """
    Solicita un número entero y lo sigue solicitando
    mientras no sea un entero válido
    """
    while True:
        try:
            posible_entero = int(input(mensaje))
            return posible_entero
        except ValueError:
            continue


def crear_tablero(filas, columnas):
    tablero = []
    for fila in range(filas):
        tablero.append([])
        for columna in range(columnas):
            tablero[fila].append(ESPACIO_VACIO)
    return tablero


def imprimir_tablero(tablero):
    # Imprime números de columnas
    print("|", end="")
    for f in range(1, len(tablero[0]) + 1):
        print(f, end="|")
    print("")
    # Datos
    for fila in tablero:
        print("|", end="")
        for valor in fila:
            color_terminal = Fore.GREEN
            if valor == COLOR_2:
                color_terminal = Fore.RED
            print(color_terminal + valor, end="")
            print(Style.RESET_ALL, end="")
            print("|", end="")
        print("")
    # Pie
    print("+", end="")
    for f in range(1, len(tablero[0]) + 1):
        print("-", end="+")
    print("")


def obtener_fila_valida_en_columna(columna, tablero):
    indice = len(tablero) - 1
    while indice >= 0:
        if tablero[indice][columna] == ESPACIO_VACIO:
            return indice
        indice -= 1
    return -1


def solicitar_columna(tablero):
    """
    Solicita la columna y devuelve la columna ingresada -1 para ser usada fácilmente como índice
    """
    while True:
        columna = solicitar_entero_valido("Ingresa la columna para colocar la pieza: ")
        if columna <= 0 or columna > len(tablero[0]):
            print("Columna no válida")
        elif tablero[0][columna - 1] != ESPACIO_VACIO:
            print("Esa columna ya está llena")
        else:
            return columna - 1


def colocar_pieza(columna, jugador, tablero):
    """
    Coloca una pieza en el tablero. La columna debe
    comenzar en 0
    """
    color = COLOR_1
    if jugador == JUGADOR_2:
        color = COLOR_2
    fila = obtener_fila_valida_en_columna(columna, tablero)
    if fila == -1:
        return False
    tablero[fila][columna] = color
    return True


def obtener_conteo_derecha(fila, columna, color, tablero):
    fin_columnas = len(tablero[0])
    contador = 0
    for i in range(columna, fin_columnas):
        if contador >= CONECTA:
            return contador
        if tablero[fila][i] == color:
            contador += 1
        else:
            contador = 0
    return contador


def obtener_conteo_izquierda(fila, columna, color, tablero):
    contador = 0
    # -1 porque no es inclusivo
    for i in range(columna, -1, -1):
        if contador >= CONECTA:
            return contador
        if tablero[fila][i] == color:
            contador += 1
        else:
            contador = 0

    return contador


def obtener_conteo_abajo(fila, columna, color, tablero):
    fin_filas = len(tablero)
    contador = 0
    for i in range(fila, fin_filas):
        if contador >= CONECTA:
            return contador
        if tablero[i][columna] == color:
            contador += 1
        else:
            contador = 0
    return contador


def obtener_conteo_arriba(fila, columna, color, tablero):
    contador = 0
    for i in range(fila, -1, -1):
        if contador >= CONECTA:
            return contador
        if contador >= CONECTA:
            return contador
        if tablero[i][columna] == color:
            contador += 1
        else:
            contador = 0
    return contador


def obtener_conteo_arriba_derecha(fila, columna, color, tablero):
    contador = 0
    numero_fila = fila
    numero_columna = columna
    while numero_fila >= 0 and numero_columna < len(tablero[0]):
        if contador >= CONECTA:
            return contador
        if tablero[numero_fila][numero_columna] == color:
            contador += 1
        else:
            contador = 0
        numero_fila -= 1
        numero_columna += 1
    return contador


def obtener_conteo_arriba_izquierda(fila, columna, color, tablero):
    contador = 0
    numero_fila = fila
    numero_columna = columna
    while numero_fila >= 0 and numero_columna >= 0:
        if contador >= CONECTA:
            return contador
        if tablero[numero_fila][numero_columna] == color:
            contador += 1
        else:
            contador = 0
        numero_fila -= 1
        numero_columna -= 1
    return contador


def obtener_conteo_abajo_izquierda(fila, columna, color, tablero):
    contador = 0
    numero_fila = fila
    numero_columna = columna
    while numero_fila < len(tablero) and numero_columna >= 0:
        if contador >= CONECTA:
            return contador
        if tablero[numero_fila][numero_columna] == color:
            contador += 1
        else:
            contador = 0
        numero_fila += 1
        numero_columna -= 1
    return contador


def obtener_conteo_abajo_derecha(fila, columna, color, tablero):
    contador = 0
    numero_fila = fila
    numero_columna = columna
    while numero_fila < len(tablero) and numero_columna < len(tablero[0]):
        if contador >= CONECTA:
            return contador
        if tablero[numero_fila][numero_columna] == color:
            contador += 1
        else:
            contador = 0
        numero_fila += 1
        numero_columna += 1
    return contador


def obtener_direcciones():
    return [
        'izquierda',
        'arriba',
        'abajo',
        'derecha',
        'arriba_derecha',
        'abajo_derecha',
        'arriba_izquierda',
        'abajo_izquierda',
    ]


def obtener_conteo(fila, columna, color, tablero):
    direcciones = obtener_direcciones()
    for direccion in direcciones:
        funcion = globals()['obtener_conteo_' + direccion]
        conteo = funcion(fila, columna, color, tablero)
        if conteo >= CONECTA:
            return conteo
    return 0


def obtener_color_de_jugador(jugador):
    color = COLOR_1
    if jugador == JUGADOR_2:
        color = COLOR_2
    return color


def comprobar_ganador(jugador, tablero):
    color = obtener_color_de_jugador(jugador)
    for f, fila in enumerate(tablero):
        for c, celda in enumerate(fila):
            conteo = obtener_conteo(f, c, color, tablero)
            if conteo >= CONECTA:
                return True
    return False


def elegir_jugador_al_azar():
    return random.choice([JUGADOR_1, JUGADOR_2])


def imprimir_y_solicitar_turno(turno, tablero):
    if not ESTA_JUGANDO_CPU:
        print(f"Jugador 1: {COLOR_1} | Jugador 2: {COLOR_2}")
    else:
        print(f"Jugador 1: {COLOR_1} | CPU: {COLOR_2}")
    if turno == JUGADOR_1:
        print(f"Turno del jugador 1 ({COLOR_1})")
    else:
        if not ESTA_JUGANDO_CPU:
            print(f"Turno del jugador 2 ({COLOR_2})")
        else:
            print("Turno de la CPU")
    return solicitar_columna(tablero)


def felicitar_jugador(jugador_actual):
    if not ESTA_JUGANDO_CPU:
        if jugador_actual == JUGADOR_1:
            print("Felicidades Jugador 1. Has ganado")
        else:
            print("Felicidades Jugador 2. Has ganado")
    else:
        if jugador_actual == JUGADOR_1:
            print("Felicidades Jugador 1. Has ganado")
        else:
            print("Ha ganado el CPU")


def es_empate(tablero):
    for columna in range(len(tablero[0])):
        if obtener_fila_valida_en_columna(columna, tablero) != -1:
            return False
    return True


def jugador_vs_jugador(tablero):
    jugador_actual = elegir_jugador_al_azar()
    while True:
        imprimir_tablero(tablero)
        columna = imprimir_y_solicitar_turno(jugador_actual, tablero)
        pieza_colocada = colocar_pieza(columna, jugador_actual, tablero)
        if not pieza_colocada:
            print("No se puede colocar en esa columna")
        ha_ganado = comprobar_ganador(jugador_actual, tablero)
        if ha_ganado:
            imprimir_tablero(tablero)
            felicitar_jugador(jugador_actual)
            break
        elif es_empate(tablero):
            imprimir_tablero(tablero)
            indicar_empate()
            break
        else:
            if jugador_actual == JUGADOR_1:
                jugador_actual = JUGADOR_2
            else:
                jugador_actual = JUGADOR_1


def obtener_columna_segun_cpu(jugador, tablero):
    return elegir_columna_ideal(jugador, tablero)


def obtener_jugador_contrario(jugador):
    if jugador == JUGADOR_1:
        return JUGADOR_2
    return JUGADOR_1


def elegir_columna_ideal(jugador, tablerOriginal):
    return random.randint(0,5)


def jugador_vs_computadora(tablero):
    global ESTA_JUGANDO_CPU
    ESTA_JUGANDO_CPU = True
    jugador_actual = elegir_jugador_al_azar()
    while True:
        imprimir_tablero(tablero)
        if jugador_actual == JUGADOR_1:
            columna = imprimir_y_solicitar_turno(jugador_actual, tablero)
        else:
            print("CPU pensando...")
            columna = obtener_columna_segun_cpu(jugador_actual, tablero)
        pieza_colocada = colocar_pieza(columna, jugador_actual, tablero)
        if not pieza_colocada:
            print("No se puede colocar en esa columna")
        ha_ganado = comprobar_ganador(jugador_actual, tablero)
        if ha_ganado:
            imprimir_tablero(tablero)
            felicitar_jugador(jugador_actual)
            break
        elif es_empate(tablero):
            imprimir_tablero(tablero)
            indicar_empate()
            break
        else:
            if jugador_actual == JUGADOR_1:
                jugador_actual = JUGADOR_2
            else:
                jugador_actual = JUGADOR_1
    ESTA_JUGANDO_CPU = False


def volver_a_jugar():
    while True:
        eleccion = input("¿Quieres volver a jugar? [s/n] ").lower()
        if eleccion == "s":
            return True
        elif eleccion == "n":
            return False


def main():
    while True:
        eleccion = input("1- Jugador vs Jugador"
                         "\n"
                         "2- Jugador vs Máquina"
                         "\n"
                         "4- Salir"
                         "\n"
                         "Elige: ")
        if eleccion == "4":
            break

        if eleccion == "1":
            filas, columnas = 6, 6
            while True:
                tablero = crear_tablero(filas, columnas)
                jugador_vs_jugador(tablero)
                if not volver_a_jugar():
                    break
        if eleccion == "2":
            filas, columnas = 6, 6
            while True:
                tablero = crear_tablero(filas, columnas)
                jugador_vs_computadora(tablero)
                if not volver_a_jugar():
                    break

main()