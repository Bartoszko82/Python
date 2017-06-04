from microbit import *
import radio


radio.on()
while True:
    message = radio.receive()
    radio.config(channel=66)
    
    if message:
        display.scroll(message)
    if button_a.was_pressed():
        display.clear()
        display.scroll("ACCEPTING")
        radio.send("TAK")
    if button_a.was_pressed():
        display.clear()
        display.scroll("REJECTING")
        radio.send("NIE")
    if pin0.is_touched():
        display.clear()
        display.scroll("SENDING")
        radio.send("PIWO?")

        