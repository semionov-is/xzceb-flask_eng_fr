"""This is module translator to translate en-fr, fr-en"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-04-28',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """This is function to translate en-fr"""
    french_translate = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text = french_translate.get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    """This is function to translate fr-en"""
    english_translate = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = english_translate.get("translations")[0].get("translation")
    return english_text
