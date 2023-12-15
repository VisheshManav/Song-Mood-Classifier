import requests
# track = {'track': 'spotify:track:4V8ceSnbXYzJsO5MXEeIMP'}
track = 'spotify:track:6Ln89sczgIcAJXGAIdS94R'
result = requests.post('http://localhost:9696/predict-id', json=track)
print(result.text)