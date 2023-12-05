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

STARTBYTE     ='BB00' # combine Header + Type
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
    
    #####################################################
    def calculate_checksum(self,data):
        checksum = 0
        for byte in data:
            checksum += byte
        checksum_1 = (checksum) % 256
        return checksum

    def calculation(self,Data):
        bin_data1 = binascii.unhexlify(Data)
        chk_1 = (hex(self.calculate_checksum(bin_data1)))
        #print("checksum",chk_1)
        if len(chk_1) == 5:
            return str(chk_1[3:])
            
        elif len(chk_1) == 4:
            return str(chk_1[2:])
        
        else:
            return '0'+ str(chk_1[3:])
    ######################################################

    def send_command(self, data):
        Data = ''.join(data)
        #print(Data)
        bin_data = binascii.unhexlify(Data)
        response = self.serial.write(bin_data)


    
    ####################################################################
    def Set_select_pera(self,tag_uid):          
        #fig = '0C00130'+Memory_bank+'000000206000'+ tag_uid
        fig = '0C001300000000206000'+ tag_uid
        dat = self.calculation(fig)
        dat1 = STARTBYTE+fig+dat+ENDBYTE
        #print('card select = ',dat1)
        data = self.send_command(dat1)
        time.sleep(0.2)
        rec_data = self.serial.read(16)
        s = []
        if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                #print('select response = ',a)
                if "".join(a) == 'bb010c0001000e7e':   
                     return 'Select sucessfull'
                else:
                    return 'invalid'
                
    
    def Read_tag_data(self,memory_bank):
        fig = '390009000000000'+memory_bank+'00000008'   
        dat = self.calculation(fig)
        dat1 = STARTBYTE+fig+dat+ENDBYTE
        #print("dat1 = ",dat1)
        
        data = self.send_command(dat1)
        time.sleep(0.2)
        rec_data = self.serial.read(40)
        s = []
        if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                print(a)
                if "".join(a) == 'bb01ff0001090a7e':
                     return 'No card is there'
                    
                elif "".join(a) != 'bb01ff0001090a7e':
                    if memory_bank == '2':
                        return "".join(a)[40:72]
                        
                    elif memory_bank == '3':
                        return "".join(a)[40:70]
                    
                    elif memory_bank == '1':
                        return "".join(a)[48:72]
                    


    def Write_tag_data(self,data_w,memory_bank):  
        fig = '490019000000000'+memory_bank+'00000008'+ data_w      
        dat = self.calculation(fig)
        dat1 = STARTBYTE+fig+dat+ENDBYTE
        print('write1111 = ',dat1)
        data = self.send_command(dat1)
        time.sleep(0.2)
        rec_data = self.serial.read(23)
        s = []
        if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                print('write data = ',a)
                if "".join(a) == 'bb01ff000110117e':  
                     return 'Write card failed,No tag response'
                    
                elif "".join(a) == 'bb01ff000117187e':   
                     return 'Command error'#'Data length should me should be integer multiple words'
                    
                else:
                     return 'Card sucessfull write'
    ################################################################################


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
        data = self.send_command([STARTBYTE, write_tag, ENDBYTE])
        time.sleep(0.5)
        rec_data = self.serial.read(24)
        #print(rec_data)
    
    def getTransmit_Power(self):
        data = self.send_command([STARTBYTE, GET_TRANSMIT_PWR, ENDBYTE])
        time.sleep(0.5)
        rec_data = self.serial.read(24)
        return rec_data
        
    def single_read(self):
        data = self.send_command([STARTBYTE, SINGLE_READ, ENDBYTE])
        time.sleep(0.5)
        rec_data = self.serial.read(24)
        #print(rec_data)
        if rec_data is not None and len(rec_data)>22:
            if rec_data[0] != 0xbb or rec_data[23] != 0x7e or rec_data[1] != 0x02:
                return None        
            return ['{:02x}'.format(x) for x in rec_data]
            
