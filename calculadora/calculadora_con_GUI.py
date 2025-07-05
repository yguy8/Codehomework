import tkinter as tk

class calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.configure(bg="royalblue")
        self.pantalla = tk.Entry(self.root, width=30, font=("Arial", 16), bg="white")
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.crear_boton()

    def crear_boton(self):
        botones = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 0), ('+', 1, 3), ('-', 2, 3), 
            ('*', 3, 3), ('/', 4, 3), ('=', 4, 1), 
            ('C', 4, 2) 
        ]

        for(text, row, col) in botones:
            button = tk.Button(self.root, text=text, padx=30, pady=30, bg="cornflowerblue", fg="white", command=lambda t=text: self.boton_click(t))
            button.grid(row=row, column=col, sticky="nsew")

    def boton_click(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.pantalla.get())
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
        elif valor == "C":
            self.pantalla.delete(0, tk.END)
        else:
            current = self.pantalla.get()
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, current + valor)

root = tk.Tk()
calculadora = calculadora(root)


root.mainloop()
