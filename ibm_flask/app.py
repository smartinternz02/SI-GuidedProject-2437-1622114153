# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:01:20 2021

@author: Shashi
"""

import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "uNr88BL0JpijM3jctcb3PSNjemYI4EczZx1aCiXVNjeW"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ["Cement","Blast Furnace Slag","FlyAsh","Water","Superplasticizer","CoarseAggregate","FineAggregate","Age"] , "values": [[540,0, 0, 162, 2.5, 1055, 676, 28]]}]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3b72b8be-bdad-418b-8aa8-72815f584709/predictions?version=2021-06-04', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions = response_scoring.json()
print(predictions['predictions'][0]['values'][0])