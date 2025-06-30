#importa el modulo que debe estar en el mismo directorio
from calculadora import cuadrado 

def main():
    test_cuadrado()

def test_cuadrado():
   # Cuando se assert (acertado el test) no va a ir nada a la salida 
   # porque todo esta bien cuando ocurra el AssertionError va a  # imprimir el tipo de error
    
    try:
        assert cuadrado(2) == 4
    except AssertionError:
        print("Error: El cuadrado de 2 debería ser 4")
    try:
        assert cuadrado(3) == 9
    except AssertionError:
        print("Error: El cuadrado de 3 debería ser 9")
    try:
        assert cuadrado(-2) == 4
    except AssertionError:
        print("Error: El cuadrado de -2 debería ser 4")
    try:
        assert cuadrado(-3) == 9
    except AssertionError:
        print("Error: El cuadrado de -3 debería ser 9")

if __name__ == "__main__":
    main()
    
