/*calculadora usando el ciclo WHILE, IF y SWITCH*/
using System;
class HelloWorld {
  static void Main() {
    bool continuar = true;

        while (continuar)
        {
            Console.WriteLine("Seleccione una operación:");
            Console.WriteLine("1. Suma");
            Console.WriteLine("2. Resta");
            Console.WriteLine("3. Multiplicación");
            Console.WriteLine("4. División");
            Console.WriteLine("5. Salir");

            int opcion = int.Parse(Console.ReadLine());

            if (opcion == 5)
            {
                continuar = false;
                break;
            }

            Console.WriteLine("Ingrese el primer número:");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Ingrese el segundo número:");
            double num2 = Convert.ToDouble(Console.ReadLine());

            double resultado = 0;

            switch (opcion)
            {
                case 1:
                    resultado = num1 + num2;
                    Console.WriteLine($"Resultado: {num1} + {num2} = {resultado}");
                    break;
                case 2:
                    resultado = num1 - num2;
                    Console.WriteLine($"Resultado: {num1} - {num2} = {resultado}");
                    break;
                case 3:
                    resultado = num1 * num2;
                    Console.WriteLine($"Resultado: {num1} * {num2} = {resultado}");
                    break;
                case 4:
                    if (num2 != 0)
                    {
                        resultado = num1 / num2;
                        Console.WriteLine($"Resultado: {num1} / {num2} = {resultado}");
                    }
                    else
                    {
                        Console.WriteLine("Error: División por cero no permitida.");
                    }
                    break;
                default:
                    Console.WriteLine("Opción no válida. Intente de nuevo.");
                    break;
            }

            Console.WriteLine();
        }

        Console.WriteLine("Gracias por usar la calculadora. ¡Hasta luego!");
  }
}
