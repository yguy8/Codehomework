import tkinter as tk
from tkinter import ttk

def seleccionar_opcion(event):
    seleccion = combo.get()
    print(f"Has seleccionado: {seleccion}")

# Crear la ventana principal
root = tk.Tk()
root.title("Selección de Opción")
root.geometry("350x520")
root.iconbitmap("descarga.ico")  # Cambia "descarga.ico" por la ruta de tu icono
root.config(bg="SpringGreen4")

# Crear un marco para organizar los widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Crear una lista de opciones
opciones = ["Retirar", "Salir"]

# Crear el menú desplegable (combobox)
combo = ttk.Combobox(frame, values=opciones)
combo.grid(row=0, column=0, padx=5, pady=5)
combo.bind("<<ComboboxSelected>>", seleccionar_opcion)

# Ejecutar el bucle principal de la ventana
root.mainloop()
