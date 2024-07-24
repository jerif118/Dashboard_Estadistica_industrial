import numpy as np
from formula_code.plot_to import plot_to_base64
import matplotlib.pyplot as plt
import scipy.stats as stats

def porcentaje_a_z(porcentaje):
    return stats.norm.ppf(1 - (1 - porcentaje / 100) / 2)

def calcular_tamano_muestra_proporcion_infinita(Z, p, q, E):
    n = (Z ** 2 * p * q) / (E ** 2)
    n = int(np.ceil(n))
    return n

def calcular_tamano_muestra_proporcion_finita(Z, p, q, E, N):
    n = (N * Z ** 2 * p * q) / ((N - 1) * E ** 2 + Z ** 2 * p * q)
    n = int(np.ceil(n))
    return n

def calcular_tamano_muestra_promedios_infinita(Z, sigma, E):
    n = (Z ** 2 * sigma ** 2) / (E ** 2)
    n = int(np.ceil(n))
    return n

def calcular_tamano_muestra_promedios_finita(Z, sigma, E, N):
    n = (N * Z ** 2 * sigma ** 2) / ((N - 1) * E ** 2 + Z ** 2 * sigma ** 2)
    n = int(np.ceil(n))
    return n

def graficar_tamano_muestra(casos, valores):
    fig, ax = plt.subplots()
    ax.bar(casos, valores)
    ax.set_title('Determinación del Tamaño de Muestra')
    ax.set_ylabel('Tamaño de Muestra')

    chart = plot_to_base64(fig)
    plt.close(fig)

    return chart
