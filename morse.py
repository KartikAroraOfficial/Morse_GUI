# This Python file uses the following encoding: utf-8
from msilib.schema import Error
from led_controller import led_controller
import time


UNIT = 0.3                 # unit time 
DOT_TIME = 1*UNIT          # also the time for space between the symbols - 1 unit
DASH_TIME = 3*UNIT         # also the space between letters - 3 units
WORD_SPACE = 7*UNIT        # space between two words - 7 units
SAME_LETTER_TIME = UNIT    # 1 unit
DIFF_LETTER_TIME = 3*UNIT  # 3 units

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}


class morse:
    def __init__(self):
        super().__init__()
        self.controller = led_controller.led_cotnroller()

    def translate(self, phrase):
        result = ''
        for x in phrase:
            if (x.upper() in morse_dict.keys()):
                result += morse_dict[x]
            else:
                raise LookupError("Invalid Character in String!")
                # result = 'Error: Invalid character in string!'
                # return result
        return result

    def blink_letter(self, character):
        if (character.upper() in morse_dict.keys()):
            for x in range(len(morse_dict[character])):
                if morse_dict[x] == '.':
                    self.controller.blinkDit()
                    if x == len(morse_dict[x])-1:
                        time.sleep(DIFF_LETTER_TIME)
                    else:
                        time.sleep(SAME_LETTER_TIME)
                elif morse_dict[x] == '-':
                    self.controller.blinkDah()
                    if x == len(morse_dict[x])-1:
                        time.sleep(DIFF_LETTER_TIME)
                    else:
                        time.sleep(SAME_LETTER_TIME)
                else:
                    time.sleep(WORD_SPACE)
        else:
            raise LookupError