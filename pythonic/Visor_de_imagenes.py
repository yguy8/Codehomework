from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Visor de imagenes')
#icono de ventana

img1 = ImageTK.PhotoImage(Image.open(" "))
img2 = ImageTK.PhotoImage(Image.open("ubicación de la imagen"))
img3 = ImageTK.PhotoImage(Image.open(" "))
img4 = ImageTK.PhotoImage(Image.open(" "))
img5 = ImageTK.PhotoImage(Image.open(" "))

img_list = [img1, img2, img3, img4, img5]

label = Label(image = img)
label.grid(row=0, column=0, columnspan=3)

#funciones de movimiento
def siguiente(numero_imagen):
  global label
  global boton_sigui
  global boton_regre

  img.grid_forget()
  img_label = Label(image=img_list[numero_imagen-1])
  boton_sigui = Button(root, text=">>", command=lambda: siguiente(numero_imagen+1))
  boton_regre = Button(root, tetx="<<", command=lambda: regreso(numero_imagen-1))

  #Si se acaban las imagenes no haya errores y se quede la ventana abierta
  if numero_imagen == 5:
    boton_sigui = Button(root, text=">>", state=DISABLE)
  
  label.grid(row=0, column=0, columnspan=3)
  boton_regre.grid(row=1, column=0)
  boton_sigui.grid(row=1, column=2)

def regreso(numero_imagen):
  global label
  global boton_sigui
  global boton_regre 

  img.grid_forget()
  img_label = Label(image=img_list[numero_imagen-1])
  boton_sigui = Button(root, text=">>", command=lambda: siguiente(numero_imagen+1))
  boton_regre = Button(root, tetx="<<", command=lambda: regreso(numero_imagen-1))

#Si se acaban las imagenes no haya errores y se quede la ventana abierta
  if numero_imagen == 5:
    boton_regre = Button(root, text="<<", state=DISABLE)
  
  label.grid(row=0, column=0, columnspan=3)
  boton_regre.grid(row=1, column=0)
  boton_sigui.grid(row=1, column=2)

#botones de movimiento
boton_sigui = Button(root, text=">>", command=lambda: siguiente())
boton_medio = Button(root, text="Salir", command=root.quit)
boton_regre = Button(root, text="<<", command=lambda: regreso())

# ubicación de los botones
boton_regre.grid(row=1, column=0)
boton_medio.grid(row=1, column=1)
boton_sigui.grid(row=1, column=2)



root.mainloop()
