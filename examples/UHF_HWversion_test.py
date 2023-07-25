'''
Demo code to test UHF command for hardware version detection
To run the code successfully, add the library file of uhf to pico W 
-> https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/examples/lib/uhf.py
'''
from machine import UART, Pin,SPI
import time,utime
from uhf import UHF #include uhf library file
import st7789
import vga1_8x16 as font1
import vga1_16x32 as font
import vga1_16x16 as font2

#configure SPI interfacing for display
spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))  #setting the parameters for the SPI communication.
tft = st7789.ST7789(spi,135,240,reset=Pin(14, Pin.OUT),cs=Pin(13, Pin.OUT),dc=Pin(11, Pin.OUT),
                    backlight=Pin(12, Pin.OUT),rotation=1)

def displayText(data):
    tft.init() # initialising the TFT 
    utime.sleep(0.5)
    tft.text(font2,data, 5,0,st7789.CYAN)

#UHF enable pin connected at GP4 
enable_pin = machine.Pin(4, machine.Pin.OUT) # set pin as OUTPUT
enable_pin.value(0) # LOW value enables UHF module, HIGH to disable module

baudrate = 115200 # communication baudrate
uhf = UHF(baudrate)	# create instance for class UHF
response = uhf.hardware_version() # call method for hardware version check command

print(response) 

displayText(response)

time.sleep(2)
uhf.stop_read()	# call function to send stop operation command 
