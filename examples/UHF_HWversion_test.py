#Demo code to test UHF command for hardware version detection
from machine import UART, Pin,SPI,I2C
import time,utime
from uhf import UHF #include uhf library file

#UHF enable pin connected at GP4 
enable_pin = machine.Pin(4, machine.Pin.OUT) # set pin as OUTPUT
enable_pin.value(0) # LOW value enables UHF module, HIGH to disable module

baudrate = 115200 # communication baudrate
uhf = UHF(baudrate)	# create instance for class UHF
response = uhf.hardware_version() # call method for hardware version check command

print(response) 

time.sleep(1)
uhf.stop_read()	# call function to send stop operation command 
