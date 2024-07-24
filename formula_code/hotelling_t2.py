import matplotlib.pyplot as plt
import numpy as np
from formula_code.plot_to import plot_to_base64
def calcular_hotelling_t2(data):
    data = np.array(data)
    mean_vector = np.mean(data, axis=0)
    cov_matrix = np.cov(data, rowvar=False)
    inv_cov_matrix = np.linalg.inv(cov_matrix)
    t2_values = []

    for obs in data:
        diff = obs - mean_vector
        t2 = np.dot(np.dot(diff, inv_cov_matrix), diff.T)
        t2_values.append(t2)

    t2_values = np.array(t2_values)
    UCL = np.percentile(t2_values, 95)  # Control Limit at 95% confidence

    # Gráfica T² de Hotelling
    fig, ax = plt.subplots()
    ax.plot(t2_values, marker='o')
    ax.axhline(y=UCL, color='r', linestyle='--', label='Límite de Control (95%)')
    ax.set_title('Carta de Control T² de Hotelling')
    ax.set_xlabel('Observación')
    ax.set_ylabel('T²')
    ax.legend()

    chart = plot_to_base64(fig)
    plt.close(fig)

    return t2_values, UCL, chart