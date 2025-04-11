# -*- coding: utf-8 -*-
nombre = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")
if nombre == "" or contrasena == "":
    print("Por favor, complete todos los campos.")
    exit()
print("Bienevenido", nombre, "a tu app bancaria")
print("-----------Menú Principal-----------")
print("1. Consultar saldo")
print("2. Retirar dinero")
print("3. Depositar dinero")
print("4. Transferir dinero")
print("5. Salir")
opcion = int(input("Seleccione una opción: "))
fondos = 2000
if opcion == 1:
    print("Su saldo es de:", fondos, "USD")
elif opcion == 2:
    retirar = int(input("¿Cuánto dinero desea retirar? "))
    if retirar > fondos:
        print("No tiene suficiente saldo.")
    else:
        fondos -= retirar
        print("Su nuevo saldo es de: ", fondos, "USD")
elif opcion == 3:  
    depositar = int(input("¿Cuánto dinero desea depositar? "))
    fondos += depositar
    print("Su nuevo saldo es de:", fondos, "USD")
elif opcion == 4:
    transferir = int(input("¿Cuánto dinero desea transferir? "))
    if transferir > fondos:
        print("No tiene suficiente saldo.")
    else:
        fondos -= transferir
        print("Su nuevo saldo es de: ", fondos, "USD")
elif opcion == 5:
    print("Gracias por usar la app bancaria.")
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")
    