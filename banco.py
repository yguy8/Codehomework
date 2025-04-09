
fondos = 2000  # Inicialización correcta fuera del condicional
nombre = input("Ingrese su nombre: ")
print("Bienvenido", nombre, "a tu app bancaria")
print("-----------Menú Principal-----------")
def menu():
    fondos = fondos  # Declaramos fondos como global
    op1 = print("1: Consultar saldo")
    op2 = print("2: Retirar dinero")
    op3 = print("3: Depositar dinero")
    op4 = print("4: Transferir dinero")
    op5 = print("5: Salir")
    print("Seleccione una opción: ")
    opcion = input()
    if opcion == op1:
        print("Su saldo es de: ", fondos)
        menu()
    elif opcion == op2:
        print("¿Cuánto desea retirar?")
        retirar = int(input())
        if retirar > fondos:
            print("No tiene suficiente saldo")
            menu()
        else:
            fondos -= retirar
            print("Su nuevo saldo es de: ", fondos)
            menu()
    elif opcion == op3:
        print("¿Cuánto desea depositar?")
        depositar = int(input())
        fondos += depositar
        print("Su nuevo saldo es de: ", fondos)
        menu() 
    elif opcion == op4:
        print("¿Cuánto desea transferir?")
        transferir = int(input())
        if transferir > fondos:
            print("No tiene suficiente saldo")
            menu()
        else:
            fondos -= transferir
            print("Su nuevo saldo es de: ", fondos)
            menu()
    elif opcion == op5:
        print("Gracias por usar la app bancaria")
        exit()

menu()  # Llamada inicial a la función
