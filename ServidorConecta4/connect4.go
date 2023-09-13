package main

import (
    "fmt"
    "net"
    "os"
    "math/rand"
    "time"
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
        fmt.Printf("Datos recibidos de %s: \n%s\n", addr, mensaje)


        
        // Generar un número aleatorio entre 0 y 5
        rand.Seed(time.Now().UnixNano())
        numeroAleatorio := rand.Intn(6)
        
        // Convertir el número a string
        respuesta := fmt.Sprintf("%d", numeroAleatorio)
        
        // Enviar la respuesta al servidor intermediario (UDP)
        _, err = udpConn.WriteTo([]byte(respuesta), addr)
        if err != nil {
            fmt.Println("Error al enviar respuesta UDP:", err)
        }

    }
}
