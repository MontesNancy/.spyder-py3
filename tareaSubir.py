# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:08:33 2024

@author: NANCY
"""

import pandas as pd
import numpy as np

# Cargar datos desde el archivo Excel
excel_path = r'C:\Users\NANCY\Desktop\Excel\datos_empacadora_actualizado.xlsx'
data = pd.read_excel(excel_path)

# Definir otras variables necesarias
epsilon = 0.05  # Valor dado
n = 200  # Número total de patrones
b = 0  # Inicializar b
w1 = 0.37  # Inicializar w1 (
w2 = 0.58  # Inicializar w2 
w3 = 0  # Tercera característica (Brillo, Longitud, Color)

# Convertir la columna 'Clase' a numérica (1 para Trucha, 0 para Salmón)
data['Clase'] = np.where(data['Clase'] == 'Trucha', 1, 0)

# Función de kernel de discriminación lineal para truchas
def phi_truchas(row):
    return (w1 * row['Brillo']) + (w1 * row['Longitud']) + (w1 * row['Color']) + (w2 * row['Brillo']) + (w2 * row['Longitud']) + (w2 * row['Color']) - b - 1

# Función de kernel de discriminación lineal para salmones
def phi_salmones(row):
    return (w1 * row['Brillo']) + (w1 * row['Longitud']) + (w1 * row['Color']) + (w2 * row['Brillo']) + (w2 * row['Longitud']) + (w2 * row['Color']) + b + 1

# Ciclo de iteraciones
iteraciones = 0
while iteraciones < 20 and len(data[(phi_truchas(data) * data['Clase'] <= 0) | (phi_salmones(data) * (1 - data['Clase']) <= 0)]) > 0:
    iteraciones += 1
    # Calcular φ(x) para cada patrón de truchas
    data['Phi_Truchas'] = data[data['Clase'] == 1].apply(phi_truchas, axis=1)
    
    # Calcular φ(x) para cada patrón de salmones
    data['Phi_Salmones'] = data[data['Clase'] == 0].apply(phi_salmones, axis=1)
    
    # Calcular el número de vectores de soporte mal clasificados
    Ns_incorrectos = len(data[(phi_truchas(data) <= 0) | (phi_salmones(data) <= 0)])

    # Calcular el error
    error = (Ns_incorrectos * epsilon) / n

    # Ajustar el valor de b
    b = b - error

# Crear un DataFrame para almacenar los resultados con un índice explícito
resultados = pd.DataFrame(columns=['VSoporte', 'Error', 'Nuevo valor de b'])

# Ciclo de iteraciones para almacenar los resultados
iteraciones = 0
while iteraciones < 20 and len(data[(phi_truchas(data) * data['Clase'] <= 0) | (phi_salmones(data) * (1 - data['Clase']) <= 0)]) > 0:
    iteraciones += 1
    # Calcular φ(x) para cada patrón de truchas
    data['Phi_Truchas'] = data[data['Clase'] == 1].apply(phi_truchas, axis=1)
    
    # Calcular φ(x) para cada patrón de salmones
    data['Phi_Salmones'] = data[data['Clase'] == 0].apply(phi_salmones, axis=1)
    
    # Calcular el número de vectores de soporte mal clasificados
    Ns_incorrectos = len(data[(phi_truchas(data) <= 0) | (phi_salmones(data) <= 0)])
    
    # Calcular el error
    error = (Ns_incorrectos * epsilon) / n
    b = b - error
    
    # Agregar los resultados a DataFrame con un índice explícito
    resultados = pd.concat([resultados, pd.DataFrame({
        'VSoporte': [Ns_incorrectos] * n,
        'Error': [error] * n,
        'Nuevo valor de b': [b] * n
        })], ignore_index=True)
    

# Imprimir 10 filas al azar de la tabla de resultados
print("\nTabla de Resultados:")
print(resultados.sample(10).to_string(index=False))


# Agregar la columna 'Phi' a los resultados
phi_data = pd.DataFrame({'Phi_Truchas': data['Phi_Truchas'], 'Phi_Salmones': data['Phi_Salmones']})

# Guardar la columna 'Phi' en un archivo Excel
phi_data.to_excel(r'C:\Users\NANCY\Desktop\Excel\phi_data_actualizado.xlsx', index=False)

print("Datos de 'Phi' guardados en phi_data.xlsx")

