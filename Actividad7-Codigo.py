# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:08:33 2024

@author: NANCY
"""

import pandas as pd
import numpy as np

# Cargar datos desde el archivo Excel
excel_path = r'C:\Users\NANCY\Desktop\Excel\datos_empacadora.xlsx'
data = pd.read_excel(excel_path)

# Inicialización de parámetros
w1 = 0.37
w2 = 0.58
b = 0
epsilon = 0.05
n = len(data)

# Convertir la columna 'Clase' a numérica (1 para Trucha, 0 para Salmón)
data['Clase'] = np.where(data['Clase'] == 'Trucha', 1, 0)

# Función de kernel de discriminación lineal
def phi(x):
    return w1 * x['Brillo'] + w1 * x['Longitud'] + w1 * x['Color'] + w2 * x['Brillo'] + w1 * x['Longitud'] + w1 * x['Color'] + b

# Ciclo de 10 iteraciones
for iteracion in range(1, 11):
    # Calcular φ(x) para cada patrón
    data['Phi'] = data.apply(phi, axis=1)

    # Calcular el número de vectores de soporte mal clasificados
    Ns_incorrectos = len(data[data['Phi'] * data['Clase'] <= 0])

    # Calcular el error
    error = Ns_incorrectos / n

    # Ajustar el valor de b
    b = b - epsilon * error

    # Mostrar resultados en pantalla
    #print(f'Iteración {iteracion}:')
    #print(f'Número de vectores de soporte mal clasificados: {Ns_incorrectos}')
    #print(f'Error (ε): {error:.4f}')
    #print(f'Nuevo valor de b: {b:.4f}\n')


# Crear un DataFrame para almacenar los resultados con un índice explícito
resultados = pd.DataFrame(columns=['Vectores mal clasificados', 'Error', 'Nuevo valor de b'])

# Ciclo de 10 iteraciones para almacenar los resultados
for iteracion in range(1, 11):
    data['Phi'] = data.apply(phi, axis=1)
    Ns_incorrectos = len(data[data['Phi'] * data['Clase'] <= 0])
    error = Ns_incorrectos / n
    b = b - epsilon * error
    
    # Agregar los resultados a DataFrame con un índice explícito
    resultados = pd.concat([resultados, pd.DataFrame({
        'Vectores mal clasificados': [Ns_incorrectos] * n,
        'Error': [error] * n,
        'Nuevo valor de b': [b] * n
    })], ignore_index=True)

# Imprimir 10 filas al azar de la tabla de resultados
print("\nMuestra de 10 filas al azar de la tabla de resultados:")
print(resultados.sample(10))

print("\nTabla de Resultados:")
print(resultados.sample(10).to_string(index=False))
