'''
Example code to demonstrate the working of SD Card -- read and write operation
To run the code , add the library file of sdcard as sdcard.py 
'''
import time, utime
import random
from machine import Pin, SPI ,UART
import sdcard
import os

def sdtest(data):  # Test method for SD CARD
    spi=SPI(0,sck=Pin(18),mosi=Pin(19),miso=Pin(16)) # setting the SPI pins
    sd=sdcard.SDCard(spi,Pin(17))
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/fc") # mount SD card
    print("Filesystem check")
    print(os.listdir("/fc")) # print the list of directory stored in the files of sd card
    fn = "/fc/File3.txt"  #create file with suitable name
    print()
    print("Single block read/write")
    with open(fn, "a") as f:
        n = f.write(data)  #write data to file
        print(n, "bytes written") 

    with open(fn, "r") as f:
        result2 = f.read() # read data from the file
        print(len(result2), "bytes read")
        print("Data written on File:")
        print(result2) # Display the data read from the SD Card, which was previously written to the card as data.
   
    os.umount("/fc")
    
sdtest("Hello World")

while True:
    time.sleep(1)
    
