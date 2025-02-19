print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones que puedes realizar son suma, resta, mult y div")

resultado = ""
while True:
   if not resultado:
    resultado = input("Ingrese un numero: ")
    if resultado.lower() == "salir":
        break 
    resultado = int(resultado)
    op = input("Ingrese un operador: ")
    if op.lower == "salir":
        break
    n2 = input("Ingresa el siguiente número: ")
    if n2.lower == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
            resultado += n2
    elif op.lower() == "resta":
            resultado -= n2
    elif op.lower() == "mult":
            resultado *= n2
    elif op.lower() == "div":     
            resultado /= n2
    else: 
        print("Operación no válida")
    break 

print(f"El resultado es {resultado}")