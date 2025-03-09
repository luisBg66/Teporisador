import time
import tkinter as tk

pausa = False
tiempo_restante = 0
resetear = False

def convertir_a_segundos(entry_tiempo):
    """Convierte el valor del Entry a segundos."""
    tiempo_texto = entry_tiempo.get()
    try:
        if ":" in tiempo_texto:
            minutos, segundos = map(int, tiempo_texto.split(":"))
            return minutos * 60 + segundos
        else:
            return int(tiempo_texto)
    except ValueError:
        entry_tiempo.delete(0, tk.END)
        entry_tiempo.insert(0, "Formato inválido")
        return None

def iniciar_temporizador(entry_tiempo):
    """Obtiene el tiempo desde el Entry y comienza la cuenta regresiva."""
    global tiempo_restante, pausa, resetear

    resetear = False
    tiempo_inicial = convertir_a_segundos(entry_tiempo)
    if tiempo_inicial is None:
        return

    tiempo_restante = tiempo_inicial
    pausa = False
    cuenta_regresiva(entry_tiempo, entry_tiempo.master, lambda: None)

def cuenta_regresiva(entry_tiempo, root, finalizar_temporizador):
    global tiempo_restante, pausa, resetear

    if resetear:
        return

    if tiempo_restante >= 0:
        if not pausa:  # Solo actualizar si NO está en pausa
            minutos = tiempo_restante // 60
            segundos = tiempo_restante % 60
            tiempo_formateado = f"{minutos:02}:{segundos:02}"
            entry_tiempo.delete(0, tk.END)
            entry_tiempo.insert(0, tiempo_formateado)
            tiempo_restante -= 1

        # Llamar a esta función después de 1 segundo, incluso si está en pausa
        root.after(1000, cuenta_regresiva, entry_tiempo, root, finalizar_temporizador)
    else:
        entry_tiempo.delete(0, tk.END)
        entry_tiempo.insert(0, "¡Tiempo terminado!")
        finalizar_temporizador()

def pausar_o_reanudar(boton, root, entry_tiempo):
    global pausa

    pausa = not pausa  # Alternar entre pausado y en marcha
    boton.config(text="Reanudar" if pausa else "Pausar")

    # Si se reanuda, volver a llamar a cuenta_regresiva
    if not pausa:
        cuenta_regresiva(entry_tiempo, root, lambda: None)

def resetear_temporizador(entry_tiempo, boton_iniciar):
    global pausa, resetear
    resetear = True
    pausa = False
    tiempo_inicial = convertir_a_segundos(entry_tiempo)
    if tiempo_inicial is None:
        return
    entry_tiempo.delete(0, tk.END)
    #minutos = tiempo_inicial // 60
    #segundos = tiempo_inicial % 60
    #tiempo_formateado = f"{minutos:02}:{segundos:02}"
    entry_tiempo.insert(0,"00:00")
    boton_iniciar.config(state="normal")  