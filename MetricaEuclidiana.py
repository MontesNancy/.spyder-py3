import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(punto1, punto2):
    return np.sqrt((punto1 - punto2) ** 2)

# Datos de la tabla
datos = {
    'pez1': [0.75, 'Trucha'],
    'pez2': [0.92, 'Trucha'],
    'pez3': [0.84, 'Trucha'],
    'pez4': [0.43, 'Salmón'],
    'pez5': [0.31, 'Salmón'],
    'pez6': [0.20, 'Salmón'],
}

# Obtener las coordenadas (brillo) y las clases de los peces
coordenadas = np.array([dato[0] for dato in datos.values()])
clases = np.array([dato[1] for dato in datos.values()])

# Función para verificar la no negatividad
def verificar_no_negatividad(distancias):
    return np.all(distancias >= 0)

# Función para verificar la reflexividad
def verificar_reflexividad(distancias):
    return np.all(np.diagonal(distancias) == 0)

# Función para verificar la simetría
def verificar_simetria(distancias):
    return np.all(distancias == distancias.T)

# Función para verificar la diferencia triangular
def verificar_diferencia_triangular(distancias):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if distancias[i, j] > distancias[i, k] + distancias[k, j]:
                    return False
    return True

# Calcular las distancias euclidianas
distancias = np.zeros((6, 6))

for i in range(6):
    for j in range(6):
        distancias[i, j] = distancia_euclidiana(coordenadas[i], coordenadas[j])

# Imprimir la matriz de distancias
print("Matriz de Distancias:")
print(distancias)

# Imprimir los resultados en formato de tabla
print("\nPropiedad            | Cumple")
print("---------------------------------")
print(f"No Negatividad       | {verificar_no_negatividad(distancias)}")
print(f"Reflexividad         | {verificar_reflexividad(distancias)}")
print(f"Simetría             | {verificar_simetria(distancias)}")
print(f"Diferencia Triangular| {verificar_diferencia_triangular(distancias)}")

# Graficar las distancias
plt.figure(figsize=(10, 6))
for i in range(6):
    plt.scatter(distancias[:, i], np.ones(6)*i, marker='o', label=f'Pez {i+1}')

plt.title('Distancias Euclidianas entre Peces')
plt.xlabel('Distancia Euclidiana')
plt.yticks(range(6), [f'Pez {i+1}' for i in range(6)])
plt.legend()
plt.show()

