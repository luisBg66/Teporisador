import time
import tkinter as tk
from tkinter import messagebox
import os
from Funcion_temporisado import cuenta_regresiva,pausar_o_reanudar,resetear_temporizador

# Configuración de la ventana
root = tk.Tk()
root.title("Temporizador")
root.geometry("350x200")

#Configuracion de la distrubucion de la ventna 
root.columnconfigure(0, weight=0)  # Columna para el menú lateral
root.rowconfigure(0,weight=1) #espacio para label
root.rowconfigure(2, weight=1)#configuracion en medio
root.columnconfigure(0, weight=1)#configuracion para el bution
root.rowconfigure(2, weight=0)#configuracion flial botones 

# Función para actualizar el texto del label
def actualizar_label(tiempo_formateado):
    labelT.config(text=f"{tiempo_formateado}")

def finalizar_temporizador():
    bntInicio.config(state=tk.NORMAL)  # Reactivar botón cuando el tiempo termine

 # frmer lateral 
frame_lateral = tk.Frame(root, bg="lightgray", width=50)
frame_lateral.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

btn_l1 = tk.Button(frame_lateral, text="config")
btn_l1.pack(pady=5, padx=10, fill="x")

btn_l2 = tk.Button(frame_lateral, text="+")
btn_l2.pack(pady=5, padx=10, fill="x")

 #timer


labelT = tk.Label(root, text="00:00", font=("Arial", 18))
labelT.grid(row=0, column=0, pady=10)

# Función para iniciar el temporizador
def iniciar_temporizador():
    bntInicio.config(state=tk.DISABLED)  # Desactivar botón al iniciar
    cuenta_regresiva(actualizar_label, root, finalizar_temporizador)



#frmer inferior 
frame_inferior = tk.Frame(root)
frame_inferior.grid(row=1, column=0)

bntRecec = tk.Button(frame_inferior, text="Reseteo", command= lambda: resetear_temporizador(actualizar_label,bntRecec))
bntRecec.grid(row=1,column=1,padx=5,pady=10)


bntInicio = tk.Button(frame_inferior, text="incio",command=iniciar_temporizador)
bntInicio.grid(row=1,column=2,padx=5,pady=10)

bntPausa = tk.Button(frame_inferior, text="pusa", command=lambda:pausar_o_reanudar(bntPausa, root, actualizar_label))
bntPausa.grid(row=1,column=3,padx=5,pady=10)
""""


label = tk.Label(root, text="Ingrese el tiempo en segundos:")
label.pack(pady=5)

entrada = tk.Entry(root)
entrada.pack(pady=5)

btn = tk.Button(root, text="Iniciar", command=iniciar_temporizador)
btn.pack(pady=10)
"""
root.mainloop()

