import pickle
import pandas as pd
import numpy as np
from sklearn import linear_model
import psutil
import os

def print_memory():
	process = psutil.Process(os.getpid())
	print("Memory used:",((process.memory_info().rss/1024)/1024))  # in bytes 

print_memory()

#loading our data as a panda
df = pd.read_csv('./winequality/winequality-white.csv', delimiter=";")

print_memory()

model_sample = [[7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56,9.4]]

#getting only the column called quality
label = df['quality']

#getting every column except for quality
features = df.drop('quality', axis=1)

print ("Training model....")

#defining our linear regression estimator and training it with our wine data
regr = linear_model.LinearRegression()
regr.fit(features, label)
print_memory()
#using our trained model to predict a fake wine
#each number represents a feature like pH, acidity, etc.
print ("Testing model with sample data ...")
print ("Prediction")
print (regr.predict(model_sample).tolist())

#serializing our model to a file called model.pkl
print ("Writing model file ...")
pickle.dump(regr, open("model.pkl","wb"),2)

#loading a model from a file called model.pkl
print("Testing saved model...")
model = pickle.load(open("model.pkl","rb"))
print (model.predict(model_sample).tolist())

print (model.coef_)



