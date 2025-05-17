from tkinter import Tk

app=Tk()
app.title("Aguila Real")

#El icono debe estar en la carpeta 
app.config(bg="SpringGreen4")
app.iconbitmap("descarga.ico")
app.resizable(1,1)
app.geometry("350x520")
#Esto siempre debe estar al última 
 #aquí iba el mainloop creo que ese era el error

#División de sesiones 
#frame 1 el de la izq

frame_logo = Frame(app, bg="SpringGreen3")
frame_logo.pack(side=LEFT, fill=BOTH, expand=True)

app.mainloop()
