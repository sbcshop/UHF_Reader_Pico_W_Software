'''
- This code demostrate how to write data into Memory of UHF Tags,
- Only EPC and USER memory are writeable
- EPC memory allow to change default EPC value of Tag
- USER memory to store required data 
'''
#import library modules
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
3 - USER --> Read/Write
'''

Memory_bank = '3'	# Make sure to select correct bank for Read/Write operation

#Select the Tag for write operation
response = uhf.Set_select_pera('80464500e280101010121100') # change with the EPC of the tag, which you want to write
print(response)

'''Make sure to maintain correct data length cannot exceed 32 words (64 bytes) for write operation, as shown below
e.g.
91418800000000000000000000000000  => Any Data, 32 word length 
10c9340080464500e280101010121100  => with EPC value, again 32 word length

- Build write data for USER : simply contains byte value of your choice

- Build EPC write data : this include,
Checksum (of Previous EPC) + PC(of Previous EPC) + EPC (change with NEW) =>
10c9 + 3400 + 80464500e280101010121100

To get checksum and PC of Tag run below script first,
https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/examples/UHF_multipleRead_test.py
'''

#Change Data which you want to Write, in case of EPC write build correct data format as shown above
response = uhf.Write_tag_data('91418800000000000000000000000000',Memory_bank) # maximum length is 32 words 
print(response)

