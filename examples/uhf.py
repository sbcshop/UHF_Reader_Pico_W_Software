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
HARD_VERSION  ='0300010004'
MULTIPLE_READ ='27000322271083'
SINGLE_READ   ='22000022'
STOP_READ     ='28000028'

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

    def single_read(self):
        data = self.send_command([STARTBYTE, SINGLE_READ, ENDBYTE])
        time.sleep(0.5)
        rec_data = self.serial.read(24)
        if rec_data is not None and len(rec_data)>22:
            if rec_data[0] != 0xbb or rec_data[23] != 0x7e or rec_data[1] != 0x02:
                return None        
            return ['{:02x}'.format(x) for x in rec_data]
            
