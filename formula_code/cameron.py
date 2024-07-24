import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from formula_code.plot_to import plot_to_base64
def calcular_cameron(NCA, NCL, alfa, beta):
    z_alpha = stats.norm.ppf(1 - alfa / 2)
    z_beta = stats.norm.ppf(1 - beta)

    p1 = NCA / 100
    p2 = NCL / 100

    n = ((z_alpha * np.sqrt(p1 * (1 - p1)) + z_beta * np.sqrt(p2 * (1 - p2))) ** 2) / ((p2 - p1) ** 2)
    n = int(np.ceil(n))

    # Gráfica de ejemplo
    fig, ax = plt.subplots()
    ax.bar(['Tamaño de muestra'], [n])
    ax.set_title('Plan de Muestreo (Cameron)')
    ax.set_ylabel('Tamaño de Muestra')

    chart = plot_to_base64(fig)
    plt.close(fig)

    return n, chart