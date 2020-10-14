import re

translationDictionary = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '0' : '-----',
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '\'' : '.----.',
    '!' : '-.-.--',
    '/' : '-..-.',
    ':' : '---...',
    ';' : '-.-.-.',
    '=' : '-...-',
    '+' : '.-.-.',
    '-' : '-....-',
    '_' : '..--.-',
    '*' : '.-..-.',
    '@' : '.--.-.'
}

def GetUserInput():
    inputString = input("Enter a string to translate into or translate from Morse:\n")
    return inputString.strip().split(' ')

def GetTranslationKey(lookupValue):
    for key, value in translationDictionary.items():
        if lookupValue == value:
            return key
    print('Translation key for \'{0}\' could not be found. Leaving it untouched.\n'.format(lookupValue))
    return lookupValue

def TranslateCharacters(charsToTranslate):
    translatedCharacters = []
    for character in charsToTranslate:
        if character.isalnum():
            for x in character:
                upperCharacter = x.upper()
                translatedCharacters.append(translationDictionary['{0}'.format(upperCharacter)])
        elif re.search("[-\-|.+]",character):
            translatedCharacters.append(GetTranslationKey(character))
        else:
            translatedCharacters.append(character)
            print('Warning: Unknown character \'{0}\' Leaving it untouched.\n'.format(character))
    return translatedCharacters

def PrintResult(original, translated):
    originalString = ""
    translatedString = ""
    for x in original:
        originalString = originalString+x
    print("Original string:\n{0}".format(originalString))
    for y in translated:
        translatedString = translatedString+y
    print("Translated string:\n{0}".format(translatedString))

if __name__ == "__main__":
    charsToTranslate = GetUserInput()
    translatedChars = TranslateCharacters(charsToTranslate)
    PrintResult(charsToTranslate, translatedChars)
