from microbit import *
import machine
import neopixel
import music
# Enable ZIP LEDs to use x & y values
def zip_plot(x, y, colour):
 zip_led[x+(y*8)] = (colour[0], colour[1], colour[2])
# Function to play tune on buzzer and run motor for 500ms
def hit_edge():
 music.play(music.BA_DING, pin2, False)
 pin1.write_digital(1)
 sleep(500)
 pin1.write_digital(0)
# Setup variables and initial ZIP LED display
zip_led = neopixel.NeoPixel(pin0, 64)
#V2 microbit has configurable pin drives, which are setup differently to the V1 by default.
#The NRF processor GPIO pin2 is microbit pin0  where the ZIP LEDs are connected.
#To set it to high drive mode we write directly to the configuration register with this obscure looking incantation:
machine.mem32[0x50000708]= 0x703
sprite_x = 3
sprite_y = 3
# Colours: Red, Yellow, Green, Blue, Purple, White
colours = [[20, 0, 0], [20, 20, 0], [0, 20, 0], [0, 0, 20], [20, 0, 20], [20, 20, 20]]
sprite_colour = colours[3]
zip_plot(sprite_x, sprite_y, sprite_colour)
zip_led.show()
# While loop to run forever
while True:
    # Check button presses
    if pin8.read_digital() == 0 and sprite_y == 0:
        hit_edge()
    elif pin8.read_digital() == 0 and sprite_y != 0:
        sprite_y = sprite_y - 1

    if pin14.read_digital() == 0 and sprite_y == 7:
        hit_edge()
    elif pin14.read_digital() == 0 and sprite_y != 7:
        sprite_y = sprite_y + 1

    if pin12.read_digital() == 0 and sprite_x == 0:
        hit_edge()
    elif pin12.read_digital() == 0 and sprite_x != 0:
        sprite_x = sprite_x - 1
    if pin13.read_digital() == 0 and sprite_x == 7:
        hit_edge()
    elif pin13.read_digital() == 0 and sprite_x != 7:
        sprite_x = sprite_x + 1
    if pin15.read_digital() == 0:
        if colours.index(sprite_colour) - 1 < 0:
            sprite_colour = colours[0]
        else:
            sprite_colour = colours[(colours.index(sprite_colour) - 1)]
    if pin16.read_digital() == 0:
        if colours.index(sprite_colour) + 1 > 5:
            sprite_colour = colours[5]
        else:
            sprite_colour = colours[(colours.index(sprite_colour) + 1)]
    # Clear and redisplay the ZIP LEDs after each button press check 
    zip_led.clear()
    zip_plot(sprite_x, sprite_y, sprite_colour)
    zip_led.show()
    # 100ms pause before restarting the while loop
    sleep(100)
