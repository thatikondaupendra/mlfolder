import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork,BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
heartDisease=pd.read_csv("heart.csv")
heartDisease = heartDisease.replace('?', np.nan)
heart_disease=pd.DataFrame(heartDisease)
print(heart_disease)

from pgmpy.models import BayesianModel
model = BayesianNetwork([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'),('heartdisease','thalach'), ('heartdisease','chol')])
from pgmpy.estimators import MaximumLikelihoodEstimator
model.fit(heart_disease,estimator=MaximumLikelihoodEstimator)

from pgmpy.inference import VariableElimination
HeartDisease_infer=VariableElimination(model)
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': int(input("enter age")), 'sex' :int(input("enter num(0 or 1)"))})

print(q)



