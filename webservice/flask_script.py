import pickle
from flask import Flask
from flask import request, jsonify

with open('model.pkl', 'rb') as model_file, open('features.pkl', 'rb') as feature_file:
  model = pickle.load(model_file)
  features = pickle.load(feature_file)

app = Flask('song-mood-predictor')

@app.route('/predict', methods=['POST'])
def predict():
  song_features = request.get_json()

  has_features = all([k in song_features for k in features])
  if not has_features:
    return jsonify({'Error': 'Missing features\nFeatures needed are: '+features}), 400
  
  X_features = [[song_features[k] for k in features]]
  moods = ['sad', 'happy', 'energetic', 'calm']
  
  pred = model.predict(X_features)[0]
  prob = model.predict_proba(X_features)[0]

  mood_prob = zip(moods, prob)
  sorted_mood_prob = sorted(mood_prob, key=lambda x: x[1])

  res = {}
  for i, m_prob in enumerate(sorted_mood_prob):
    res[moods[i]] = {'probability': float(m_prob[1]), 
                     'is_predicted': bool(pred == i)}
    
  return jsonify(res)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9696)
