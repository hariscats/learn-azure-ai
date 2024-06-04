from dotenv import load_dotenv
import os
import http.client
import json
import urllib
from urllib import request, parse, error

def load_configuration():
    """Load configuration from .env file"""
    load_dotenv()
    ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
    ai_key = os.getenv('AI_SERVICE_KEY')
    if not ai_endpoint or not ai_key:
        raise ValueError("AI_SERVICE_ENDPOINT and AI_SERVICE_KEY must be set in the .env file")
    return ai_endpoint, ai_key

def get_language(text, ai_endpoint, ai_key):
    """Get the detected language for the provided text"""
    try:
        # Construct the JSON request body
        json_body = {
            "documents": [{"id": 1, "text": text}]
        }

        # Make an HTTP request to the REST interface
        uri = ai_endpoint.rstrip('/').replace('https://', '')
        conn = http.client.HTTPSConnection(uri)

        # Add the authentication key to the request header
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': ai_key
        }

        # Use the Text Analytics language API
        conn.request("POST", "/text/analytics/v3.1/languages?", json.dumps(json_body), headers)

        # Send the request
        response = conn.getresponse()
        data = response.read().decode("UTF-8")

        # Handle the response
        if response.status == 200:
            results = json.loads(data)
            print(json.dumps(results, indent=2))
            for document in results["documents"]:
                print("\nLanguage:", document["detectedLanguage"]["name"])
        else:
            print(f"Error: {response.status} - {response.reason}")
            print(data)

        conn.close()

    except Exception as ex:
        print(f"An error occurred: {ex}")

def main():
    try:
        ai_endpoint, ai_key = load_configuration()

        while True:
            user_text = input('Enter some text ("quit" to stop, "batch" for batch processing):\n')
            if user_text.lower() == 'quit':
                break
            elif user_text.lower() == 'batch':
                batch_texts = []
                print("Enter texts for batch processing (empty line to end):")
                while True:
                    text = input()
                    if text == '':
                        break
                    batch_texts.append(text)
                for text in batch_texts:
                    get_language(text, ai_endpoint, ai_key)
            else:
                get_language(user_text, ai_endpoint, ai_key)

    except Exception as ex:
        print(f"An error occurred during setup: {ex}")

if __name__ == "__main__":
    main()
