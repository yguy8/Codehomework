from tkinter import Tk

app=Tk()
app.title("Aguila Real")

#El icono debe estar en la carpeta 
app.config(bg="SpringGreen4")
app.iconbitmap("descarga.ico")
app.resizable(1,1)
app.geometry("350x650")
#Esto siempre debe estar al última 
app.mainloop()