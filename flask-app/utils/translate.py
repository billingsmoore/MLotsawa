from transformers import pipeline
from  thl_phonetic_transliteration.transliterator import Transliterator

model = 'billingsmoore/phonetic-tibetan-to-english-translation'
translator = pipeline('translation', model=model, device_map='auto')

def translate(input):

    # clean input for translation
    input = input.strip()
    input_lst = input.split('\n')

    for elt in input_lst:
        if elt=='\r':
            input_lst.remove(elt)
        elt.replace('\r', '')

    # transliterate text
    transliterator = Transliterator()

    phonetic_lst = [transliterator.convert(elt) for elt in input_lst]

    # create translation
    translation_lst = translator(phonetic_lst)
    translation_lst = [elt['translation_text'] for elt in translation_lst]

    # prepare texts for display
    output_lst = []

    for i in range(len(input_lst)):
        combo = [input_lst[i], phonetic_lst[i], translation_lst[i]]
        combo = '\n'.join(combo)
        output_lst.append(combo+'\n')

    output = '\n'.join(output_lst)
    print(output)

    return output