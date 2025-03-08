import time
import tkinter as tk
from tkinter import messagebox
import os

def iniciar_temporizador():
    try:
        segundos = int(entrada.get())
        if segundos <= 0:
            messagebox.showerror("Error", "Ingrese un número positivo")
            return

        label.config(text="Temporizador en marcha...")
        root.update()
        time.sleep(segundos)

        # Mostrar alerta y reproducir sonido
        messagebox.showinfo("Temporizador", "¡Tiempo terminado!")
        os.system("aplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga &")
        
        label.config(text="Ingrese el tiempo en segundos:")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

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

 # frmer lateral 
frame_lateral = tk.Frame(root, bg="lightgray", width=50)
frame_lateral.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

btn_l1 = tk.Button(frame_lateral, text="config")
btn_l1.pack(pady=5, padx=10, fill="x")

btn_l2 = tk.Button(frame_lateral, text="+")
btn_l2.pack(pady=5, padx=10, fill="x")

 #timer
labelT= tk.Label(root,text="00:00",font=("Arial", 24))
labelT.grid(row=0, column=0, pady=10)

#frmer inferior 
frame = tk.Frame(root)
frame.grid(row=1, column=0)

bntRecec = tk.Button(frame, text="Reseteo")
bntRecec.grid(row=1,column=1,padx=5,pady=10)

bntInicio = tk.Button(frame, text="incio")
bntInicio.grid(row=1,column=2,padx=5,pady=10)

bntPausa = tk.Button(frame, text="pusa")
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

