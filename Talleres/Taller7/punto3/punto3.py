import tkinter as tk
from .ejemplo1 import menu1
from .ejemplo2 import menu2

def menu3():
    ventana = tk.Tk()
    ventana.title("MENÚ PUNTO 3")

    tk.Label(ventana, text="Seleccione una opción").pack(pady=10)

    tk.Button(ventana, text="Ejemplo 1", command=menu1).pack(pady=5)
    tk.Button(ventana, text="Ejemplo 2", command=menu2).pack(pady=5)

    tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=20)

    ventana.mainloop()