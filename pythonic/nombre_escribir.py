nombre = input("¿Cuál es tu nombre? ")

#en nombres.txt se van a escribir los nombres que ingresemos desde consola "a" es de append 
# que se usa para añadir porque si hacemos un "w" de write escribir reescribe todo
with open("nombres.txt", "a") as file:
    file.write(f"{nombre}\n") #escribir y tener un salto de linea entre lo escrito
    file.close() #cerrar el archivo para que no se corrompa

# Para ver el archivo en la terminal seria 
# python nombre.py -correr el archivo-
# code nombres.txt -ver lo que se ha escrito-
