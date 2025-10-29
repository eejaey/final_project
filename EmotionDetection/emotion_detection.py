import requests
import json

def emotion_detector(text_to_analyse):     
    # URL of the emotion detection service     
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'     
    # Constructing the request payload in the expected format     
    myobj = { "raw_document": { "text": text_to_analyse } }     
    # Custom header specifying the model ID for the emotion detection service     
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}     
    # Sending a POST request to the emotion detection API     
    response = requests.post(url, json=myobj, headers=header)     
    # Parsing the JSON response from the API     
    formatted_response = json.loads(response.text)    
     # Extract the emotion predictions     
    emotions = formatted_response['emotionPredictions'][0]['emotion']         
     # Find the emotion with the highest score     
    highest_emotion = max(emotions, key=emotions.get)          
    # Return the emotion with the highest score    
    return highest_emotion 