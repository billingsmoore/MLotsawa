from transformers import pipeline

class Transliterator():

    def __init__(self):

        # initialize a translation pipeline
        self.pipe = pipeline('translation', 'billingsmoore/tibetan-phonetic-transliteration')


    def convert(self, input_text):
        """
        This function takes in a string and if it is in Tibetan unicode, the function converts it to 
        Wylie transliteration using pyewts. Otherwise, the function assumes that the inputted text is
        already a Wylie transliteration and converts it to THL Simplified Phonetic Transliteration.

        Args:
            input_text: a string of either Tibetan unicode or a Wylie transliteration

        Returns
            phonetic: a string of text which is the THL phonetic version of the input
        """

        # if input is Tibetan unicode, use pyewts to convert it to Wylie
        if self.is_tibetan_unicode(input_text):
            
            transliteration = self.transliterate(input_text)

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
        
        # Check each character in the string
        for char in text:
            if ord(char) in tibetan_range:
                return True
        return False

    def transliterate(self, input_text):
        """
        This is a helper function for convert. This function transliterates the inputted
        Tibetan text.

        Args:
            input_text: a string of Tibetan unicode text
        
        Returns:
            output_text: a string of transliterated text
        """

        output = self.pipe(input_text)

        output_text = [elt['translation_text'] for elt in output]

        output_text = '\n'.join(output_text)

        return output_text
