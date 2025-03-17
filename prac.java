/*Calculadora*/
import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduce el primer número:");
        double num1 = scanner.nextDouble();

        System.out.println("Introduce el segundo número:");
        double num2 = scanner.nextDouble();

        System.out.println("Elige una operación: suma (+), resta (-), multiplicación (*), división (/):");
        char operacion = scanner.next().charAt(0);

        double resultado;

        switch (operacion) {
            case '+':
                resultado = num1 + num2;
                System.out.println("El resultado de la suma es: " + resultado);
                break;
            case '-':
                resultado = num1 - num2;
                System.out.println("El resultado de la resta es: " + resultado);
                break;
            case '*':
                resultado = num1 * num2;
                System.out.println("El resultado de la multiplicación es: " + resultado);
                break;
            case '/':
                if (num2 != 0) {
                    resultado = num1 / num2;
                    System.out.println("El resultado de la división es: " + resultado);
                } else {
                    System.out.println("Error: División por cero no permitida.");
                }
                break;
            default:
                System.out.println("Operación no válida.");
                break;
        }

        scanner.close();
    }
}
/*Calculadora*/
import java.util.Scanner;

public class Calculadora {
	    public static void main(String[] args) {
		            Scanner scanner = new Scanner(System.in);

			            System.out.println("Introduce el primer número:");
				            double num1 = scanner.nextDouble();

					            System.out.println("Introduce el segundo número:");
						            double num2 = scanner.nextDouble();

							            System.out.println("Elige una operación: suma (+), resta (-), multiplicación (*), división (/):");
								            char operacion = scanner.next().charAt(0);

									            double resultado;

										            switch (operacion) {
												                case '+':
															                resultado = num1 + num2;
																	                System.out.println("El resultado de la suma es: " + resultado);
																			                break;
																					            case '-':
																					                resultado = num1 - num2;
																							                System.out.println("El resultado de la resta es: " + resultado);
																									                break;
																											            case '*':
																											                resultado = num1 * num2;
																													                System.out.println("El resultado de la multiplicación es: " + resultado);
																															                break;
																																	            case '/':
																																	                if (num2 != 0) {
																																				                    resultado = num1 / num2;
																																						                        System.out.println("El resultado de la división es: " + resultado);
																																									                } else {
																																												                    System.out.println("Error: División por cero no permitida.");
																																														                    }
																																			                break;
																																					            default:
																																					                System.out.println("Operación no válida.");
																																							                break;
																																									        }

											            scanner.close();
												        }
}
/*Calculadora*/
import java.util.Scanner;

public class Calculadora {
	    public static void main(String[] args) {
		            Scanner scanner = new Scanner(System.in);

			            System.out.println("Introduce el primer número:");
				            double num1 = scanner.nextDouble();

					            System.out.println("Introduce el segundo número:");
						            double num2 = scanner.nextDouble();

							            System.out.println("Elige una operación: suma (+), resta (-), multiplicación (*), división (/):");
								            char operacion = scanner.next().charAt(0);

									            double resultado;

										            switch (operacion) {
												                case '+':
															                resultado = num1 + num2;
																	                System.out.println("El resultado de la suma es: " + resultado);
																			                break;
																					            case '-':
																					                resultado = num1 - num2;
																							                System.out.println("El resultado de la resta es: " + resultado);
																									                break;
																											            case '*':
																											                resultado = num1 * num2;
																													                System.out.println("El resultado de la multiplicación es: " + resultado);
																															                break;
																																	            case '/':
																																	                if (num2 != 0) {
																																				                    resultado = num1 / num2;
																																						                        System.out.println("El resultado de la división es: " + resultado);
																																									                } else {
																																												                    System.out.println("Error: División por cero no permitida.");
																																														                    }
																																			                break;
																																					            default:
																																					                System.out.println("Operación no válida.");
																																							                break;
																																									        }

											            scanner.close();
												        }
}
/*Calculadora*/
import java.util.Scanner;

public class Calculadora {
	    public static void main(String[] args) {
		            Scanner scanner = new Scanner(System.in);

			            System.out.println("Introduce el primer número:");
				            double num1 = scanner.nextDouble();

					            System.out.println("Introduce el segundo número:");
						            double num2 = scanner.nextDouble();

							            System.out.println("Elige una operación: suma (+), resta (-), multiplicación (*), división (/):");
								            char operacion = scanner.next().charAt(0);

									            double resultado;

										            switch (operacion) {
												                case '+':
															                resultado = num1 + num2;
																	                System.out.println("El resultado de la suma es: " + resultado);
																			                break;
																					            case '-':
																					                resultado = num1 - num2;
																							                System.out.println("El resultado de la resta es: " + resultado);
																									                break;
																											            case '*':
																											                resultado = num1 * num2;
																													                System.out.println("El resultado de la multiplicación es: " + resultado);
																															                break;
																																	            case '/':
																																	                if (num2 != 0) {
																																				                    resultado = num1 / num2;
																																						                        System.out.println("El resultado de la división es: " + resultado);
																																									                } else {
																																												                    System.out.println("Error: División por cero no permitida.");
																																														                    }
																																			                break;
																																					            default:
																																					                System.out.println("Operación no válida.");
																																							                break;
																																									        }

											            scanner.close();
												        }
}

