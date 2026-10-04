# Morse LED Simulator

This project demonstrates how Morse-code timing maps to an LED controlled by CircuitPython.

The generated program targets a Raspberry Pi Pico-family board with an external LED connected to `board.GP14`. Use a current-limiting resistor in series with the LED.

Start with [`beginner-code.py`](beginner-code.py). It uses ordinary `if`/`else` statements and basic `for` loops, without `enumerate()` or a compressed conditional expression.

The simulator:

- translates letters and numbers into Morse code;
- blinks a virtual LED using standard dot, dash, letter-gap, and word-gap timing;
- highlights the active letter and symbol;
- allows the message and speed to be changed; and
- generates matching CircuitPython code.

Open `index.html` in a browser to use it. No installation or build step is required.
