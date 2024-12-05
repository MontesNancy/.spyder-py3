import numpy as np
import matplotlib.pyplot as plt

def calcular_distancia_euclidiana(punto1, punto2):
    return np.sqrt(np.sum((np.array(punto1, dtype=float) - np.array(punto2, dtype=float)) ** 2))

# Datos de la tabla
datos = {
    'pez1': [0.75, 'Trucha'],
    'pez2': [0.92, 'Trucha'],
    'pez3': [0.84, 'Trucha'],
    'pez4': [0.43, 'Salmón'],
    'pez5': [0.31, 'Salmón'],
    'pez6': [0.20, 'Salmón'],
}

# Funciones para evaluar propiedades de la distancia
def no_negatividad(distancias):
    return np.all(distancias >= 0)

def reflexividad(distancias):
    return np.all(np.diag(distancias) == 0)

def simetria(distancias):
    return np.all(distancias == distancias.T)

def diferencia_triangular(distancias):
    n = distancias.shape[0]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if distancias[i, j] + distancias[j, k] < distancias[i, k]:
                    return False
    return True

# Calcular distancias
distancias = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        distancias[i, j] = calcular_distancia_euclidiana(datos[f'pez{i+1}'][0], datos[f'pez{j+1}'][0])

# Imprimir resultados
print("No Negatividad:", no_negatividad(distancias))
print("Reflexividad:", reflexividad(distancias))
print("Simetría:", simetria(distancias))
print("Diferencia Triangular:", diferencia_triangular(distancias))

# Graficar distancias
plt.figure(figsize=(10, 6))
for i in range(6):
    plt.scatter(np.ones(6) * i, distancias[i, :], marker='o', label=f'Pez{i+1}')

plt.title('Distancias Euclidianas entre Peces')
plt.xlabel('Peces')
plt.ylabel('Distancia Euclidiana')
plt.xticks(range(6), list(datos.keys()))
plt.legend()
plt.show()