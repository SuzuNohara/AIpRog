import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.ServerSocket;

class Proxy
{


  static String host_remoto_1, host_remoto_2;
  static int puerto_remoto_1, puerto_remoto_2;
  static int puerto_local;
  static class Worker_1 extends Thread
  {
    Socket cliente_1,cliente_2,cliente_3;
    Worker_1(Socket cliente_1)
    {
      this.cliente_1 = cliente_1;
    }
    public void run()
    {
      try
      {
        // se conecta al host remoto
        cliente_2 = new Socket(host_remoto_1,puerto_remoto_1);
        cliente_3 = new Socket(host_remoto_2,puerto_remoto_2);
        // thread que dirige el tráfico del host remoto al cliente
        new Worker_2(cliente_1,cliente_2,cliente_3).start();
        InputStream entrada_1 = cliente_1.getInputStream();
        OutputStream salida_2 = cliente_2.getOutputStream();
        OutputStream salida_3 = cliente_3.getOutputStream();
        byte[] buffer = new byte[1024];
        int n;
        while((n = entrada_1.read(buffer)) != -1)
        {
          salida_2.write(buffer,0,n);
          salida_2.flush();
        }
      }
      catch (IOException e)
      {
      }
      finally
      {
        try
        {
          if (cliente_1 != null) cliente_1.close();
          if (cliente_2 != null) cliente_2.close();
          if (cliente_3 != null) cliente_3.close();
        }
        catch (IOException e2)
        {
          e2.printStackTrace();
        }
      }
    }
  }


  static class Worker_2 extends Thread
  {
    Socket cliente_1,cliente_2, cliente_3;
    Worker_2(Socket cliente_1,Socket cliente_2, Socket cliente_3)
    {
      this.cliente_1 = cliente_1;
      this.cliente_2 = cliente_2;
      this.cliente_3 = cliente_3;
    }
    public void run()
    {
      try
      {
        InputStream entrada_2 = cliente_2.getInputStream();
        OutputStream salida_1 = cliente_1.getOutputStream();
        byte[] buffer = new byte[4096];
        int n;
        while((n = entrada_2.read(buffer)) != -1)
        {
          salida_1.write(buffer,0,n);
          salida_1.flush();
        }
      }
      catch (IOException e)
      {
      }
      finally
      {
        try
        {
          if (cliente_1 != null) cliente_1.close();
          if (cliente_2 != null) cliente_2.close();
          if (cliente_3 != null) cliente_3.close();
        }
        catch (IOException e2)
        {
          e2.printStackTrace();
        }
      }
    }
  }

  public static void main(String[] args) throws Exception
  {
    if (args.length != 5)
    { 
      System.err.println("Uso:\njava Proxy <host-remoto-1> <puerto-remoto-1> <host-remoto-2> <puerto-remoto-2> <puerto-local>");
      System.exit(1);
    }
    host_remoto_1 = args[0];
    puerto_remoto_1 = Integer.parseInt(args[1]);
    host_remoto_2 = args[2];
    puerto_remoto_2 = Integer.parseInt(args[3]);
    puerto_local = Integer.parseInt(args[4]);
    System.out.println("host_remoto_1: " + host_remoto_1 + ", puerto_remoto_1: " + puerto_remoto_1 + ", host_remoto_2: "+ host_remoto_2+", puerto_remoto_2: "+puerto_remoto_2 +", puerto_local: " + puerto_local);
    ServerSocket ss = new ServerSocket(puerto_local);
    for(;;)
    {
      // espera una conexión del cliente
      Socket cliente_1 = ss.accept();

      // thread que dirige el tráfico del cliente al host remoto
      new Worker_1(cliente_1).start();
    }
  }
}