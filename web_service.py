from flask import Flask, render_template, request
from src.model import predict_model

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        experience = request.form.get("experience")
        result = predict_model(experience)
    else:
        result = ""
        experience = ""
    return render_template('index.html', res = result, exp = experience)
    
@app.route('/experience', methods = ['POST'])
def exp_json():
    input_json = request.get_json(force=True)
    result = predict_model(input_json["experience"])
    return str(result[0])    

if __name__ == "__main__":
    app.run(debug=True)