'''
Example Code to operate the User button. 
3 user buttons (label as BT2, BT3 and BT4 ) are there on the board on pressing each button the TFT screen would show the separate message
'''

from machine import UART,SPI,Pin
import time
import st7789
import vga1_8x16 as font1
import vga1_16x32 as font
import vga1_16x16 as font2

spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))  #setting the parameters for the SPI communication.

'''
#spi-->SPI bus object
#135,240 -->width & height of the TFT display
#reset pin, chip select pin ,Data command pin & Backlight of TFT -->GPIO output
#Rotation =1--> Display rotation setting as per need, other options 0(default), 2, 3 
'''
tft = st7789.ST7789(spi,135,240,reset=Pin(14, Pin.OUT),cs=Pin(13, Pin.OUT),dc=Pin(11, Pin.OUT),
                    backlight=Pin(12, Pin.OUT),rotation=1)

#Set button pins for input operation to read current status of switch pressed or not
BT2 = Pin(10, Pin.IN, Pin.PULL_UP)
BT3 = Pin(9, Pin.IN, Pin.PULL_UP)
BT4 = Pin(8, Pin.IN, Pin.PULL_UP)

tft.init() # initialising the TFT
time.sleep(0.2)

while True:
    if BT2.value() == 0:  # On pressing the Button 2 , user will see the message on TFT screen
        print("button2")
        tft.text(font,"Button_2!", 0,0,st7789.RED)
        time.sleep(0.5)
        tft.fill(0) #clear screen
       
    elif BT3.value() == 0:  # On pressing the Button 3 , user will see the message on TFT screen
        print("button3")
        tft.text(font,"Button_3!", 0,0,st7789.BLUE)
        time.sleep(0.5)
        tft.fill(0) #clear screen

    elif BT4.value() == 0: # On pressing the Button 4 , user will see the message on TFT screen
        print("button4")
        tft.text(font,"Button_4!", 0,0,st7789.YELLOW)
        time.sleep(0.5)
        tft.fill(0) #clear screen
    time.sleep(0.1)
