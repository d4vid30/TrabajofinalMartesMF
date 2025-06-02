# video 6:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score

# Simular un DataFrame de ejemplo
Datos = pd.DataFrame({
    "Altura": [150, 160, 165, 170, 175, 180, 185],
    "Peso": [50, 55, 60, 65, 70, 75, 80]
})

# Convertir a arrays y reformatear
x = Datos["Altura"].to_numpy().reshape(-1, 1)
y = Datos["Peso"].to_numpy().reshape(-1, 1)

# Crear y entrenar modelo de regresión lineal
regr = linear_model.LinearRegression()
regr.fit(x, y)

# Mostrar la ecuación de la recta
print(f"La recta es: y = {regr.coef_[0][0]:.2f}x + {regr.intercept_[0]:.2f}")

# Graficar puntos y línea de regresión
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, regr.predict(x), color='red', label='Regresión lineal')
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.title("Relación Altura vs Peso")
plt.legend()
plt.grid(True)
plt.show()

# Mostrar R²
print("R^2:", r2_score(y, regr.predict(x)))

# codigo en base video 6:

# Ejemplo sencillo de regresión lineal en Python

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # 1. Definimos datos de ejemplo:
# #    X: variable independiente (por ejemplo, número de horas de estudio)
# #    y: variable dependiente (por ejemplo, puntaje obtenido)
# X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# y = np.array([2, 3, 5, 4, 6])

# # 2. Creamos y entrenamos el modelo de regresión lineal
# model = LinearRegression()
# model.fit(X, y)

# # 3. Obtenemos coeficiente (pendiente) y ordenada al origen (intercepto)
# pendiente = model.coef_[0]
# intercepto = model.intercept_
# print(f"Ecuación de la recta: y = {pendiente:.2f}·x + {intercepto:.2f}")

# # 4. Graficamos los puntos originales y la línea ajustada
# plt.scatter(X, y, color='blue', label='Datos reales')
# plt.plot(X, model.predict(X), color='red', label='Recta ajustada')
# plt.xlabel("X (Horas de estudio)")
# plt.ylabel("y (Puntaje)")
# plt.title("Regresión Lineal Sencilla")
# plt.legend()
# plt.show()