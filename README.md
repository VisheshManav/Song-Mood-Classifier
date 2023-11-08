# Song-Mood-Classifier
> This project is in accordance with the requirements for MLZoomcamp course's midterm project.

## Project Description
The goal of this project is to build a webservice that would take the features of spotify songs and classify the mood of the song based on four distinct emotions: happiness, sadness, calmness and energy.
The dataset for this project can be downloaded from [here](https://www.kaggle.com/datasets/abdullahorzan/moodify-dataset/data).

## The Process
The _**script.py**_ file creates two files `model.pkl, features.pkl` (.pkl extension for denoting that they were created using pickle) in the folder `./webservice` which respectively contains the model for prediction and the subset of spotify's audio features used to train the model.  
The `./webservice` folder contains:  
- test.py -> for testing if the model.pkl and features.pkl files run as intended.
- flask_script.py -> for creation of a flask app that can be used to predict given the audio features
- request.py -> for testing the deployment of flask and docker

## Run with Flask
The flask app can be run independently without docker with:
```
cd webservice  
python flask_script.py
```
and tested using request.py:
```
python request.py
```
or sending requests to `http://localhost:9696/predict`.

## Run with Docker
To run the app with docker; follow the steps mentioned:  
1. Go to the webservice directory
2. Build the image  
    ```
    docker build -t song-mood-classifier .
    ```  
3. Run
    ```
    docker run -it -p 9696:9696 song-mood-classifier:latest
    ```
    This command will run the service at `http://localhost:9696/predict`.

---