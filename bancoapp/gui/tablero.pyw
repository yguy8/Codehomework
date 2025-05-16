from tkinter import Tk, Label, Button, Toplevel

vent2 = Tk()
vent2.title("Aguila Real")
vent2.config(bg="SpringGreen4")
#vent2.iconbitmap("descarga.ico") # Cambia "descarga.ico" por la ruta de tu icono
vent2.resizable(0, 0)
vent2.geometry("350x520")

def abrir_nueva_ventana():
    nueva_ventana = Toplevel(vent2)
    nueva_ventana.config(bg="SpringGreen4")
    nueva_ventana.title("Consultar Saldo")
    nueva_ventana.iconbitmap("descarga.ico") 
    nueva_ventana.geometry("350x520")
    etiqueta = Label(nueva_ventana, text="¿Hola, listo para ver tu saldo?", bg="SpringGreen4", font=("Special Gothic", 12))
    etiqueta.pack(pady=20)
    
def abrir_segunda_ventana():
    segunda_ventana = Toplevel(vent2)
    segunda_ventana.config(bg="SpringGreen4")
    segunda_ventana.title("Retirar Dinero")
    segunda_ventana.iconbitmap("descarga.ico")
    segunda_ventana.geometry("350x520")
    etiqueta = Label(segunda_ventana, text="¿Hola, listo para retirar dinero?", bg="SpringGreen4", font=("Special Gothic", 12))
    etiqueta.pack(pady=20)


#títulos de la app
lbl1 = Label(vent2, text="Bienvenido a Aguila Real", fg="black", bg="SpringGreen4",font=("Special Gothic", 17))
lbl1.place(x=50, y=30, width=250, height=30)
lbl2 = Label(vent2, text="¿Qué desea realizar?", fg="white", bg="SpringGreen4",font=("Special Gothic", 12))
lbl2.place(x=50, y=90, width=250, height=30)
#botones de la app
btt =Button(vent2, text="Mostrar saldo", fg="white", bg="SpringGreen4", font=("Special Gothic", 12), command=abrir_nueva_ventana, activeforeground="SpringGreen4", activebackground="white")
btt.place(x=50, y=150, width=250, height=50)
btt2 =Button(vent2, text="Retirar dinero", fg="white", bg="SpringGreen4", font=("Special Gothic", 12), command=abrir_segunda_ventana, activeforeground="SpringGreen4", activebackground="white")
btt2.place(x=50, y=210, width=250, height=50)
btt3 =Button(vent2, text="Salir", fg="white", bg="SpringGreen4", font=("Special Gothic", 12), command=vent2.destroy, activeforeground="SpringGreen4", activebackground="white")
btt3.place(x=50, y=270, width=250, height=50)

vent2.mainloop()