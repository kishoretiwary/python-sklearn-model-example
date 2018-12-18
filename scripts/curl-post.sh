#!/bin/bash
curl -X POST http://predict-python-app.cfapps.io/predict --data '{ "feature_array" : [7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56,8] }' --header "Content-Type: application/json"

