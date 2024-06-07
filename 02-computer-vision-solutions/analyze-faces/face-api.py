from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

def main():
    global face_client

    try:
        # Get Configuration Settings
        load_dotenv()
        cog_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        cog_key = os.getenv('AI_SERVICE_KEY')

        # Authenticate Face client
        face_client = FaceClient(cog_endpoint, CognitiveServicesCredentials(cog_key))

        # Menu for face functions
        print('1: Detect faces\nAny other key to quit')
        command = input('Enter a number:')
        if command == '1':
            DetectFaces(os.path.join('images', 'people.jpg'))

    except Exception as ex:
        print(ex)

def DetectFaces(image_file):
    print('Detecting faces in', image_file)

    # Specify facial features to be retrieved
    face_attributes = ['age', 'gender', 'emotion']

    # Open image
    image = open(image_file, 'rb')

    # Get faces
    detected_faces = face_client.face.detect_with_stream(image, return_face_attributes=face_attributes)

    if not detected_faces:
        print('No faces detected.')
        return

    # Display results
    print('Detected faces:')
    for face in detected_faces:
        print(f'Face ID: {face.face_id}')
        print(f' - Age: {face.face_attributes.age}')
        print(f' - Gender: {face.face_attributes.gender}')
        print(f' - Emotion: {face.face_attributes.emotion}')

if __name__ == "__main__":
    main()
