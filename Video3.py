#EJERCICIO1/VIDEO3
import numpy as np
import matplotlib.pyplot as plt

# def PILeibniz(N):
#     suma=0.0
#     if N!=0.0:
#         for i in range(N):
#             suma=suma+ ((-1)**i)/(2.0*i+1.0)
#             return 4.0*suma
#         else:
#             return 1.0
        
# def PIWallis(N):
#     prod=1.0
#     for i in range(1, N+1):
#         prod=prod*((2.0*i)/(2.0*i-1.0))*((2.0*i)/(2.0*i+1))

#     return 2.0*prod

# listaN=np.linspace(1, 1000, 1000, dtype=(int))
# listaLeibniz=[]
# listaWallis=[]

# for i in listaN:
#     listaLeibniz.append(PILeibniz(i))
#     listaWallis.append(PIWallis(i))

# plt.plot(listaN, listaLeibniz, "o-", label="Leibniz")
# plt.plot(listaN, listaWallis, "o-", label="Wallis")

# plt.xlabel("N")
# plt.ylabel("Valor de pi")
# plt.grid(ls="dashed")

# plt.legend()
# plt.show()


#EJERCICIO2/VIDEO3


def PILeibniz(N):
    suma = 0.0
    for i in range(N):
        suma += ((-1)**i) / (2*i + 1)
    return 4*suma

def PIWallis(N):
    prod = 1.0
    for i in range(1, N+1):
        prod *= (2*i / (2*i - 1)) * (2*i / (2*i + 1))
    return 2*prod

Nvals = np.arange(1, 1001)
pi_leib = [PILeibniz(N) for N in Nvals]
pi_wallis = [PIWallis(N) for N in Nvals]

plt.plot(Nvals, pi_leib, label="Leibniz")
plt.plot(Nvals, pi_wallis, label="Wallis")
plt.axhline(np.pi, color='gray', linestyle='--', label="π real")

plt.xlabel("N")
plt.ylabel("Valor de π")
plt.legend()
plt.grid(True, linestyle="--")
plt.show()