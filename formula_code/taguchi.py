import matplotlib.pyplot as plt
import numpy as np
from formula_code.plot_to import plot_to_base64
def calcular_taguchi(factores, niveles):
    # factores: lista de nombres de factores
    # niveles: lista de listas con los niveles de cada factor
    
    # Convertimos los niveles a un arreglo numpy
    niveles = np.array(niveles, dtype=float)
    
    # Calcular la media y la variabilidad del proceso
    mean_performance = np.mean(niveles, axis=1)
    variability = np.var(niveles, axis=1)
    
    # Gráfica de ejemplo
    fig, ax = plt.subplots()
    for i, factor in enumerate(factores):
        ax.plot(niveles[i], 'o-', label=factor)
    ax.legend()
    ax.set_title('Optimización Taguchi')
    ax.set_xlabel('Nivel')
    ax.set_ylabel('Rendimiento')
    
    chart = plot_to_base64(fig)
    plt.close(fig)
    
    return mean_performance, variability, chart