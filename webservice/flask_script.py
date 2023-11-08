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
  X_features = [[song_features[k] for k in features]]
  pred = model.predict(X_features)[0]
  moods = ['sad', 'happy', 'energetic', 'calm']
  res = {moods[i]: {
            'probability': float(prob),
            'is_predicted': bool(pred == i) 
          } 
         for i, prob in enumerate(model.predict_proba(X_features)[0])}
  return jsonify(res)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9696)
