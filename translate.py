import re
from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

def translateTo(source, lanCode):
    try:
        translation = translator.translate(source, dest=lanCode)
        return f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
    except:
        return 'Fehler'

def Languages():
    StringRet = str(f"Total supported languages: {len(constants.LANGUAGES)} \nLanguages: \n")
    for x in constants.LANGUAGES:
        StringRet += f'{x} : {constants.LANGUAGES[x]} \n'
    return StringRet
