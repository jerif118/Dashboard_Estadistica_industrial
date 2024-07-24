import matplotlib.pyplot as plt
import numpy as np
from formula_code.plot_to import plot_to_base64
def calcular_mil_std_414(N, k, sigma):
    """
    N: Tamaño del lote
    k: Número de desviaciones estándar permitidas
    sigma: Desviación estándar de la muestra
    """
    # Ejemplo simplificado de cálculo del tamaño de muestra
    n = (k * sigma) ** 2 / N
    n = int(np.ceil(n)) 
   
    data = np.random.normal(loc=0, scale=sigma, size=n)

    # Gráfica de ejemplo
    fig, ax = plt.subplots()
    ax.plot(data, 'o-', label='Datos de la muestra')
    ax.axhline(y=np.mean(data), color='r', linestyle='--', label='Media de la muestra')
    ax.axhline(y=np.mean(data) + k * sigma, color='g', linestyle='--', label='Límite superior')
    ax.axhline(y=np.mean(data) - k * sigma, color='g', linestyle='--', label='Límite inferior')
    ax.set_title('Control de Calidad MIL STD 414')
    ax.set_xlabel('Observación')
    ax.set_ylabel('Valor')
    ax.legend()

    chart = plot_to_base64(fig)
    plt.close(fig)

    return n, chart