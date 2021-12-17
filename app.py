import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    

    output = "Rejected"

    return render_template('index2.html', prediction_text=output)
@app.route('/next',methods=['POST'])
def next():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
