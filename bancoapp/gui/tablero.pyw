from tkinter import Tk, Label, Entry, Button

vent = Tk()
vent.title("Aguila Real")
vent.config(bg="SpringGreen4")
vent.iconbitmap("descarga.ico") # Cambia "descarga.ico" por la ruta de tu icono
vent.resizable(0, 0)
vent.geometry("350x520")

def retirar():
    num1 = text1.get()
    num2 = text2.get()
    retiro = float(num1) - float(num2) 
    text3.insert(0,retiro)
    

#títulos de la app
lbl1 = Label(vent, text="Bienvenido a Aguila Real", fg="black", bg="SpringGreen4",font=("Special Gothic", 17))
lbl1.place(x=50, y=30, width=250, height=30)
lbl2 = Label(vent, text="¿Qué desea realizar?", fg="white", bg="SpringGreen4",font=("Special Gothic", 12))
lbl2.place(x=50, y=90, width=250, height=30)

text1 = Entry(vent, width=20, bg="DarkOliveGreen3", fg="black")
text1.place(x=50, y=210, width=120, height=50)
text2 = Entry(vent, width=20, bg="DarkOliveGreen3", fg="black")
text2.place(x=180, y=210, width=120, height=50)
btt =Button(vent, text="Retirar", fg="black", bg="SpringGreen4", font=("Special Gothic", 12), command=retirar)
btt.place(x=50, y=150, width=250, height=50)

text3 = Entry(vent, width=20, bg="DarkOliveGreen3", fg="black")
text3.place(x=50, y=370, width=250, height=50)

vent.mainloop()