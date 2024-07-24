import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import io
import base64

def calcular_hotelling_t2(data):
    # Convertir los datos a un array numpy
    data = np.array(data)
    
    # Calcular el vector de medias
    mean_vector = np.mean(data, axis=0)
    
    # Calcular la matriz de covarianza
    covariance_matrix = np.cov(data, rowvar=False)
    
    # Invertir la matriz de covarianza
    inv_covariance_matrix = np.linalg.inv(covariance_matrix)
    
    # Calcular el número de muestras y el número de variables
    n, p = data.shape
    
    # Calcular los valores T²
    t2_values = np.array([
        np.dot(np.dot((obs - mean_vector).T, inv_covariance_matrix), (obs - mean_vector))
        for obs in data
    ])
    
    # Calcular el límite de control superior (UCL)
    F_crit = stats.f.ppf(q=0.95, dfn=p, dfd=n-p)
    UCL = (p * (n + 1) * (n - 1) / (n * (n - p))) * F_crit
    
    # Graficar los valores T²
    fig, ax = plt.subplots()
    ax.plot(t2_values, marker='o', linestyle='-', color='b')
    ax.axhline(y=UCL, color='r', linestyle='--')
    ax.set_title('Hotelling T² Chart')
    ax.set_xlabel('Observation')
    ax.set_ylabel('T² Value')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    
    return t2_values, UCL, img_base64
