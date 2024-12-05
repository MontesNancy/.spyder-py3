import pandas as pd
import numpy as np

# Cargar datos desde el archivo Excel
excel_path = r'C:\Users\NANCY\Desktop\Excel\datos_empacadora_actualizado.xlsx'
data = pd.read_excel(excel_path)

# Definir otras variables necesarias
epsilon = 0.05  # Valor dado
n = 200  # Número total de patrones
b = 0  # Inicializar b
w1 = 0.37  # Inicializar w1 
w2 = 0.58  # Inicializar w2 
w3 = 0  # Tercera característica (Brillo, Longitud, Color)

# Convertir la columna 'Clase' a numérica (1 para Trucha, 0 para Salmón)
data['Clase'] = np.where(data['Clase'] == 'Trucha', 1, 0)

# Definir DataFrame para almacenar resultados
resultados = pd.DataFrame(columns=['VSoporte', 'Error', 'Nuevo valor de b', 'truchas', 'Salmon'])

# Función de kernel de discriminación lineal para truchas
def phi_truchas(row):
    return (w1 * row['Brillo']) + (w1 * row['Longitud']) + (w1 * row['Color']) + (w2 * row['Brillo']) + (w2 * row['Longitud']) + (w2 * row['Color']) - b - 1

# Función de kernel de discriminación lineal para salmones
def phi_salmón(row):
    return (w1 * row['Brillo']) + (w1 * row['Longitud']) + (w1 * row['Color']) + (w2 * row['Brillo']) + (w2 * row['Longitud']) + (w2 * row['Color']) + b + 1

# Ciclo de iteraciones
for iteracion in range(1, 11):
    # Calcular φ(x) para cada patrón y actualizar el valor de b
    data['Phi'] = data.apply(phi_truchas, axis=1)  # Calcular Phi para truchas
    if len(data[data['Phi'] * data['Clase'] <= 0]) != 0:
        truchas = len(data[(data.index <= 100) & (data['Phi'] < 1)])
        salmones = len(data[(data.index > 100) & (data['Phi'] >= 1)])   
        Ns_incorrectos = (truchas + salmones) - 100
        error = (Ns_incorrectos * epsilon) / n
        b = b - error
        # Agregar los resultados a DataFrame con un índice explícito
        resultados = pd.concat([resultados, pd.DataFrame({
            'VSoporte': [Ns_incorrectos] * n,
            'Error': [error] * n,
            'Nuevo valor de b': [b] * n,
            'truchas':[truchas] *n,
            'Salmon': [salmones] * n,
            })], ignore_index=True)
    else:
        break

# Imprimir 10 filas al azar de la tabla de resultados
print("\nTabla de Resultados:")
print(resultados.sample(10).to_string(index=False))

# Agregar la columna 'Phi' a los resultados
phi_data = pd.DataFrame({'Phi': data['Phi']})

# Guardar la columna 'Phi' en un archivo Excel
phi_data.to_excel(r'C:\Users\NANCY\Desktop\Excel\phi_data_actualizado.xlsx', index=False)

print("Datos de 'Phi' guardados en phi_data_actualizado.xlsx")

