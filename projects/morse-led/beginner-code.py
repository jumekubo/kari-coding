import time
import board
import digitalio

# External LED on GP14 (physical pin 19)
led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT

# One Morse timing unit is 0.2 seconds.
UNIT = 0.2
MESSAGE = "KARINA"

# Only the letters needed to spell KARINA are included for now.
MORSE = {
    "A": ".-",
    "I": "..",
    "K": "-.-",
    "N": "-.",
    "R": ".-."
}


def flash(symbol):
    led.value = True

    if symbol == ".":
        time.sleep(UNIT)
    else:
        time.sleep(3 * UNIT)

    led.value = False


def send_message(message):
    for letter in message:
        pattern = MORSE[letter]

        for symbol in pattern:
            flash(symbol)
            time.sleep(UNIT)

        # The last symbol supplied 1 off-unit.
        # Two more creates the 3-unit gap between letters.
        time.sleep(2 * UNIT)


while True:
    send_message(MESSAGE)

    # The last letter supplied 3 off-units.
    # Four more creates a 7-unit gap before repeating.
    time.sleep(4 * UNIT)
