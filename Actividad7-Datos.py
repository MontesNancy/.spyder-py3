import pandas as pd
import numpy as np

# Configuración de la generación de datos
np.random.seed(42)  # Establecer semilla para reproducibilidad

# Generar datos aleatorios
brillo = np.round(np.random.uniform(0, 1, 200), 4)
longitud = np.round(np.random.uniform(0.20, 0.90, 200), 4)
color = np.concatenate([np.full(100, 0.33), np.full(100, 0.99)])
clase = np.concatenate([np.ones(100), np.zeros(100)])

# Inicialización de parámetros
b = 0
w1 = 0.37
w2 = 0.58

# Crear un DataFrame con los datos
data = pd.DataFrame({
    'No. muestra': [f'pez{i+1}' for i in range(200)],
    'Brillo': brillo,
    'Longitud': longitud,
    'Color': color,
    'Clase': ['Trucha' if c == 1 else 'Salmón' for c in clase]
})

# Guardar los datos en un archivo Excel
excel_path = r'C:\Users\NANCY\Desktop\Excel\datos_empacadora.xlsx'
data.to_excel(excel_path, index=False)
print(f"Los datos han sido guardados en {excel_path}")


