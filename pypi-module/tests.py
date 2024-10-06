from colorama import init, Fore

# Initializes Colorama
init(autoreset=True)

from src.mlotsawa.transliterator import Transliterator 
from src.mlotsawa.translator import Translator 

# Transliteration tests
transliterator = Transliterator()

# Test #1 preserve already transliterated
tibetan_text = 'sangyé kün gyi daknyi'
phonetics = transliterator.transliterate(tibetan_text)
if tibetan_text == phonetics:
    print(Fore.GREEN + 'Passed test case #1: preserve already transliterated')
else:
    print(Fore.RED + f'Failed test case #1: expected {tibetan_text}, instead got {phonetics}')

# Test #2 transliterate single string
tibetan_text = 'སངས་རྒྱས་ཀུན་གྱི་བདག་ཉིད། །'
phonetics = transliterator.transliterate(tibetan_text)
if type(phonetics) is str:
    print(Fore.GREEN + f'Passed test case #2: transliterated single string as {phonetics}')
else:
    print(Fore.RED + f'Failed test case #2: expected str, instead got {type(phonetics)}')

# Test #3 transliterate list of strings
tibetan_text = ['སངས་རྒྱས་ཀུན་གྱི་བདག་ཉིད། །', 'ཡེ་ཤེས་སྤྱན་གྱིས་གཟིགས་ཤིག །']
phonetics = transliterator.transliterate(tibetan_text)
if type(phonetics) is list:
    print(Fore.GREEN + f'Passed test case #3: transliterated list of strings as {phonetics}')
else:
    print(Fore.RED + f'Failed test case #2: expected list, instead got {type(phonetics)}')


# Translation tests
translator = Translator()

# Test case #4 translate single string
tibetan_text = 'ཡེ་ཤེས་སྤྱན་གྱིས་གཟིགས་ཤིག །' # may be in Tibetan script or phoneticized
translation = translator.translate(tibetan_text)
if type(translation) is str:
    print(Fore.GREEN + f'Passed test case #4: translated single string as {translation}')
else:
    print(Fore.RED + f'Failed test case #4: expected str, instead got {type(translation)} for {translation}')

# Test case #5 translate list of strings
tibetan_text = ['སངས་རྒྱས་ཀུན་གྱི་བདག་ཉིད། །', 'sangyé kün gyi daknyi']
translation = translator.translate(tibetan_text)
if type(translation) is list:
    print(Fore.GREEN + f'Passed test case #5: translated list of strings as {translation}')
else:
    print(Fore.RED + f'Failed test case #5: expected list, instead got {type(translation)}')