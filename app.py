from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the SVM model from the pickle file
loaded_svm_model = joblib.load('best_model .pkl')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        thalach = float(request.form['thalach'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        user_input = [[age, sex, cp, trestbps, chol, thalach, fbs, restecg, exang, oldpeak, slope, ca, thal]]

        prediction = loaded_svm_model.predict(user_input)

        if prediction[0] == 1:
            result = "Based on the input, you may have heart disease."
        else:
            result = "Based on the input, you may not have heart disease."

        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
