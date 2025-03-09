import time
# funciones.py
pausa=False
tiempo_restante = 120  # 

# Esta función actualiza el texto del Label
def cuenta_regresiva(actualizar_label, root,finalizar_temporizador):
    global tiempo_restante, pausa

    if tiempo_restante >= 0:
        if not pausa:  # Solo actualizar si NO está en pausa
            minutos = tiempo_restante // 60
            segundos = tiempo_restante % 60
            tiempo_formateado = f"{minutos:02}:{segundos:02}"
            actualizar_label(tiempo_formateado)
            tiempo_restante -= 1

        # Llamar a esta función después de 1 segundo, incluso si está en pausa
        root.after(1000, cuenta_regresiva, actualizar_label, root, finalizar_temporizador)
    else:
        actualizar_label("¡Tiempo terminado!")
        finalizar_temporizador()

# Función para pausar o reanudar el temporizador
def pausar_o_reanudar(boton, root, actualizar_label):
    global pausa

    pausa = not pausa  # Alternar entre pausado y en marcha
    boton.config(text="Reanudar" if pausa else "Pausar")

    # Si se reanuda, volver a llamar a cuenta_regresiva
    if not pausa:
        cuenta_regresiva(actualizar_label, root)

# Función para resetear el temporizador y activar el botón de inicio
def resetear_temporizador(actualizar_label, boton_iniciar):
    global tiempo_restante, pausa
    pausa = False
    tiempo_restante = 120  # Reiniciar a 2 minutos
    actualizar_label("02:00")
    boton_iniciar.config(state="normal")  # Reactivar botón de inicio