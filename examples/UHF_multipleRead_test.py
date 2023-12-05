'''
Demo to Several Time polling command of UHF reader
To run the code successfully, add the library file of uhf to pico W 
-> https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/examples/lib/uhf.py
'''
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
#uhf.setRegion_US()

uhf.multiple_read() # Calling Method to initialise the multiple read by sending related UHF command 
try:
    while 1:
        rev = uhf.read_mul()  # storing the data frame in the array rev
        if rev is not None:
            print('EPC = ',"".join(rev[8:20])) # Extracting the EPC value from 8th bit to 20th bit & print it
            print('RSSI(dBm) = ',rev[5])       # Extracting the RSSI value stored at 5th bit & print it.
            print('CRC = ',rev[20],rev[21])    # Extracting the CRC values stored at 20th & 21st bit & print the same
            print('PC = ',rev[6],rev[7])	   # Extracting the PC  stored at 6th & 7th 
            print("\n")
        time.sleep(0.000001 )
        
except KeyboardInterrupt:
    uhf.stop_read()
    time.sleep(1)
    print("stop")

