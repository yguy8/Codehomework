with open("nombres.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())


#lo mismo pero más largo
#nombre = []

#with open("nombres.txt") as file:
#    for line in file:
#        nombres.append(line.rstrip())

#for nombre in sorted(nombres):
#    print(f"hello, {nombre}")

