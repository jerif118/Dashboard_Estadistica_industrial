import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def calcular_carta_control_p(data):
    n = np.array([item['inspeccionado'] for item in data])
    d = np.array([item['no_conformidades'] for item in data])
    p = np.array([item['proporcion'] for item in data])
    
    p_bar = np.sum(d) / np.sum(n)
    UCL = p_bar + 3 * np.sqrt((p_bar * (1 - p_bar)) / n)
    LCL = p_bar - 3 * np.sqrt((p_bar * (1 - p_bar)) / n)
    LCL = np.where(LCL < 0, 0, LCL)  # LCL cannot be negative

    # Plotting the control chart
    plt.figure(figsize=(10, 6))
    plt.plot(p, marker='o', linestyle='-', color='b', label='Proporción de No-conformidades')
    plt.axhline(p_bar, color='green', linestyle='--', label='Límite Central')
    plt.plot(UCL, color='red', linestyle='--', label='Límite Superior de Control')
    plt.plot(LCL, color='red', linestyle='--', label='Límite Inferior de Control')
    plt.xlabel('Número de Subgrupo')
    plt.ylabel('Proporción de No-conformidades')
    plt.title('Carta de Control p')
    plt.legend()
    plt.grid(True)

    # Convert plot to PNG image
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return p, UCL, LCL, image_base64
