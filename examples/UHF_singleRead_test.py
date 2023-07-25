'''
Demo code to test UHF for single poll command
To run the code successfully, add the library file of uhf to pico W 
-> https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/examples/lib/uhf.py
'''
from machine import UART, Pin,SPI,I2C
import time,utime
from uhf import UHF #import uhf library file

#UHF enable pin connected at GP26 
enable_pin = machine.Pin(26, machine.Pin.OUT) # set pin as OUTPUT
enable_pin.value(0) # LOW value enables UHF module, HIGH to disable module

baudrate = 115200 # communication baudrate
uhf = UHF(baudrate)	# create instance for class UHF
response = uhf.single_read() # call method for single poll command

print(response)

if response is not None:
   print('EPC = ',response[8:20])
   print('RSSI(dBm) = ', response[5])
   print('CRC = ',response[20],response[21])


time.sleep(1)
uhf.stop_read()	# call function to send stop operation command 
