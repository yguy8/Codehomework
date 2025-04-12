from tkinter import Tk, Label, Entry

app = Tk()
app.title("Aguila Real")

#El diseño de la ventana
app.config(bg="SpringGreen4")
app.iconbitmap("descarga.ico")
app.resizable(1,1)
app.geometry("350x520")

lbl1 = Label(app, text="Bienvenido a Aguila Real", bg="DarkOliveGreen3", fg="aliceblue")
lbl1.place(x=50, y=60, width=250, height=50)

lbl2 = Label(app, text="Ingrese su usuario y contraseña", fg="SkyBlue4")
txt1 = Entry(app, width=20, bg="DarkOliveGreen3", fg="aliceblue")
txt1.place(x=50, y=120, width=250, height=50)
txt2 = Entry(app, width=20, bg="DarkOliveGreen3", fg="aliceblue")
txt2.place(x=50, y=180, width=250, height=50)

#Esto siempre debe estar al última para que corra la ventana
app.mainloop()