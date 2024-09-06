from flask import Flask, render_template, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)


model = load('pipeline.joblib')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']  
    dependents = int(request.form['dependents'])
    education = request.form['education']
    self_employed = request.form['self_employed']
    income_annum = int(request.form['income_annum'])
    loan_amount = int(request.form['loan_amount'])
    loan_term = int(request.form['loan_term'])
    cibil_score = int(request.form['cibil_score'])
    residential_assets_value = int(request.form['residential_assets_value'])
    commercial_assets_value = int(request.form['commercial_assets_value'])
    luxury_assets_value = int(request.form['luxury_assets_value'])
    bank_asset_value = int(request.form['bank_asset_value'])

    education_ = 1 if education == "Graduate" else 0
    self_employed_ = 1 if self_employed == "Yes" else 0

    input_data = [[dependents, education_, self_employed_, income_annum, loan_amount, loan_term, cibil_score,
                   residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value]]

    input_array = np.array(input_data)

    prediction = model.predict(input_array)

    result_message = 'Approved' if prediction[0] == ' Approved' else 'Rejected'
    return jsonify({
        'name':name,
        'prediction': result_message,
    })

if __name__ == '__main__':
    app.run(debug=True)


