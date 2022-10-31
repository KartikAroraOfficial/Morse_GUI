import led_controller
import morse
import time


controller = led_controller.led_controller()

def test_controller_blinkDit():
    controller.blinkDit()

def test_controller_blinkDah():
    controller.blinkDah()

def test_morse_values():
    for x in morse.morse_dict.keys():
        print (f"{x}: {morse.morse_dict[x]} ")


def check_character_existance():
    char = input("Enter the character you want to check for in the morse dict: ")

    try:
        print(f"letter found: {morse.morse_dict[char.upper()]}")
    except:
        print("Can't find the letter! ")

if __name__ == "__main__":
    test_controller_blinkDit()
    time.sleep(1)
    test_controller_blinkDah()
    time.sleep(1)
    check_character_existance()