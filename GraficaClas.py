import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Datos
x = [0.75, 0.92, 0.84, 0.77, 0.84, 0.96, 0.43, 0.31, 0.2, 0.16, 0.22, 0.45]
y = [0.2, 0.3, 0.4, 0.25, 0.35, 0.32, 0.43, 0.5, 0.6, 0.7, 0.8, 0.91]
z = [1.0735, 1.3786, 1.4012, 1.1526, 1.3447, 1.4464, 0.9718, 0.153, 0.904, 0.9718, 1.1526, 1.5368]

# Crear figura 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Colores para cada vector
colors = np.arange(len(x))

# Graficar los puntos
scatter = ax.scatter(x, y, z, c=colors, cmap='viridis', marker='o', s=50)

# Configurar etiquetas de ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Añadir barra de colores
cbar = fig.colorbar(scatter)
cbar.set_label('Índice del vector')

# Mostrar el gráfico
plt.show()

