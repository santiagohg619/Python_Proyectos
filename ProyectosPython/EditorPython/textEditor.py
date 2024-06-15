import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Función Abrir archivo
def abrir_archivo(ventana, text_edit):
    filepath = askopenfilename(filetypes = [("Text Files", "*.txt")])
    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    ventana.title(f"Archivo abierto: {filepath}")

#Función Guardar archivo
def guardar_archivo(ventana, text_edit):
    filepath = asksaveasfilename(filetypes = [("Text Files", "*.txt")])
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    ventana.title(f"Archivo guardado: {filepath}")

#Función principal
#Creación de la ventana principal
def main():
    ventana = tk.Tk()

    #Título de la ventana
    ventana.title("Editor de texto")

    #Tamaño de la ventana
    ventana.rowconfigure(0, minsize = 400)
    ventana.columnconfigure(1, minsize = 500)

    #Fuente del texto
    text_edit = tk.Text(ventana, font = "Helvetica 18")
    #Ubicación del texto
    text_edit.grid(row = 0, column = 1)

    #Frame
    frame = tk.Frame(ventana, relief = tk.RAISED, bd = 2)
    #Boton guardar
    boton_guardar = tk.Button(frame, text = "Guardar", command = lambda: guardar_archivo(ventana, text_edit))
    #Boton abrir
    boton_abrir = tk.Button(frame, text = "Abrir", command = lambda: abrir_archivo(ventana, text_edit))

    #Ubicación del frame
    boton_guardar.grid(row = 0, column = 0, padx = 5, pady = 5)
    boton_abrir.grid(row = 1, column = 0, padx = 5, sticky = "ew")
    frame.grid(row = 0, column = 0, sticky = "ns")

    ventana.bind("<Control-s>", lambda x: guardar_archivo(ventana, text_edit))
    ventana.bind("<Control-o>", lambda x: abrir_archivo(ventana, text_edit))


    #Abrir ventana
    ventana.mainloop()


main()

