import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload
    myobj = {"raw_document": {"text": text_to_analyse}}
    
    # Custom header specifying the model ID
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)
    
    # Handle blank input (status_code = 400)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    # Normal case: parse the JSON response
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Add dominant emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
