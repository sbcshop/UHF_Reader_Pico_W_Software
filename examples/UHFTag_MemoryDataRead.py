'''
Code to perform read operation from Memory of UHF Tags,
Reserved, EPC, TID and User are different memory options available

'''
from machine import UART, Pin,SPI
import time,utime
from uhf import UHF #include uhf library file

#UHF enable pin connected at GP4 
enable_pin = machine.Pin(4, machine.Pin.OUT) # set pin as OUTPUT
enable_pin.value(0) # LOW value enables UHF module, HIGH to disable module

baudrate = 115200   # communication baudrate
uhf = UHF(baudrate) # create instance for class UHF

'''
Memory Bank 
1 - EPC  --> Read/Write
2 - TID  --> Only readable
3 - USER --> Read/Write
'''

Memory_bank = '3' # Change to read corresponding Memory 

#Select the tag EPC id for read data
response = uhf.Set_select_pera('80464500e280101010121100') # provide the EPC of the tag, which you want to read
print(response)

#Tag data read
response = uhf.Read_tag_data(Memory_bank)
print(response)

