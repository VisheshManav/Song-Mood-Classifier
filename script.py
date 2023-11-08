import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
import pickle

df = pd.read_csv('./dataset/278k_song_labelled.csv')
y = df['labels'].values
df.drop('labels', axis=1, inplace=True)
X = df.iloc[:, 1:] # remove the id column

X_fulltrain, X_test, y_fulltrain, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_fulltrain.reset_index(drop=True, inplace=True)
X_test.reset_index(drop=True, inplace=True)

features_selected = X_fulltrain.columns.drop(['duration (ms)', 'spec_rate', 'tempo', 'liveness']).values

X_fulltrain = X_fulltrain[features_selected].values
X_test = X_test[features_selected].values

dt = DecisionTreeClassifier(min_samples_leaf=23, max_depth=11, random_state=42)
dt.fit(X_fulltrain, y_fulltrain)
y_pred = dt.predict(X_test)
print(f1_score(y_test, y_pred, average='weighted'))

with open('./webservice/model.pkl', 'wb') as model_file:
  pickle.dump(dt, model_file)
with open('./webservice/features.pkl', 'wb') as feature_file:
  pickle.dump(features_selected, feature_file)