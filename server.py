# final_project/server.py

from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload
    myobj = {"raw_document": {"text": text_to_analyse}}
    
    # Custom header specifying the model ID
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)
    
    # Parsing the JSON response
    formatted_response = json.loads(response.text)
    
    # Extract the emotion predictions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Add dominant emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions

# Flask route with the required decorator name
@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    # Get the statement from query parameter
    statement = request.args.get("text")
    
    if not statement:
        return jsonify({"error": "Please provide a text query parameter"}), 400
    
    # Run the detector
    result = emotion_detector(statement)
    
    # Build the formatted response string
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    return response_str

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
