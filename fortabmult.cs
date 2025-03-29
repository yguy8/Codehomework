//Dos for que muestran las tablas de múltiplicar del 1 al 20 


using System;

class Program
{
	static void Main()
	{
		for (int i = 1; i <= 20; i++)
		{
			Console.WriteLine($"Tabla de multiplicar del {i}:");
			for (int j = 1; j <= 10; j++)
			{
				Console.WriteLine($"{i} x {j} = {i * j}");
			}
			Console.WriteLine(); // LC-nea en blanco para separar las tablas
		}
	}
}



/***********************************************************************************************************************************************************************


/*En este caso lo que hace es pedir especificaciónes al usuario desde donde quiere que empiece todo 
 * el inició de la múltiplicación y desde que tabla y el fin de la múltiplicación y de la tabla
 * haciendolo más interactivo un ejemplo por si no fue claro 
 *
 * las primeras dos opiciones del primer FOR son para decir desde que tabla hasta que tabla quieres desde la del 1-10 entonces imprime la del 1,2,3,4...10
 * las otras dos del segundo FOR para decir desde donde empieza a múltiplicar y hasta donde la tabla del 1 hasta el 12 seria 1X1 1X2....1X12 espero y quede claro*/
/* Algo del For pero mejor*/

using System;

class Program
{
	static void Main()
	{
	    //interación con el usuario
	    Console.WriteLine("Hola bienvenido a las tablas de múltiplicar deja te explico como se ingresan los números");
	    Console.WriteLine("Ingresas cuatro números, el primero establece donde empiezan tus tablas");
	    Console.WriteLine("y el segundo donde acaban; ej 1- 10 te muestra las tablas del 1,2,3,4...10");
	    Console.WriteLine("el tercero, te dice si las quieres empezar múltiplicando desde que número a los demás números ej; 2 x 3 eligues el 2");
	    Console.WriteLine("y por último si quieres múltiplicalos hasta que númer ej; 1 x 19 el 19 es el que eliges");
	    

	    Console.WriteLine("Ahora comenzamos :)");
	    
	    //el rango de las tablas si es de la del 7 hasta la de 10 
	    Console.WriteLine("Ingresa un primer número (recuerda que es donde inicia)");
	    int num1 = int.Parse(Console.ReadLine());
	    Console.WriteLine("Ingresa el segundo recuerda que es donde termina");
	    int num2 = int.Parse(Console.ReadLine());
	    Console.WriteLine("Ingresa el tercer número (recuerda que es donde inicia)");
	    int num3 = int.Parse(Console.ReadLine());
	    Console.WriteLine("Ahora ingresa el último número recuerda que es donde termina");
	    int num4 = int.Parse(Console.ReadLine());
	    
		for (int i = num1; i <= num2; i++)
		{
			Console.WriteLine($"Tabla de multiplicar del {i}:");
			for (int j = num3; j <= num4; j++)
			{
				Console.WriteLine($"{i} x {j} = {i * j}");
			}
			Console.WriteLine(); // separa las tablas
		}
	}
}
******************************************************************************************************************************************************************/
