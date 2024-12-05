import numpy as np
import matplotlib.pyplot as plt

# Definir los datos
datos = {
    "pez1": [0.75, 0.20, "Trucha"],
    "pez2": [0.92, 0.30, "Trucha"],
    "pez3": [0.84, 0.40, "Trucha"],
    "pez4": [0.77, 0.25, "Trucha"],
    "pez5": [0.84, 0.35, "Trucha"],
    "pez6": [0.96, 0.32, "Trucha"],
    "pez7": [0.43, 0.43, "Salmon"],
    "pez8": [0.31, 0.50, "Salmon"],
    "pez9": [0.20, 0.60, "Salmon"],
    "pez10": [0.16, 0.70, "Salmon"],
    "pez11": [0.22, 0.80, "Salmon"],
    "pez12": [0.45, 0.91, "Salmon"]
}

# Función para calcular la distancia euclidiana
def distancia_euclidiana(punto1, punto2):
    return np.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)

# Crear la matriz de distancias
matriz_distancias = np.zeros((len(datos), len(datos)))

# Organizamos la matriz en filas de 12x12
for i, (_, punto1) in enumerate(datos.items()):
    for j, (_, punto2) in enumerate(datos.items()):
        matriz_distancias[i, j] = distancia_euclidiana(punto1, punto2)

# Visualizar la matriz de distancias de manera organizada
print("Matriz de Distancias:")
for fila in matriz_distancias:
    print(" ".join(f"{distancia:.4f}" for distancia in fila))

# Calcular la distancia euclidiana entre pez1 y pez2 usando la fórmula proporcionada
distancia_pez1_pez2_formula = distancia_euclidiana(datos["pez1"], datos["pez2"])
print(f'\nDistancia entre pez1 y pez2 usando la fórmula proporcionada: {distancia_pez1_pez2_formula}')

# Graficar todas las distancias calculadas
plt.scatter(np.arange(len(datos)*len(datos)), matriz_distancias.flatten())
plt.title('Distancias Euclidianas')
plt.xlabel('Pares de puntos')
plt.ylabel('Distancia Euclidiana')
plt.show()