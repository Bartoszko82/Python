from microbit import *
import radio


radio.on()
while True:
    message = radio.receive()
    if message:
        display.scroll("RECEIVED")
    if button_a.was_pressed():
        display.clear()
        display.scroll("SENDING")
        radio.send("haha")
