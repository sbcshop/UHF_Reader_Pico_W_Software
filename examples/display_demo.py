# Example to show the Message display on TFT screen configure with Rasberry Pi Pico W
from machine import UART,SPI,Pin
import st7789
import time,utime
import vga1_8x16 as font1
import vga1_16x32 as font
import vga1_16x16 as font2

#configure SPI interfacing for display
spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))  #setting the parameters for the SPI communication.

'''
#spi-->SPI bus object
#135,240 --> width & height of the TFT display
#reset pin, chip select pin ,Data command pin & Backlight of TFT --> GPIO output
#Rotation = 1 --> Display rotation setting as per need, other options 0(default), 2, 3 
'''
tft = st7789.ST7789(spi,135,240,reset=Pin(14, Pin.OUT),cs=Pin(13, Pin.OUT),dc=Pin(11, Pin.OUT),
                    backlight=Pin(12, Pin.OUT),rotation=1)
                    

def displayText():
    tft.init() # initialising the TFT 
    utime.sleep(0.5)
    tft.text(font,"Hello!", 0,0,st7789.RED)
    time.sleep(1)
    tft.fill(0) #clear screen
    tft.text(font2,"Thank You For ", 0,0,st7789.GREEN)
    tft.text(font2,"Buying", 0,30,st7789.GREEN)
    tft.text(font2,"SB Components", 0,100,st7789.BLUE)
    time.sleep(5)
    tft.fill(0) #clear screen
        
displayText()
