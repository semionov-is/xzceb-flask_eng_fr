"""This is module translator to translate en-fr, fr-en"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
# os.environ OR os.env???
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-04-28',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """This is function to translate en-fr"""
    french_translate = language_translator.translate(
        text=englishText, model_id='en-fr').get_result()
    frenchText = french_translate.get("translations")[0].get("translation")
    return frenchText

def frenchToEnglish(frenchText):
    """This is function to translate fr-en"""
    english_translate = language_translator.translate(
        text=frenchText, model_id='fr-en').get_result()
    englishText = english_translate.get("translations")[0].get("translation")
    return englishText

text_p = englishToFrench('mother')
print(text_p)