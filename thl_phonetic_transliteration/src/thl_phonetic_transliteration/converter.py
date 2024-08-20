import pyewts
import re

def convert(input_text):
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
    if is_tibetan_unicode(input_text):
        converter = pyewts.pyewts()
        wylie = converter.toWylie(input_text).split('\n')
    else:
        wylie = input_text.split('\n')

    # convert text Wylie to THL Simplified Phonetic Transliteration
    phonetic = wylie_to_phonetic(wylie)

    phonetic = '\n'.join(phonetic)

    return phonetic


def is_tibetan_unicode(text):
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

# These are the character replacements to convert Wylie to THL phonetic
replacements = [[['lth', 'rh', 'db'] , ' '],
    [['rb', 'sb', 'sbr', 'lb', '’b', '\'b'] , 'b'],
    [['c', 'cw', 'gc', 'bc', 'lc', 'py', 'lpy', 'spy', 'dpy', 'mch', '’ch', '\'ch', 'phy', '’phy', '\'phy'] , 'ch'],
    [['rd', 'sd', 'gd', 'bd', 'brd', 'bsd', 'zl', 'bzl', 'ld', 'md', '’d', '\'d', 'dw'] , 'd'],
    [['rgr', 'lgr', 'sgr', 'dgr', 'dbr', 'bsgr', 'rbr', 'lbr', 'sbr', 'mgr', '’gr', '\'gr', '’dr', '\'dr', '’br', '\'br', 'gr', 'br', 'grw'] , 'dr'],
    [['rdz', 'gdz', 'brdz', 'mdz', '’dz', '\'dz'] , 'dz'],
    [['rg', 'lg', 'sg', 'dg', 'bg', 'brg', 'bsg', 'lg', 'mg', '’g', '\'g', 'gw'] , 'g'],
    [['rgy', 'lgy', 'sgy', 'dgy', 'bgy', 'brgy', 'bsgy', 'mgy', '’gy', '\'gy'] , 'gy'],
    [['hw'] , 'h'],
    [['rby', 'lby', 'sby', 'rj', 'gj', 'brj', 'lj', 'mj', '’j', '\'j', '’by', '\'by', 'by'] , 'j'],
    [['rk', 'lk', 'sk', 'kw', 'dk', 'bk', 'brk', 'bsk'] , 'k'],
    [['khw', 'mkh', '’kh', '\'kh'] , 'kh'],
    [['mkhy', '’khy', '\'khy'] , 'khy'],
    [['rky', 'lky', 'sky', 'dky', 'bky', 'brky', 'bsky'] , 'ky'],
    [['kl', 'gl', 'bl', 'rl', 'sl', 'brl', 'bsl', 'lw'] , 'l'],
    [['rm', 'sm', 'dm', 'smr', 'mr'] , 'm'],
    [['rn', 'sn', 'gn', 'brn', 'bsn', 'mn'] , 'n'],
    [['rng', 'lng', 'sng', 'dng', 'brng', 'bsng', 'mng'] , 'ng'],
    [['rny', 'sny', 'gny', 'brny', 'bsny', 'mny', 'nyw', 'rmy', 'smy', 'my'] , 'ny'],
    [['sp', 'dp', 'lp', 'ph', '’ph', '\'ph'] , 'p'],
    [['rw'] , 'r'],
    [['sr', 'sw', 'gs', 'bs', 'bsr'] , 's'],
    [['shw', 'gsh', 'bsh'] , 'sh'],
    [['rt', 'lt', 'st', 'tw', 'gt', 'bt', 'brt', 'blt', 'bst', 'bld', 'th', 'mth', '’th' '\'th'] , 't'],
    [['kr', 'rkr', 'lkr', 'skr', 'pr', 'lpr', 'spr', 'dkr', 'dpr', 'bkr', 'bskr', 'bsr', 'khr', 'thr', 'phr', 'mkhr', '’khr', '’phr'] , 'tr'],
    [['rts', 'sts', 'rtsw', 'stsw', 'gts', 'bts', 'brts', 'bsts', 'tsh', 'tshw', 'mtsh', '’tsh', '\'tsh'] , 'ts'],
    [['db', 'b'] , 'w'],
    [['g.y', 'dby'] , 'y'],
    [['zw', 'gz', 'bz'] , 'z'],
    [['zh', 'zhw', 'gzh', 'bzh'] , 'zh']]


def wylie_to_phonetic(wylie):
    """
    This is a helper function for thl_phonetic translation. This is a function to 
    convert Wylie transliteration to THL Simplified Tibetan Transliteration.

    Args:
        wylie: A string composed of text which the Wylie transliteration of Tibetan

    Returns:
        phonetic: A string composed of the THL phonetic version of 'wylie'
    """

    phonetic = []
    for line in wylie:
        if line != '':
            # perform replacements
            result = line
            for elt in replacements:
                replace_list = elt[0]
                for string in replace_list:
                    result = result.replace(string, elt[1])

            # remove non-alphabetical chars
            result = re.sub(r'[^a-zA-Z\s]', '', result)
            phonetic.append(result)

    return phonetic
