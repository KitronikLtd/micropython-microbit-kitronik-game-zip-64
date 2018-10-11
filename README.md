# micropython-microbit-kitronik-game-zip-64
Example MicroPython (for BBC micro:bit) code for the Kitronik :GAME ZIP 64 ( www.kitronik.co.uk/5626 )

## Overview

This repo contains examples of MicroPython programs for the Kitronik :GAME ZIP 64.
No unique functions are required to use the :GAME ZIP 64, just the normal use of the 'microbit' and 'neopixel' libraries.

## :GAME ZIP 64 Pinout

* 8x8 ZIP LED Display (Pin 0)
* Vibration Motor for Haptic Feedbacl (Pin 1)
* Piezo Buzzer for Audio Feedback (Pin 2)
* Joypad Up Button (Pin 8)
* Joypad Left Button (Pin 12)
* Joypad Right Button (Pin 13)
* Joypad Down Button (Pin 14)
* Fire 1 Button (Pin 15)
* Fire 2 Button (Pin 16)

* Button Expansion Point 1 (Pin 20) 
* Button Expansion Point 2 (Pin 19)

## Bit Pong

The file 'bit_pong.py' is a simple game based on the classic 'Pong'.
The Joypad Up and Down buttons are used to control one paddle, and Fire 1 and 2 the other.
A 'ball' bounces between them.
If the 'ball' passes a paddle, the opposite player gains 1 point.
It is the 'best of 3' matches to see who is the winner!

## License

MIT

## Supported Targets

BBC micro:bit