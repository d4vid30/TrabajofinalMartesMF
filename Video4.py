#EJERCICIO/VIDEO4

import matplotlib.pyplot as plt
import numpy as np

# X=np.linspace(0, 2*np.pi, 100)
# Y=np.sin(X)
# Y2=np.cos(X)
# Y3=Y+Y2
# Y4=(np.sin(X))**2

# plt.subplot(2,2,1)

# plt.plot(X,Y, color="red", label="$\sin x$")
# plt.title("Funciones Trigonometricas")
# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.grid(ls="dashed")
# plt.legend()

# plt.subplot(2,2,2)
# plt.plot(X,Y2, color="blue", label="$\cos x$")

# plt.title("Funciones Trigonometricas")
# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.grid(ls="dashed")
# plt.legend()

# plt.subplot(2,2,3)
# plt.plot(X,Y3, color="cyan", label="$\sin + \cos x$")

# plt.title("Funciones Trigonometricas")
# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.grid(ls="dashed")
# plt.legend()

# plt.subplot(2,2,4)
# plt.plot(X,Y4, color="magenta", label="$\sin^2 x$")

# plt.title("Funciones Trigonometricas")
# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.grid(ls="dashed")
# plt.legend()
# plt.show()

#EJERCICIO2/VIDEO4

# Datos
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Crear figura con 1 fila y 2 columnas
plt.figure(figsize=(10, 4))

# Primera subgráfica: seno
plt.subplot(1, 2, 1)
plt.plot(x, y_sin, color='green', label='$\sin x$')
plt.title("Seno")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid(True)
plt.legend()

# Segunda subgráfica: coseno
plt.subplot(1, 2, 2)
plt.plot(x, y_cos, color='orange', label='$\cos x$')
plt.title("Coseno")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid(True)
plt.legend()

# Mostrar la figura
plt.tight_layout()
plt.show()