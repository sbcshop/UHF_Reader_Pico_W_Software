# Example to read tags and show on display 
from machine import UART,SPI,Pin
import st7789
import time,utime
import vga1_8x16 as font1
import vga1_16x32 as font
import vga1_16x16 as font2
#Import the uhf library along with some inbuilt libraries.
from machine import UART,SPI,I2C,Pin
import time,utime
from uhf import UHF

#setting parameters
enable_pin = Pin(26, machine.Pin.OUT) #enabling the pin for module
enable_pin.value(0) # Here LOW enables UHF module, HIGH disable
baudrate = 115200 # communication baudrate between Pico W and UHF module

uhf = UHF(baudrate)

'''
Uncomment corresponding section to increase reading range,
you will have to set the region as per requirment
'''
#uhf.setRegion_EU() 
uhf.setRegion_US()

uhf.multiple_read() # Calling Method to initialise the multiple read by sending related UHF command

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
                    
tft.init() # initialising the TFT

def displayText(epart1, epart2):
    tft.text(font,"TAG Detected!", 20,10,st7789.RED)
    tft.text(font2,epart1, 0,70,st7789.GREEN)
    tft.text(font2,epart2, 0,90,st7789.GREEN)
    utime.sleep(3)
    tft.fill(0) #clear screen

def msgDisplay(msgText):
    tft.text(font, msgText, 20,20,st7789.YELLOW)
    utime.sleep(2)
    tft.fill(0) #clear screen

msgDisplay("Hello!")

uhf.multiple_read() # Calling Method to initialise the multiple read by sending related UHF command
msgDisplay("Ready")

try:
    while 1:
        rev = uhf.read_mul()  # storing the data frame in the array rev
        if rev is not None:
            print('EPC = ',"".join(rev[8:20])) # Extracting the EPC value from 8th bit to 20th bit & print it
            print('RSSI(dBm) = ',rev[5])       # Extracting the RSSI value stored at 5th bit & print it.
            print('CRC = ',rev[20],rev[21])    # Extracting the CRC values stored at 20th & 21st bit & print the same
            print('PC = ',rev[6],rev[7])	   # Extracting the PC  stored at 6th & 7th 
            print("\n")
            tagValuePart1 = "".join(rev[8:16])
            tagValuePart2 = "".join(rev[17:20])
            displayText(tagValuePart1,tagValuePart2)
        time.sleep(0.000001 )
        
except KeyboardInterrupt:
    uhf.stop_read()
    time.sleep(1)
    print("stop")