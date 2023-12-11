import pickle
from flask import Flask
from flask import request, jsonify, render_template

with open('model.pkl', 'rb') as model_file, open('features.pkl', 'rb') as feature_file:
  model = pickle.load(model_file)
  features = pickle.load(feature_file)

app = Flask('song-mood-predictor')

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/predict-form', methods=['POST'])
def predict_form():
  data = request.form.to_dict()
  pred = predict(data)
  return pred

@app.route('/predict-json', methods=['POST'])
def predict_json():
  data = request.form.get('jsonInput')
  pred = predict(data)
  return pred

@app.route('/predict', methods=['POST'])
def predict():
  data = request.get_json()
  pred = predict(data)
  return pred

def predict(song_features):

  missing_features = [k for k in features if k not in song_features]
  if missing_features:
    return jsonify({'Error': 'Missing features : '+str(missing_features)}), 400
  
  X_features = [[song_features[k] for k in features]]
  moods = ['sad', 'happy', 'energetic', 'calm']
  
  pred = model.predict(X_features)[0]
  prob = model.predict_proba(X_features)[0]

  mood_prob = zip(moods, prob)

  res = {}
  for i, m_prob in enumerate(mood_prob):
    res[moods[i]] = {'probability': float(m_prob[1]), 
                     'is_predicted': bool(pred == i)}
    
  return jsonify(res)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9696)
