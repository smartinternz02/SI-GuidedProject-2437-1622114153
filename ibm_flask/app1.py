# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:07:43 2021

@author: Shashi
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd

import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "uNr88BL0JpijM3jctcb3PSNjemYI4EczZx1aCiXVNjeW"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line   
app = Flask(__name__) # initializing a flask app

@app.route('/')# route to display the home page
def home():
    return render_template('home.html') #rendering the home page
@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('index1.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')
@app.route('/predict',methods=['POST']) # route to show the predictions in a web UI

def index():
    cement = request.form["Cement"]
    slag = request.form["Blast Furnace Slag"]
    ash = request.form["Fly Ash"]
    water = request.form["Water"]
    plast = request.form["Superplasticizer"]
    ca = request.form["Coarse Aggregate"]
    fa = request.form["Fine Aggregate"]
    age = request.form["Age"]
    
    t = [[float(cement),float(slag),float(ash),float(water),float(plast),float(ca),float(fa),int(age)]]
   
    payload_scoring = {"input_data": [{"field": ["Cement","Blast Furnace Slag","Fly Ash","Water","Superplasticizer","Coarse Aggregate","Fine Aggregate","Age"] , "values": t }]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3b72b8be-bdad-418b-8aa8-72815f584709/predictions?version=2021-06-04', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    predictions = response_scoring.json()
    print(predictions['predictions'][0]['values'][0])
    prediction = predictions['predictions'][0]['values'][0]
    # showing the prediction results in a UI
    return render_template('result2.html',prediction_text=prediction)

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    #app.run(debug=False) # running the app
    app.run(debug=True) #local host 8080