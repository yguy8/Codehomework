nombre = input("Ingrese su nombre: ")
contrasena = input("Ingrese su contraseña: ")
print("Bienvenido", nombre.capitalize())

print("¿Qué acción desea realizar?")

saldo = 2000
print("1. Mostrar saldo")
print("2. Retirar dinero")
print("3. Salir")

opcion = int(input("Seleccione una opción: "))
while opcion != 3:
    if opcion == 1:
        print("Su saldo es:", saldo)
    elif opcion == 2:
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print("Retiro exitoso. Su nuevo saldo es:", saldo)
    else:
        print("Opción no válida.")
    print("¿Qué acción desea realizar?")
    print("1. Mostrar saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
print("Gracias por usar el sistema. ¡Hasta luego!", nombre.capitalize())
