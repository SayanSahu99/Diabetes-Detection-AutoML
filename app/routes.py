from app import app
from flask import render_template, request
from app.detect import detect_diabetes

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_file():
  if request.method == 'POST':
    # Request data goes here
    data = {
        "data": [
            {
            "Pregnancies": int(request.form.get('Pregnencies')),
            "Glucose": int(request.form.get('Glucose')),
            "BloodPressure": int(request.form.get('BloodPressure')),
            "SkinThickness": int(request.form.get('SkinThickness')),
            "Insulin": int(request.form.get('Insulin')),
            "BMI": int(request.form.get('BMI')),
            "DiabetesPedigreeFunction": int(request.form.get('DiabetesPedigree')),
            "Age": int(request.form.get('Age'))
            }
        ],
        "method": "predict"
    }
    result = detect_diabetes(data)
    result = detect_diabetes(data).decode("UTF-8")[-4]
    if(result == '1'):
        return render_template('positive.html')
    else:
        return render_template('negative.html')

