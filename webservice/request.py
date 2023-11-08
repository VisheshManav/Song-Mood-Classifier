import requests

song_features = {'Unnamed: 0': 119145.0,
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

response = requests.post('http://localhost:9696/predict', json=song_features)
for k, v in response.json().items():
  print(f'{k:10s} -> {v}')