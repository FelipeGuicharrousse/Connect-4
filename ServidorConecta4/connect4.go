package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    // Dirección IP y puerto para escuchar en UDP
    udpAddress := "localhost:8001" // Cambia esto al puerto y la IP deseada

    // Crear una conexión UDP
    udpConn, err := net.ListenPacket("udp", udpAddress)
    if err != nil {
        fmt.Println("Error al crear la conexión UDP:", err)
        os.Exit(1)
    }
    defer udpConn.Close()

    fmt.Println("Servidor `connect4` esperando conexiones UDP en", udpAddress)

    for {
        // Recibir datos del servidor intermediario (UDP)
        buffer := make([]byte, 1024)
        n, addr, err := udpConn.ReadFrom(buffer)
        if err != nil {
            fmt.Println("Error al recibir datos UDP:", err)
            continue
        }

        mensaje := string(buffer[:n])
        fmt.Printf("Datos recibidos de %s: %s\n", addr, mensaje)

        // Procesar los datos (aquí puedes implementar la lógica del juego Connect4)

        // Enviar una respuesta al servidor intermediario (UDP)
        respuesta := "Respuesta desde `connect4`"
        _, err = udpConn.WriteTo([]byte(respuesta), addr)
        if err != nil {
            fmt.Println("Error al enviar respuesta UDP:", err)
        }
    }
}
