import time
import tkinter as tk
from tkinter import messagebox
import os
from Funcion_temporisado import cuenta_regresiva, pausar_o_reanudar, resetear_temporizador, iniciar_temporizador

# Configuración de la ventana
root = tk.Tk()
root.title("Temporizador")
root.geometry("350x200")

# Configuración de la distribución de la ventana
root.columnconfigure(0, weight=0)  # Columna para el menú lateral
root.rowconfigure(0, weight=1)  # Espacio para label
root.rowconfigure(2, weight=1)  # Configuración en medio
root.columnconfigure(0, weight=1)  # Configuración para el botón
root.rowconfigure(2, weight=0)  # Configuración final botones

# Frame lateral
frame_lateral = tk.Frame(root, bg="lightgray", width=50)
frame_lateral.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

btn_l1 = tk.Button(frame_lateral, text="config")
btn_l1.pack(pady=5, padx=10, fill="x")

btn_l2 = tk.Button(frame_lateral, text="+")
btn_l2.pack(pady=5, padx=10, fill="x")

# Entry que servirá para ingresar y mostrar el tiempo restante
entry_tiempo = tk.Entry(root, width=10, font=("Arial", 20), justify="center")
entry_tiempo.insert(0, "00:00")  # Tiempo inicial en segundos
entry_tiempo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Función para iniciar el temporizador
def iniciar_temporizador_gui():
    bntInicio.config(state=tk.DISABLED)  # Desactivar botón al iniciar
    iniciar_temporizador(entry_tiempo)

# Frame inferior
frame_inferior = tk.Frame(root)
frame_inferior.grid(row=1, column=0)

bntRecec = tk.Button(frame_inferior, text="Reseteo", command=lambda: resetear_temporizador(entry_tiempo, bntInicio))
bntRecec.grid(row=1, column=1, padx=5, pady=10)

bntInicio = tk.Button(frame_inferior, text="Inicio", command=iniciar_temporizador_gui)
bntInicio.grid(row=1, column=2, padx=5, pady=10)

bntPausa = tk.Button(frame_inferior, text="Pausa", command=lambda: pausar_o_reanudar(bntPausa, root, entry_tiempo))
bntPausa.grid(row=1, column=3, padx=5, pady=10)

root.mainloop()

