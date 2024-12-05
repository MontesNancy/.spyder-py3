# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:31:52 2024

@author: NANCY
"""

import tkinter as tk
import time

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Liam te amo")
ventana.geometry("400x200")
ventana.configure(bg='black')

# Lista de colores para el efecto brillante
colores = ["red", "yellow", "green", "blue", "purple", "pink", "orange"]

# Crear una etiqueta con el mensaje
mensaje = tk.Label(ventana, text="Liam te amo", font=("Helvetica", 32, "bold"), bg="black")
mensaje.pack(pady=40)

# Función para animar el movimiento del texto y cambiar colores
def animar_texto():
    x_pos = 0
    color_index = 0
    direccion = 1  # 1 para mover a la derecha, -1 para mover a la izquierda

    while True:
        # Mover el texto de lado a lado
        if x_pos > 200 or x_pos < 0:
            direccion = -direccion  # Cambiar dirección si llega al borde
        x_pos += direccion * 5
        mensaje.place(x=x_pos, y=70)

        # Cambiar color del texto para simular brillo
        mensaje.config(fg=colores[color_index])
        color_index = (color_index + 1) % len(colores)

        # Pausar un poco antes de la siguiente iteración
        ventana.update()
        time.sleep(0.1)

# Ejecutar la animación en un hilo separado
ventana.after(0, animar_texto)

# Ejecutar la ventana
ventana.mainloop()
