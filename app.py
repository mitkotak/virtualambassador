from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get('/')
def get_index():
    return render_template("base.html")

@app.post('/predict')
def predict():
    text = request.get_json().get("message")
    #TODO check message vaild
    response = get_response(text)
    message = {"answer" : response}
    return jsonify(message)
    

