!#/bin/bash
ab -p body.json -T application/json -c 10 -n 1000 http://predict-python-app.cfapps.io/predict
