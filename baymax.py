import tkinter as tk
from tkinter import messagebox
import json

def guardar_historia_medica(datos_paciente):
    with open("historia_medica.json", "a") as archivo:
        json.dump(datos_paciente, archivo)
        archivo.write("\n")
        messagebox.showinfo("Éxito", "Historia médica guardada con éxito.")

def iniciar_consulta():
    datos_paciente = {}
    datos_paciente["Nombre"] = entry_nombre.get()
    datos_paciente["Edad"] = entry_edad.get()
    datos_paciente["Síntomas"] = entry_sintomas.get()
    datos_paciente["Alergias"] = entry_alergias.get()
    datos_paciente["Antecedentes"] = entry_antecedentes.get()
    guardar_historia_medica(datos_paciente)

#Crear la interfaz gráfica
root = tk.Tk()
root.title("Asistente Médico Virtual")

#boton hombre de paciente
tk.Label(root, text="Nombre del paciente:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Edad:").pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

tk.Label(root, text="Síntomas actuales:").pack()
entry_sintomas = tk.Entry(root)
entry_sintomas.pack()

tk.Label(root, text="Alergias:").pack()
entry_alergias = tk.Entry(root)
entry_alergias.pack()

tk.Label(root, text="Antecedentes médicos:").pack()
entry_antecedentes = tk.Entry(root)
entry_antecedentes.pack()

tk.Button(root, text="Guardar Historia Médica", command=iniciar_consulta).pack()

root.mainloop()