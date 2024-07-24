function submitForm(panel) {
    if (panel === 'six_sigma') {
        const formData = new FormData(document.getElementById('six_sigma_form'));
        const analysisType = formData.get('analysis_type_six_sigma');
        const url = analysisType === 'control_chart' ? '/six_sigma/control_chart' : '/six_sigma/sigma_level';

        fetch(url, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                if (analysisType === 'control_chart') {
                    document.getElementById('six_sigma_chart').src = 'data:image/png;base64,' + data.chart;
                    document.getElementById('six_sigma_chart').style.display = 'block';
                    document.getElementById('sigma_level_result').style.display = 'none';
                } else {
                    document.getElementById('sigma_level_result').innerText = 'Nivel Sigma: ' + data.sigma_level.toFixed(2);
                    document.getElementById('sigma_level_result').style.display = 'block';
                    document.getElementById('six_sigma_chart').style.display = 'none';
                }
                document.getElementById('six_sigma_results').style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}