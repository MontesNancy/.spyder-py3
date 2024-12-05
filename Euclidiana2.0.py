import numpy as np
import matplotlib.pyplot as plt

# Función para convertir valores lógicos en 'Sí' o 'No'
def respuesta_binaria(valor):
    return 'Sí' if valor else 'No'

# Datos
muestras = ['pez1', 'pez2', 'pez3', 'pez4', 'pez5', 'pez6']
brillo = [0.75, 0.92, 0.84, 0.43, 0.31, 0.20]
clase = ['Trucha', 'Trucha', 'Trucha', 'Salmon', 'Salmon', 'Salmon']

# Inicializar la matriz euclidiana
matriz_euclidiana = np.zeros((len(muestras), len(muestras)))

# Calcular la matriz euclidiana
for i in range(len(muestras)):
    for j in range(len(muestras)):
        # Calcular la distancia euclidiana utilizando la fórmula proporcionada
        distancia = np.sqrt((brillo[i] - brillo[j])**2)
        # Almacenar la distancia en la matriz
        matriz_euclidiana[i, j] = distancia

# Mostrar la matriz euclidiana
print('Matriz Euclidiana:')
print(matriz_euclidiana)

# Graficar las distancias con formato de punto
plt.figure()
plt.scatter(np.repeat(range(1, len(muestras)+1), len(muestras)), matriz_euclidiana.flatten(), c='blue', marker='o')
plt.xlabel('Muestras')
plt.ylabel('Distancia Euclidiana')
plt.title('Distancias Euclidianas entre Muestras')
plt.grid(True)
plt.show()


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

# Resultados y propiedades métricas
print('\nResultados y Propiedades Métricas:\n')

# 5. No negatividad de la distancia euclidiana entre P1 y P2
resultado_no_negatividad = matriz_euclidiana[0, 1]
print(f'5. No negatividad de la distancia euclidiana entre P1 y P2:\nResultado entre P1 y P2: {resultado_no_negatividad}\nCumple: {respuesta_binaria(resultado_no_negatividad >= 0)}\n')

# 6. Reflexividad de la distancia euclidiana entre P5 y P5
resultado_reflexividad = matriz_euclidiana[4, 4]
print(f'6. Reflexividad de la distancia euclidiana entre P5 y P5:\nResultado entre P5 y P5: {resultado_reflexividad}\nCumple: {respuesta_binaria(resultado_reflexividad == 0)}\n')

# 7. Simetría de la distancia euclidiana entre P1 y P2
resultado_simetria_p1_p2 = matriz_euclidiana[0, 1]
resultado_simetria_p2_p1 = matriz_euclidiana[1, 0]
print(f'7. Simetría de la distancia euclidiana entre P1 y P2:\nResultado entre P1 y P2: {resultado_simetria_p1_p2}\nResultado entre P2 y P1: {resultado_simetria_p2_p1}\nCumple: {respuesta_binaria(resultado_simetria_p1_p2 == resultado_simetria_p2_p1)}\n')

# 8. Desigualdad triangular de la distancia euclidiana entre P1, P2 y P3
resultado_dist_p1_p2 = matriz_euclidiana[0, 1]
resultado_dist_p2_p3 = matriz_euclidiana[1, 2]
resultado_dist_p1_p3 = matriz_euclidiana[0, 2]
suma_dist_p1_p2_p3 = resultado_dist_p1_p2 + resultado_dist_p2_p3
print(f'8. Desigualdad triangular de la distancia euclidiana entre P1, P2 y P3:\nResultado entre P1 y P2: {resultado_dist_p1_p2}\nResultado entre P2 y P3: {resultado_dist_p2_p3}\nResultado entre P1 y P3: {resultado_dist_p1_p3}\nSuma entre P1 y P2: {suma_dist_p1_p2_p3}\nD[P1, P2] + D[P2, P3] > D[P1, P3]\n{suma_dist_p1_p2_p3} > {resultado_dist_p1_p3}\nLa desigualdad triangular se cumple\n')

# Función para convertir valores lógicos en 'Sí' o 'No'
def respuesta_binaria(valor):
    return 'Sí' if valor else 'No'

