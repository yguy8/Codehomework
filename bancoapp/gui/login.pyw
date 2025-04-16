from tkinter import Tk, Label, Button, Entry

vent = Tk()
vent.title("Aguila Real")
vent.config(bg="SpringGreen4")
vent.iconbitmap("descarga.ico") # Cambia "descarga.ico" por la ruta de tu icono
vent.resizable(0, 0)
vent.geometry("350x520")


def ingresar():
    usuario = text1.get()
    contrasena = text2.get()
    print("Usuario:", usuario, "Contraseña:", contrasena)
    if usuario == "admin" and contrasena == "1234":
        print("Bienvenido al sistema")
    else:
        print("Usuario o contraseña incorrectos")

lbl1 = Label(vent, text="Bienvenido a Aguila Real", fg="black", bg="SpringGreen4",font=("Special Gothic", 17))
lbl1.place(x=50, y=30, width=250, height=30)
lbl2 = Label(vent, text="Ingrese usuario y contraseña", fg="white", bg="SpringGreen4",font=("Special Gothic", 12))
lbl2.place(x=50, y=90, width=250, height=30)

text1 = Entry(vent, width=20, bg="DarkOliveGreen3", fg="black")
text1.place(x=50, y=150, width=250, height=50)
text2 = Entry(vent, width=20, bg="DarkOliveGreen3", fg="black")
text2.place(x=50, y=210, width=250, height=50)
btt =Button(vent, text="Ingresar", fg="black", bg="SpringGreen4", font=("Special Gothic", 12), command=ingresar)
btt.place(x=50, y=300, width=250, height=50)

vent.mainloop()