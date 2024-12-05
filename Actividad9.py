# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:20:09 2024

@author: NANCY
"""

import pandas as pd
import numpy as np

# Paso 1: Leer el archivo de datos
data = pd.read_excel(r'C:\Users\NANCY\Desktop\Excel\coleccion_msv_perceptron.xlsx')

# Paso 2: Establecer bias_msv = 0
bias_msv = 0

# Paso 3: Elegir el kernel como una red neuronal tipo perceptrón
# Paso 4: Considerar los pesos
w11 = 0.80
w12 = 0.33
w13 = 0.55

# Paso 5: Iniciar ciclo de 10 iteraciones
for i in range(10):
    # Paso 6: Establecer parámetro de aprendizaje alpha
    alpha = 1.0
    
    # Paso 7: Establecer bias_ptrn
    bias_ptrn = 1 + bias_msv
    
    # Paso 8: Iniciar ciclo de 20 iteraciones para el perceptrón
    for j in range(20):
        # Paso 9: Calcular la respuesta para la unidad de salida Yin
        data['Yin'] = bias_ptrn + (data['brillo'] * w11) + (data['longuitud'] * w12) + (data['color_code'] * w13)
        
        # Paso 10: Verificar la regla de activación del perceptrón
        theta = 0.67
        data['Yactivada'] = np.where(data['Yin'] > theta, 1, 0)
        
        # Paso 11: Comparar Yactivada con Clase y actualizar pesos si es necesario
        data['diferente'] = np.where(data['Yactivada'] != data['Clase'], 1, 0)
        misclassified = data[data['diferente'] == 1]
        # Paso 12
        if not misclassified.empty:
            w11 += misclassified['Clase'].iloc[0] * alpha * misclassified['brillo'].iloc[0]
            w12 += misclassified['Clase'].iloc[0] * alpha * misclassified['longuitud'].iloc[0]
            w13 += misclassified['Clase'].iloc[0] * alpha * misclassified['color_code'].iloc[0]
        else:
            break  # Si todos los patrones están clasificados correctamente, salir del ciclo
        
    # Paso 15: Calcular vectores de soporte no clasificados correctamente
    Ns = misclassified.shape[0] if not misclassified.empty else 0
    
    # Paso 16: Calcular el error de la MSV
    error = 0.045 * Ns / data.shape[0]
    
    # Paso 17: Ajustar bias_msv
    bias_msv -= error
    
    # Mostramos la tabla al finalizar cada iteración
    print("Iteración:", i+1)
    print("Vectores de soporte:", Ns)
    print("Error:", error)
    print("Bias MSV:", bias_msv)
    print("Bias PTRN:", bias_ptrn)
    print("-----------------------------")

    
    # Paso 18: Repetir el proceso
    # Paso 19: Fin del algoritmo de MSV
