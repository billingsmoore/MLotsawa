from  mlotsawa.transliterator import Transliterator
from mlotsawa.translator import Translator

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
    translator = Translator()

    phonetic_lst = transliterator.transliterate(input_lst)

    # create translation
    translation_lst = translator.translate(input_lst)

    # prepare texts for display
    output_lst = []

    for i in range(len(input_lst)):
        combo = [input_lst[i], phonetic_lst[i], translation_lst[i]]
        combo = '\n'.join(combo)
        output_lst.append(combo+'\n')

    output = '\n'.join(output_lst)

    return output