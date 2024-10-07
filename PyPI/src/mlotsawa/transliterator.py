from transformers import pipeline

class Transliterator():

    def __init__(self):

        # initialize a translation pipeline
        self.pipe = pipeline('translation', 'billingsmoore/tibetan-phonetic-transliteration')


    def transliterate(self, input_text):
        """
        This function takes in a string and if it is in Tibetan unicode, the function transliterates it. 
        Otherwise, the function assumes the input was a mistake and returns it unaltered. Input and output may be either
        a single string or a list of strings but must always be of the same type.

        Args:
            input_text: a string  or a list of strings to be transliterated

        Returns
            phonetic: a string or list of strings of transliterated text
        """

        # if input is Tibetan unicode, transliterate it
        if self.is_tibetan_unicode(input_text):
            
            transliteration = self.convert(input_text)

            if type(input_text) is str and len(transliteration) == 1:

                transliteration = transliteration[0]

            return transliteration
        
        # if input is already transliterated, return the input unchanged
        else:

            return input_text


    def is_tibetan_unicode(self, text):
        """
        This is a helper function for convert. This function checks if a string
        is composed of Tibetan unicode text and returns True if it is and returns False otherwise.

        Args:
            text: A string of text to check 

        Returns:
            Bool: True if the text is Tibetan unicode, False otherwise.
        """
        # Define the Tibetan Unicode range
        tibetan_range = range(0x0F00, 0x0FFF + 1)

        if type(text) is not str:
            text = text[0]
        
        # Check each character in the string
        for char in text:
            if ord(char) in tibetan_range:
                return True
            
        return False

    def convert(self, input_text):
        """
        This is a helper function for transliterate. This function transliterates the inputted
        Tibetan text.

        Args:
            input_text: a string of Tibetan unicode text
        
        Returns:
            output_text: a list of strings of transliterated text
        """

        output = self.pipe(input_text)

        output_text = [elt['translation_text'] for elt in output]

        return output_text
