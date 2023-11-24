import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
heartDisease=pd.read_csv('heart.csv')
heartDisease=heartDisease.replace('?',np.nan)
heart_disease=pd.DataFrame(heartDisease)
model=BayesianNetwork([('age','trestbps'),('age','fbs'),('sex','trestbps'),('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'),('heartdisease','thalach'),('heartdisease','chol')])
model.fit(heart_disease,estimator=MaximumLikelihoodEstimator)
HeartDisease_infer=VariableElimination(model)
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': int(input("enter age")), 'sex' :int(input(" num(0 or 1)"))})
print(q)