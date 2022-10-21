import pandas as pd
import sys
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('news.csv')
X = df['combine_text']
y = df['is_True']

vec_train = TfidfVectorizer()
vec_train.fit(X)
X=vec_train.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1, stratify=y, random_state=0)

model = LogisticRegression()
model.fit(X_train,y_train)
predicted_value = model.predict(X_test)

pickle.dump(model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))