from flask import Flask, render_template, request, redirect, url_for, jsonify
from formula_code.cameron import calcular_cameron
from formula_code.hotelling_t2 import calcular_hotelling_t2
from formula_code.mil_std_414 import calcular_mil_std_414
from formula_code.taguchi import calcular_taguchi
from formula_code.six_sigma import calcular_grafico_control, calcular_nivel_sigma
from formula_code.control_p import calcular_carta_control_p
from formula_code.sample_size import (
    calcular_tamano_muestra_proporcion_infinita,
    calcular_tamano_muestra_proporcion_finita,
    calcular_tamano_muestra_promedios_infinita,
    calcular_tamano_muestra_promedios_finita,
    graficar_tamano_muestra,porcentaje_a_z
)
from formula_code.c_control import calcular_hotelling_t2 as control

app = Flask(__name__, static_folder='front', template_folder='front')

@app.route('/')
def login():
    return render_template('html/login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dasboar/dashboard.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "password":  # Ejemplo simple de autenticación
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

@app.route('/cameron', methods=['POST'])
def cameron():
    try:
        NCA = float(request.form['aql'])
        NCL = float(request.form['ncl'])
        alfa = float(request.form['confianza'])
        beta = float(request.form['beta'])
        
        n, chart = calcular_cameron(NCA, NCL, alfa, beta)
        return jsonify(n=n, chart=chart)
    except Exception as e:
        return jsonify(error=str(e))
@app.route('/mil_std_414', methods=['POST'])
def mil_std_414():
    try:
        N = int(request.form['lote_size'])
        k = float(request.form['desviaciones'])
        sigma = float(request.form['desviacion_estandar'])
        
        n, chart = calcular_mil_std_414(N, k, sigma)
        return jsonify(n=n, chart=chart)
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/taguchi', methods=['POST'])
def taguchi():
    try:
        factores = request.form.getlist('factores')
        niveles = [request.form.getlist(f'niveles[{i}]') for i in range(len(factores))]
        
        mean_performance, variability, chart = calcular_taguchi(factores, niveles)
        return jsonify(mean_performance=mean_performance.tolist(), variability=variability.tolist(), chart=chart)
    except Exception as e:
        return jsonify(error=str(e))
@app.route('/six_sigma/control_chart', methods=['POST'])
def six_sigma_control_chart():
    try:
        raw_data = request.form['data']
        data = list(map(float, raw_data.split(',')))
        
        chart = calcular_grafico_control(data)
        return jsonify(chart=chart)
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/six_sigma/sigma_level', methods=['POST'])
def six_sigma_sigma_level():
    try:
        raw_data = request.form['data']
        data = list(map(float, raw_data.split(',')))
        
        sigma_level = calcular_nivel_sigma(data)
        return jsonify(sigma_level=sigma_level)
    except Exception as e:
        return jsonify(error=str(e))


@app.route('/sample_size', methods=['POST'])
def sample_size():
    try:
        porcentaje = float(request.form['porcentaje'])
        Z = porcentaje_a_z(porcentaje)
        E = float(request.form['E'])
        N = request.form.get('N', None)
        p = request.form.get('p', None)
        q = request.form.get('q', None)
        sigma = request.form.get('sigma', None)
        selected_case = request.form['cases']

        if N:
            N = int(N)
        if p:
            p = float(p)
        if q:
            q = float(q)
        if sigma:
            sigma = float(sigma)

        caso = ""
        valor = None

        if selected_case == 'proporcion_infinita':
            caso = 'Proporción Infinita'
            valor = calcular_tamano_muestra_proporcion_infinita(Z, p, q, E)

        if selected_case == 'proporcion_finita' and N:
            caso = 'Proporción Finita'
            valor = calcular_tamano_muestra_proporcion_finita(Z, p, q, E, N)

        if selected_case == 'promedios_infinita' and sigma:
            caso = 'Promedios Infinita'
            valor = calcular_tamano_muestra_promedios_infinita(Z, sigma, E)

        if selected_case == 'promedios_finita' and N and sigma:
            caso = 'Promedios Finita'
            valor = calcular_tamano_muestra_promedios_finita(Z, sigma, E, N)

        chart = graficar_tamano_muestra([caso], [valor])
        return jsonify(casos=[caso], valores=[valor], chart=chart)
    except Exception as e:
        return jsonify(error=str(e))
@app.route('/multivariate_control', methods=['POST'])
def multivariate_control():
    try:
        raw_data = request.form['data']
        data = [list(map(float, obs.split(','))) for obs in raw_data.split(';')]
        
        t2_values, UCL, chart = control(data)
        return jsonify(t2_values=t2_values.tolist(), UCL=UCL, chart=chart)
    except Exception as e:
        return jsonify(error=str(e))
@app.route('/control_p', methods=['POST'])
def control_p():
    try:
        data = []
        for key in request.form.keys():
            if key.startswith('subgrupo_'):
                index = key.split('_')[1]
                subgrupo = int(request.form[f'subgrupo_{index}'])
                inspeccionado = int(request.form[f'inspeccionado_{index}'])
                no_conformidades = int(request.form[f'no_conformidades_{index}'])
                proporcion = float(request.form[f'proporcion_{index}'])
                data.append({
                    'subgrupo': subgrupo,
                    'inspeccionado': inspeccionado,
                    'no_conformidades': no_conformidades,
                    'proporcion': proporcion
                })

        p, UCL, LCL, chart = calcular_carta_control_p(data)
        return jsonify(p=p.tolist(), UCL=UCL.tolist(), LCL=LCL.tolist(), chart=chart)
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
