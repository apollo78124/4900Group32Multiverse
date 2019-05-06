package org.ea.service;

/**
 * Hello world!
 *
 */
 import java.lang.Exception;

public class App
{
    public static void main( String[] args )
    {
        System.out.println( "1" );
        sleep(400);
        System.out.println( "2 World!" );
        sleep(400);
        System.out.println( "3 World!" );
        sleep(400);
        System.out.println( "4 World!" );
        sleep(400);
        System.out.println( "5 World!" );
        sleep(400);
        System.out.println( "6 World!" );
        sleep(400);
        System.out.println( "7 World!" );
    }

    public static void sleep(int nanos) {
      try  {
         Thread.sleep(nanos);
      }catch (Exception e) {
        e.printStackTrace();
      }
    }
}
