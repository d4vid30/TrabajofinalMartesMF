# video 5;

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



# # Crear figura y ejes 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Rango de valores
# X = np.arange(-2, 2, 0.005)
# Y = np.arange(-2, 2, 0.005)
# X, Y = np.meshgrid(X, Y)

# # Función a graficar
# Z = np.sin(X*2) + 0.5 * np.cos(Y*2)

# # Graficar la superficie
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# # Configurar el eje Z
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # Barra de colores
# fig.colorbar(surf, shrink=0.5, aspect=5)

# # Mostrar gráfica
# plt.show()

# Codigo diferente en base al video 5:



# Crear figura y ejes

# Crear figura y ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear malla de puntos
X = np.linspace(-2, 2, 20)
Y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(X, Y)

# Función simple: Z = X + Y
Z = X + Y

# Graficar superficie
ax.plot_surface(X, Y, Z)

# Etiquetas básicas
ax.set_title("Gráfica 3D simple: Z = X + Y")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostrar gráfica
plt.show()