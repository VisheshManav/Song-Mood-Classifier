import pickle

with open('model.pkl', 'rb') as model_file:
  model = pickle.load(model_file)
with open('features.pkl', 'rb') as feature_file:
  features = pickle.load(feature_file)

X = {'Unnamed: 0': 119145.0,
 'duration (ms)': 240400.0,
 'danceability': 0.715,
 'energy': 0.653,
 'loudness': -7.031,
 'speechiness': 0.0403,
 'acousticness': 0.211,
 'instrumentalness': 0.0,
 'liveness': 0.148,
 'valence': 0.586,
 'tempo': 129.982,
 'spec_rate': 1.6763727121464226e-07
}
X_features = [[X[k] for k in features]]
moods = ['sad', 'happy', 'energetic', 'calm']
for i, prob in enumerate(model.predict_proba(X_features)[0]):
  print(f'{moods[i]:10s} -> {prob}')
