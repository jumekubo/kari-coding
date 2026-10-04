# Kari Coding

A growing collection of coding experiments and learning projects for Kari and family.

## Live project

[Open Kari's Morse Lab](https://karis-morse-lab.jumekubo.chatgpt.site/)

## Projects

### Morse LED simulator

An interactive browser project that translates a message into Morse code, blinks a virtual LED, and generates matching CircuitPython code for a Nano-compatible board.

Open `projects/morse-led/index.html` in a browser. No installation or build step is needed. After GitHub Pages is enabled, the project will also be available at `https://jumekubo.github.io/kari-coding/projects/morse-led/`.

Future projects can live alongside it:

```text
projects/
├── morse-led/
├── rgb-led/
├── sensors/
├── p5js/
└── unity/
```

## Moving a project to the Nano

Save CircuitPython programs as `code.py` on the board's `CIRCUITPY` drive. Pin names may need to be adjusted for the exact Nano model.

## Hardware safety

When using an external LED, add a current-limiting resistor (commonly 220–330 ohms) and verify the board's pinout before wiring it.
