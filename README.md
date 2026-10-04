# Python Coding

A growing collection of approachable Python and physical-computing projects.

## Live website

[Open the Python Coding project hub](https://jumekubo.github.io/python-coding/)

## Projects

### Python Morse Lab

An interactive browser project that translates a message into Morse code, blinks a virtual LED, and generates matching CircuitPython code for a Raspberry Pi Pico-family board.

Open `projects/python-morse-lab/index.html` locally, or [open Python Morse Lab](https://jumekubo.github.io/python-coding/projects/python-morse-lab/). No installation or build step is needed.

Future projects can live alongside it:

```text
projects/
├── python-morse-lab/
├── rgb-led/
├── sensors/
├── p5js/
└── unity/
```

## Moving a project to the Pico

Save CircuitPython programs as `code.py` on the board's `CIRCUITPY` drive. Python Morse Lab uses an external LED on `board.GP14`.

## Hardware safety

When using an external LED, add a current-limiting resistor (commonly 220–330 ohms) and verify the board's pinout before wiring it.
