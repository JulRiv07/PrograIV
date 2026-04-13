import tkinter as tk

def menu2():
    vehiculos = [
        "Coche - 4 ruedas",
        "Bicicleta - 2 ruedas",
        "Camioneta - 4 ruedas",
        "Motocicleta - 2 ruedas"
    ]

    ventana = tk.Toplevel() 
    ventana.title("Catálogo Vehículos")

    lista = tk.Listbox(ventana, width=40)
    lista.pack()

    def mostrar():
        lista.delete(0, tk.END)
        for v in vehiculos:
            lista.insert(tk.END, v)

    def filtrar_2():
        lista.delete(0, tk.END)
        for v in vehiculos:
            if "2 ruedas" in v:
                lista.insert(tk.END, v)

    def filtrar_4():
        lista.delete(0, tk.END)
        for v in vehiculos:
            if "4 ruedas" in v:
                lista.insert(tk.END, v)

    tk.Button(ventana, text="Mostrar todos", command=mostrar).pack()
    tk.Button(ventana, text="2 ruedas", command=filtrar_2).pack()
    tk.Button(ventana, text="4 ruedas", command=filtrar_4).pack()