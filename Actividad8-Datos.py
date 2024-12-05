# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:29:32 2024

@author: NANCY
"""

import pandas as pd
import numpy as np

# Configuración de la generación de datos
np.random.seed(42)  # Establecer semilla para reproducibilidad

# Generar datos aleatorios con los nuevos rangos
brillo_truchas = np.round(np.random.uniform(0.1, 0.70, 100), 4)
brillo_salmón = np.round(np.random.uniform(0.1, 0.69, 100), 4)

longitud_truchas = np.round(np.random.uniform(0.20, 0.39, 100), 4)
longitud_salmón = np.round(np.random.uniform(0.40, 0.91, 100), 4)

color = np.concatenate([np.full(100, 0.33), np.full(100, 0.99)])
clase = np.concatenate([np.ones(100), np.zeros(100)])

# Crear un DataFrame con los datos actualizados
data = pd.DataFrame({
    'No. muestra': [f'pez{i+1}' for i in range(200)],
    'Brillo': np.concatenate([brillo_truchas, brillo_salmón]),
    'Longitud': np.concatenate([longitud_truchas, longitud_salmón]),
    'Color': color,
    'Clase': ['Trucha' if c == 1 else 'Salmón' for c in clase]
})

# Guardar los datos en un archivo Excel
excel_path = r'C:\Users\NANCY\Desktop\Excel\datos_empacadora_actualizado.xlsx'
data.to_excel(excel_path, index=False)
print(f"Los datos actualizados han sido guardados en {excel_path}")
