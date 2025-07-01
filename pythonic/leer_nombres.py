nombre = []

with open("nombres.txt") as file:
    for line in file:
        nombres.append(line.rstrip())

for nombre in sorted(nombres, reverse=TRUE): #ordenados de la z-a con el reverse sin el es a-z
   print(f"hello, {nombre}")

#lo mismo pero más corto y menos manipulable
#with open("nombres.txt") as file:
#    for line in sorted(file):
 #       print("hello,", line.rstrip())
