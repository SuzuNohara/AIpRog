import java.io.*;
import java.net.Socket;
import java.nio.ByteBuffer;

public class Cliente {
    public static void main(String[] args) {
        String servidor = "localhost";
        int puerto = args[0].equals("-p") ? Integer.parseInt(args[1]) : 8080;

        try (Socket conexion = new Socket(servidor, puerto);
             DataOutputStream salida = new DataOutputStream(conexion.getOutputStream());
             DataInputStream entrada = new DataInputStream(conexion.getInputStream())) {

            System.out.println("Conectado al servidor " + servidor + " en el puerto " + puerto);

            // Enviar un entero de 32 bits
            salida.writeInt(123);
            System.out.println("Entero enviado: 123");

            // Enviar un numero flotante de 64 bits
            salida.writeDouble(1234567890.1234567890);
            System.out.println("Double enviado: 1234567890.1234567890");

            // Enviar una cadena de caracteres "hola"
            salida.write("hola".getBytes());
            System.out.println("Cadena enviada: hola");

            // Recibir una cadena de 4 bytes del servidor
            byte[] buffer = new byte[4];
            entrada.readFully(buffer, 0, 4);
            System.out.println("Cadena recibida: " + new String(buffer, "UTF-8"));

            // Enviar un conjunto de numeros punto flotante usando ByteBuffer
            ByteBuffer b = ByteBuffer.allocate(5 * 8); // 5 numeros de 64 bits (8 bytes cada uno)
            b.putDouble(1.1);
            b.putDouble(1.2);
            b.putDouble(1.3);
            b.putDouble(1.4);
            b.putDouble(1.5);

            byte[] datos = b.array();
            salida.write(datos);
            System.out.println("Paquete de numeros enviado");

            // Esperar antes de cerrar la conexion
            Thread.sleep(1000);
            System.out.println("Conexion cerrada");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}