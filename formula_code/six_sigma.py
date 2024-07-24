import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def calcular_grafico_control(data):
    data = np.array(data)
    mean = np.mean(data)
    std_dev = np.std(data)
    
    # Calcular los límites de control
    UCL = mean + 3 * std_dev
    LCL = mean - 3 * std_dev

    # Generar el gráfico de control
    plt.figure(figsize=(10, 6))
    plt.plot(data, marker='o', linestyle='-', color='b', label='Datos')
    plt.axhline(mean, color='green', linestyle='--', label='Media')
    plt.axhline(UCL, color='red', linestyle='--', label='Límite Superior de Control')
    plt.axhline(LCL, color='red', linestyle='--', label='Límite Inferior de Control')
    plt.xlabel('Observaciones')
    plt.ylabel('Valor')
    plt.title('Gráfico de Control')
    plt.legend()
    plt.grid(True)

    # Convertir el gráfico a imagen PNG
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return image_base64

def calcular_nivel_sigma(data):
    data = np.array(data)
    mean = np.mean(data)
    std_dev = np.std(data)
    
    # Calcular los límites de control
    UCL = mean + 3 * std_dev
    LCL = mean - 3 * std_dev

    # Calcular el nivel sigma
    sigma_level = (UCL - mean) / std_dev

    return sigma_level
