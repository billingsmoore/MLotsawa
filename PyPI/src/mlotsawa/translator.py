from transformers import pipeline

class Translator():

    def __init__(self):
        self.pipe = pipeline('translation', model='billingsmoore/tibetan-to-english-translation', device_map='auto')

    def translate(self, input_text):
        """
        This function takes in a string and translates it. 
        Input and output may be either a single string or a list of strings but must always be of the same type.

        Args:
            input_text: a string  or a list of strings to be transliterated

        Returns
            phonetic: a string or list of strings of transliterated text
        """

        if type(input_text) is str:

            #preprocess individual string
            split_text = input_text.split('\n')

            for elt in split_text:
                if elt=='\r':
                    split_text.remove(elt)
                elt.replace('\r', '')

            translation = self.pipe(split_text)

        else:

            translation = self.pipe(input_text)


        translation = [elt['translation_text'] for elt in translation]

        if type(input_text) is str and len(translation) == 1:

            translation = translation[0]
        
        return translation