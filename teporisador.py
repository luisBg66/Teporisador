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
root.geometry("300x150")

label = tk.Label(root, text="Ingrese el tiempo en segundos:")
label.pack(pady=5)

entrada = tk.Entry(root)
entrada.pack(pady=5)

btn = tk.Button(root, text="Iniciar", command=iniciar_temporizador)
btn.pack(pady=10)

root.mainloop()

