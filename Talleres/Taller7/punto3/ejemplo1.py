import tkinter as tk

def menu1():
    def calcular_area():
        try:
            base = float(entry_base.get())
            altura = float(entry_altura.get())

            if base <= 0 or altura <= 0:
                resultado.config(text="Valores deben ser positivos")
            else:
                area = (base * altura) / 2
                resultado.config(text=f"Área: {area}")

        except:
            resultado.config(text="Entrada inválida")

    ventana = tk.Toplevel() 
    ventana.title("Área Triángulo")

    tk.Label(ventana, text="Base:").pack()
    entry_base = tk.Entry(ventana)
    entry_base.pack()

    tk.Label(ventana, text="Altura:").pack()
    entry_altura = tk.Entry(ventana)
    entry_altura.pack()

    tk.Button(ventana, text="Calcular", command=calcular_area).pack()

    resultado = tk.Label(ventana, text="")
    resultado.pack()