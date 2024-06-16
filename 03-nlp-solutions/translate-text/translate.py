from azure.ai.translation.text import *
from azure.ai.translation.text.models import InputTextItem
import os
from dotenv import load_dotenv

def create_client(key, region):
    try:
        credential = TranslatorCredential(key, region)
        client = TextTranslationClient(credential)
        return client
    except Exception as e:
        print("Error creating client:", e)
        return None

def get_supported_languages(client):
    try:
        languages_response = client.get_languages(scope="translation")
        return languages_response.translation
    except Exception as e:
        print("Error fetching languages:", e)
        return None

def choose_target_language(supported_languages):
    print("{} languages supported.".format(len(supported_languages)))
    print("(See https://learn.microsoft.com/azure/ai-services/translator/language-support#translation)")
    print("Enter a target language code for translation (for example, 'en'):")

    while True:
        target_language = input()
        if target_language in supported_languages.keys():
            return target_language
        else:
            print("{} is not a supported language.".format(target_language))

def translate_text(client, target_language):
    input_text = ""
    while input_text.lower() != "quit":
        input_text = input("Enter text to translate ('quit' to exit):")
        if input_text.lower() != "quit":
            try:
                input_text_elements = [InputTextItem(text=input_text)]
                translation_response = client.translate(content=input_text_elements, to=[target_language])
                translation = translation_response[0] if translation_response else None
                if translation:
                    source_language = translation.detected_language
                    for translated_text in translation.translations:
                        print(f"'{input_text}' was translated from {source_language.language} to {translated_text.to} as '{translated_text.text}'.")
            except Exception as e:
                print("Error translating text:", e)

def main():
    # Load environment variables from .env file
    load_dotenv()
    translatorKey = os.getenv("TRANSLATOR_KEY")
    translatorRegion = os.getenv("TRANSLATOR_REGION")

    if not translatorKey or not translatorRegion:
        print("Please set the TRANSLATOR_KEY and TRANSLATOR_REGION environment variables in the .env file.")
        return

    client = create_client(translatorKey, translatorRegion)
    if client:
        supported_languages = get_supported_languages(client)
        if supported_languages:
            target_language = choose_target_language(supported_languages)
            translate_text(client, target_language)

if __name__ == "__main__":
    main()
