from led_controller import led_controller
import time


UNIT = 0.3                 # unit time
DOT_TIME = 1*UNIT          # also the time for space between the symbols - 1 unit
DASH_TIME = 3*UNIT         # also the space between letters - 3 units
WORD_SPACE = 7*UNIT        # space between two words - 7 units
SAME_LETTER_TIME = UNIT    # 1 unit
DIFF_LETTER_TIME = 3*UNIT  # 3 units

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

controller = led_controller()

class morse:
    def __init__(self):
        super().__init__()


    def translate(self, phrase):
        result = ''
        for x in phrase:
            if (x.upper() in morse_dict.keys()):
                result += morse_dict[x.upper()] + " "
            else:
                result = 'Error: Invalid character in string!'
                return result                                       # returns the error message string!
        return result

# character received is always in upper()
    def blink_letter(self, character):
        if (character in morse_dict.keys()):
            for x in range(len( morse_dict[character])):
                if morse_dict[character][x] == '.':                 # checks if the character in the value received is a Dot

                    controller.blinkDit()
                    if x == len(morse_dict[character])-1:
                        time.sleep(DIFF_LETTER_TIME)
                    else:
                        time.sleep(SAME_LETTER_TIME)
                elif morse_dict[character.upper()][x] == '-':       # checks if the character in the value received is a Dash
                    controller.blinkDah()
                    if x == len(morse_dict[character])-1:
                        time.sleep(DIFF_LETTER_TIME)
                    else:                                           # checks if the character in the value received is a /
                        time.sleep(SAME_LETTER_TIME)
                else:
                    time.sleep(WORD_SPACE)
