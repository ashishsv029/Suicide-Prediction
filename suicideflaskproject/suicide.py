
#ML MODEL USING MULTI LINEAR REGRESSION

import numpy as np
import pandas as pd
import warnings
import pickle
warnings.filterwarnings("ignore")

df=pd.read_csv('suicidenote1.csv')

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score
y=df.iloc[:,8:].values
#except neropinephrine (since its correlation is very low)

x=df[['serotonin(101-283 ngm/ml)','dopamine(120-196 pmol/ltr)','cortisol(6-23) ng/ml','glutamte(50-100)umol/ltr',
      'fiveHIAA(10.5-36.6) micromol/24h']].values

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)#ytest=ypredicted data
reg=LinearRegression()
reg=reg.fit(xtrain,ytrain)
ypred=reg.predict(xtest)


pickle.dump(reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


