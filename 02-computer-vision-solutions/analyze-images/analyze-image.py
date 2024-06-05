from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
import sys
from matplotlib import pyplot as plt
from azure.core.exceptions import HttpResponseError
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import requests
from io import BytesIO

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        if not ai_endpoint or not ai_key:
            print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
            return

        # Get current script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Get image
        image_file = os.path.join(script_dir, 'images', 'street.jpg')
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        # Check if the file exists
        if not os.path.isfile(image_file):
            print(f"Error: File '{image_file}' does not exist.")
            return

        with open(image_file, "rb") as f:
            image_data = f.read()

        # Authenticate Azure AI Vision client
        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )
        
        # Analyze image
        AnalyzeImage(image_data, cv_client)
        
        # Background removal
        BackgroundForeground(ai_endpoint, ai_key, image_file)

    except Exception as ex:
        print(ex)


def AnalyzeImage(image_data, cv_client):
    print('\nAnalyzing image...')

    try:
        # Analyze image
        result = cv_client.analyze(
            image_data=image_data,
            visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS, VisualFeatures.OBJECTS],
            gender_neutral_caption=True
        )
        
        # Display analysis results
        print("Image analysis results:")
        if result.caption:
            print(" Caption:")
            print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")
        else:
            print("No caption found.")
        if result.tags:
            print(" Tags:")
            for tag in result.tags:
                print(f"- {tag.name} (confidence: {tag.confidence})")
        else:
            print("No tags found.")
        if result.objects:
            print(" Objects:")
            for obj in result.objects:
                print(f"- {obj.object_property} (confidence: {obj.confidence})")
        else:
            print("No objects found.")

    except HttpResponseError as e:
        print(f"Status code: {e.status_code}")
        print(f"Reason: {e.reason}")
        print(f"Message: {e.error.message}")


def BackgroundForeground(endpoint, key, image_file):
    # Define the API version and mode
    api_version = "2023-02-01-preview"
    mode = "backgroundRemoval" # Can be "foregroundMatting" or "backgroundRemoval"
    
    url = f"{endpoint}/vision/v3.2/analyze?api-version={api_version}&mode={mode}"
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/octet-stream"
    }

    with open(image_file, "rb") as f:
        image_data = f.read()

    response = requests.post(url, headers=headers, data=image_data)
    
    if response.status_code == 200:
        # Open the image using Pillow and process the result
        result_image = Image.open(BytesIO(response.content))
        result_image.save("background_removed.png")
        print("Background removed and saved as background_removed.png")
    else:
        print(f"Failed to remove background: {response.status_code}")
        print(response.json())


if __name__ == "__main__":
    main()
