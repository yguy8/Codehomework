/*Calculadora de área de terrenos*/
using System;
class HelloWorld {
  static void Main() {
     
    Console.WriteLine("Hola, bienvenido");
    Console.WriteLine("Ingrese lo ancho del terreno en metros");
    float ancho = float.Parse(Console.ReadLine());
    Console.WriteLine("Ingrese lo largo del terreno en metros");
    float largo = float.Parse(Console.ReadLine());
    Console.WriteLine("Aquí esta el calculo realizado");
    float area = ancho * largo;
    Console.WriteLine("Su terreno tiene un área de: " + area + " metros cuadrados");
    
  }
}

/*IMC*/
using System;
class HelloWorld {
  static void Main() {
    Console.WriteLine("Hola de nuevo humano ahora calcularemos tu indice de masa corporal");
    Console.WriteLine("Ingrese su peso en kg, ejemplo 70");
    float kg = float.Parse(Console.ReadLine());
    Console.WriteLine("Ahora su estatura en metros, ejemplo 1.67");
    float alt = float.Parse(Console.ReadLine());
    
    float imc = (kg)/(alt*alt);
    Console.WriteLine("Aquí esta su IMC: " + imc);
    Console.WriteLine("Su peso " +  kg + "Su estatura "+ alt);
  }
}

/*teorema de pitágoras*/
using System;
class HelloWorld {
  static void Main() {
    Console.WriteLine("Si amabas a pitágoras ahora lo vas a amar más");
    Console.WriteLine("Si conoces los catetos ingresalos y te dare la hipotenusa");
    Console.WriteLine("Primer cateto: ");
    float c1 = float.Parse(Console.ReadLine());
    Console.WriteLine("Segundo cateto: ");
    float c2 = float.Parse(Console.ReadLine());
    
    float hip = (c1*c1) + (c2*c2);
    double hipO = Math.Sqrt(hip);
    Console.WriteLine("Aquí tienes tu hipotenusa pequeño saltamontes: " + hipO);
  }
}

/*Para la chamba*/
using System;
class HelloWorld {
  static void Main() {
      //Comentarios que este si revuelve
    Console.WriteLine("Calcula tu propina.com");
    Console.WriteLine("Hola, gente chambeadora");
     // el monto total de la cuenta
        Console.Write("Ingrese el monto total de la cuenta: ");
        double totalCuenta = Convert.ToDouble(Console.ReadLine());

        // el porcentaje de propina
        Console.Write("Ingrese el porcentaje de propina (por ejemplo, 15 para 15%): ");
        double porcentajePropina = Convert.ToDouble(Console.ReadLine());

        // Calcular la propina
        double propina = totalCuenta * (porcentajePropina / 100);

        // Calcular el total a pagar
        double totalPagar = totalCuenta + propina;

        // Mostrar los resultados
        Console.WriteLine($"Propina: " + propina);
        Console.WriteLine("Total a pagar: " + totalPagar);
  }
}

/*Convertir Celsius a Fahrenheit y viseversa*/
using System;
class HelloWorld {
  static void Main() {
      //saludo y preguntas
    Console.WriteLine("Hola, humano");
    //Celsius a Fahrenheit
    Console.WriteLine("Si quiere convertir Celsius a Fahrenheit ingrese el número y si no un 00");
    double grad1 = double.Parse(Console.ReadLine());
    double F = (grad1*1.8) + 32;
    if (grad1 == 00 ){
        Console.WriteLine("Ok, pasaremos a la otra conversión, espere un segundo");
    }else{
        Console.WriteLine("Los Celsius en Fahrenheit: " + F );
    }
    //Fahrenheit a Celsius
    Console.WriteLine("Ahora de Fahrenheit a Celsius, ingrese un número y si no ingrese 00");
    double grad2 = double.Parse(Console.ReadLine());
    double C = (grad2 - 32) / 1.8;
    if (grad1 == 00 ){
        Console.WriteLine("Ok, fin del programa ya que no ingreso nada, gracias humano");
    }else{
        Console.WriteLine("De Fahrenheit a Celsius: " + C );
    }
  }

/*Distancia millas y kilometros*/
using System;
class HelloWorld {
  static void Main() {
   //saludo y preguntas
    Console.WriteLine("Hola");
    //Millas
    Console.WriteLine("Si quiere convertir Millas a Kilometros ingrese el número y si no un 00");
    double milla = double.Parse(Console.ReadLine());
    double M = (milla*1.609);
    if (milla == 00 ){
        Console.WriteLine("Ok, pasaremos a la otra conversión, espere un segundo");
    }else{
        Console.WriteLine("millas a kilometros: " + M);
    }
    //Kilometros
    Console.WriteLine("Ahora de Kilometros a millas, ingrese un número y si no ingrese 00");
    double kil = double.Parse(Console.ReadLine());
    double K = (kil*0.621);
    if (kil == 00 ){
        Console.WriteLine("Ok, fin del programa ya que no ingreso nada, gracias humano");
    }else{
        Console.WriteLine("De Kilometros a millas: " + K);
    }
    Console.WriteLine("Gracias y hasta pronto :)");
  }
}

/*Interes $$$$*/
using System;
class HelloWorld {
  static void Main() {
    Console.WriteLine("Calculadora de interés SIMPLE");
     // Solicitar datos al usuario
        Console.Write("Ingrese el capital inicial: ");
        double principal = double.Parse(Console.ReadLine());

        Console.Write("Ingrese la tasa de interés anual en porcentaje: ");
        double rate = double.Parse(Console.ReadLine()) / 100;

        Console.Write("Ingrese el tiempo en años: ");
        int time = int.Parse(Console.ReadLine());

        // Calcular el interés simple
        double interest = principal * rate * time;

        // Mostrar el resultado
        Console.WriteLine("El interés simple es: " + interest );
  }
}

/*Descuento*/
using System;
class HelloWorld {
  static void Main() {
    // Precio original del producto
        decimal precioOriginal = 100.00m;
        
        // Porcentaje de descuento
        decimal porcentajeDescuento = 20.00m;
        
        // Calcular el monto del descuento
        decimal montoDescuento = (precioOriginal * porcentajeDescuento) / 100;
        
        // Calcular el precio final después del descuento
        decimal precioFinal = precioOriginal - montoDescuento;
        
        // Mostrar los resultados
        Console.WriteLine("Precio Original: $" + precioOriginal);
        Console.WriteLine("Porcentaje de Descuento: " + porcentajeDescuento + "%");
        Console.WriteLine("Monto del Descuento: $" + montoDescuento);
        Console.WriteLine("Precio Final: $" + precioFinal);
  }
}
