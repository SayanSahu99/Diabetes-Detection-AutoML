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
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)