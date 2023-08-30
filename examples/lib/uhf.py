#uhf library file
import machine
import time
import binascii
import array

'''
standard commands for UHF operations, refer command manual for more details
https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/documents/UHF%20Commands%20Manual.pdf
So, you can add more commands for other operation
'''

STARTBYTE     ='BB00'	# combine Header + Type
ENDBYTE       ='7E'

'''2.1 Get the reader module information'''
HARD_VERSION  ='0300010004'

''' 2.2 Single polling command '''
SINGLE_READ   ='22000022'

''' 2.3 Several times polling command '''
MULTIPLE_READ ='27000322271083'

STOP_READ     ='28000028'

'''section: 2.12 Set Working Place'''
SET_REGION_EU = '070001030B' #for Setting EU Region
SET_REGION_US = '070001020A' #for Setting US Region

'''Section: 2.16 Get transmitting power '''
GET_TRANSMIT_PWR = 'B70000B7'

class UHF():
    def __init__(self,baudrate):
        self.serial = machine.UART(1, baudrate=baudrate, bits=8, parity=None, stop=1, tx=machine.Pin(4), rx=machine.Pin(5))
        self.serial.init(baudrate=baudrate, bits=8, parity=None, stop=1)
        time.sleep(0.2)
        
    def read_mul(self):
        rec_data = self.serial.read(24)
        if rec_data is not None and len(rec_data)>22:
            if rec_data[0] != 0xbb or rec_data[23] != 0x7e or rec_data[1] != 0x02:
                return None        
            return ['{:02x}'.format(x) for x in rec_data]
            
    def send_command(self, data):
        Data = ''.join(data)
        bin_data = binascii.unhexlify(Data)
        response = self.serial.write(bin_data)

    def hardware_version(self):
        self.send_command([STARTBYTE,HARD_VERSION,ENDBYTE])
        time.sleep(0.5)
        d = self.serial.read(19)
        s = []
        if d is not  None: 
            def split_bytes_data(data, packet_size):
                # Split the bytes object into packets of the specified size
                packets = [data[i:i+packet_size] for i in range(0, len(data), packet_size)]
                return packets
            ds = split_bytes_data(d,6)
            for i in range(1,len(ds)):
                   s.append(str(ds[i],'latin-1'))
            return "".join(s)

    def multiple_read(self):
        data = self.send_command([STARTBYTE, MULTIPLE_READ, ENDBYTE])

    def stop_read(self):
        data = self.send_command([STARTBYTE, STOP_READ, ENDBYTE])
    
    def setRegion_EU(self):
        data = self.send_command([STARTBYTE, SET_REGION_EU, ENDBYTE])
        time.sleep(0.5)
        rec_data = self.serial.read(24)
        #print(rec_data)    
    
    def setRegion_US(self):
        data = self.send_command([STARTBYTE, SET_REGION_US, ENDBYTE])
        time.sleep(0.5)
        rec_data = self.serial.read(24)
        #print(rec_data)
        
    def getTransmit_Power(self):
        data = self.send_command([STARTBYTE, GET_TRANSMIT_PWR, ENDBYTE])
        time.sleep(0.5)
        rec_data = self.serial.read(24)
        print(rec_data)
        
    def single_read(self):
        data = self.send_command([STARTBYTE, SINGLE_READ, ENDBYTE])
        time.sleep(0.5)
        rec_data = self.serial.read(24)
        #print(rec_data)
        if rec_data is not None and len(rec_data)>22:
            if rec_data[0] != 0xbb or rec_data[23] != 0x7e or rec_data[1] != 0x02:
                return None        
            return ['{:02x}'.format(x) for x in rec_data]
            
