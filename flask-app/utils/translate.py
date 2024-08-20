from transformers import pipeline

model = 'billingsmoore/mlotsawa'
translator = pipeline('translation', model=model)

def translate(input):

    # clean input for translation
    input = input.strip()
    input = input.split('\n')

    # create translation
    translation = translator(input)

    # clean translation for display
    translation = [elt['translation_text'] for elt in translation]
    translation = '\n'.join(translation)

    return translation