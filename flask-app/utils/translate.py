from transformers import pipeline
from  thl_phonetic_transliteration.converter import convert

model = 'billingsmoore/mlotsawa'
translator = pipeline('translation', model=model, device_map='auto')

def translate(input):

    # transliterate text
    input = convert(input)
    
    # clean input for translation
    input = input.strip()
    input = input.split('\n')

    # create translation
    translation = translator(input)

    # clean translation for display
    translation = [elt['translation_text'] for elt in translation]
    translation = '\n'.join(translation)

    return translation