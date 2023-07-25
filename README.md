# UHF_Reader_Pico_W_Software
<img src="https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/images/UHF%20Reader%20banner.jpg">

This github page provides a getting started guide and other working details for the UHF reader for Pico W. The UHF Reader for Pico W is a rapid multi-tag reading device for efficient and effective inventory management.

### Features:
- UHF Reader for Pico Powered by Pico W 
- Onboard High-performance UHF RFID reader module
- 24 hours x 365 days’ work normally
- 1.14” TFT display for visual interaction
- Multi-tone Buzzer onboard for Audio alerts
- Micro USB for programming and Type C for power.
- Drag-and-drop programming using mass storage over USB
- Onboard 3 user programmable buttons and reset button
- SD card slot for storage and data transfer
- Battery power and charging circuit for portable use
- Status LED for Power and Battery charging available
- Multipurpose GPIOs breakout for interfacing external peripherals
- SWD pins breakout for serial debugging 
- Compatible with Micropython, circuitpython and Arduino for programming.

### Specifications:
- RP2040 microcontroller is dual-core Arm Cortex-M0+ processor, 2MB of onboard flash storage, 264kB of RAM with WiFi and BLE support.
- Operating voltage of pins 3.3V and board supply 5V
- Display resolution 240 × 135 pixels
- ST7789 display driver
- UHF Module: 

## Getting Started with UHF Reader for Pico W
### Hardware Overview
#### Pinout
<img src="https://github.com/sbcshop/ReadPi_RFID_Software/blob/main/images/ReadPi_RFID%20pinout.jpg">

- (1) 1.3” Display


#### GPIO Pins Detail
<img src="https://github.com/sbcshop/ReadPi_RFID_Software/blob/main/images/READPI%20GPIO%20PINS%20breakout.jpg">

### Interfacing Details
- Pico W and UHF module interfacing
  
  | Pico W | UHF Module Pin | Function |
  |---|---|---|
  |GP4 (Tx) | UHF_RX | Serial UART connection |
  |GP5 (Rx) | UHF_TX  | Serial UART connection |
  |GP26 | EN  | UHF Reader enable pin, LOW to activate and HIGH to deactivate|

- Pico W and Display interfacing
  
  | Pico W | Display Pin | Function |
  |---|---|---|
  |GP6 | SCLK | Clock pin of SPI interface for display|
  |GP7 | DIN  | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP11 | DC | Data/Command pin of SPI interface|
  |GP13 | CS   | Chip Select pin of SPI interface for display|
  |GP14 | Reset | Display Reset Pin |
  |GP12 | BL | Backlight of Display |
  
- Pico W and micro SD card interfacing

  | Pico W | microSD Card | Function |
  |---|---|---|
  |GP18 | SCLK |Clock pin of SPI interface for microSD card |
  |GP19 | DIN  | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP16 | DOUT | MISO (Master IN Slave OUT) data pin of SPI interface|
  |GP17 | CS   | Chip Select pin of SPI interface for SDcard|

- Buttons, Buzzer and LED Interfacing with Pico W
  | Pico W | Buttons | Function |
  |---|---|---|
  |GP10 | BT2 | programmable button |
  |GP9 | BT3 | programmable button |
  |GP8 | BT4 | programmable button |
  |GP22 | Buzzer | Buzzer positive |
  |GP25 | LED | OnBoard LED pin of Pico W  |
 
- Breakout GPIOs
  | Pico W |Physical Pin | Multi-Function |
  |---|---|---|
  |GP0 | 1  | General IO / SPI0 RX / I2C0 SDA / UART0 TX |
  |GP1 | 2 | General IO / SPI0 CSn / I2C0 SCL / UART0 RX |
  |GP2 | 4 | General IO / SPI0 SCK / I2C1 SDA |
  |GP3 | 5 | General IO / SPI0 TX / I2C1 SCL |
  |GP21 | 27 | General IO / I2C0 SCL |
  |GP20 | 26 | General IO / I2C0 SDA |
  |GP28| 34 | General IO / ADC2 / SPI1 RX |
  |GP15| 20 | General IO / SPI1 TX / I2C1 SCL|


### 1. Step to install boot Firmware
   - Every UHF reader board will be provided with boot firmware already installed, so you can skip this step and directly go to step 2.
   - If in case you want to install firmware for your board, Push and hold the BOOTSEL button and plug your Pico W into the USB port of your computer. Release the BOOTSEL button after your Pico is connected.
   <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif">
   
   - It will mount as a Mass Storage Device called RPI-RP2.
   - Drag and drop the MicroPython UF2 - [Boot firmware](https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/uhfreader_picow_firmware.uf2) file provided in this github onto the RPI-RP2 volume. Your Pico will reboot. You are now running MicroPython on Pico W of UHF Reader.

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect UHF Reader board to laptop/PC.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
     
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
      
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/examples/onboard_ledBlink.py), then click on the green run button to make your script run on board.
     
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up board and it should run your script, go to step 3. Once you have transferred your code to the board, to see your script running, just plug in power either way using micro USB or via Vin, both will work.

### 3. How to move your script on Pico W of Board
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as main.py
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
      In similar way you can add various python code files to Pico. Also you can try out sample codes given here in [examples folder](https://github.com/sbcshop/ReadPi_RFID_Software/tree/main/examples). 
   
   - But in case if you want to move multiple files at one go, example suppose you are interested to save library files folder into Pico W, below image demonstrate that
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />
   
**NOTE: Don't rename _lib_ files** or and other files, only your main code script should be rename as main.py for standalone execution without Thonny.


### Example Codes
   Save whatever example code file you want to try as **main.py** in **Pico W** as shown in above [step 3](), also add related lib files with default name.
   In [example](https://github.com/sbcshop/UHF_Reader_Pico_W_Software/tree/main/examples) folder you will find demo example script code to test onboard components of board like 
   - [Buzzer test](https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/examples/BuzzerDemo.py) : code to test onboard Buzzer
   - [SD card demo](https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/examples/sdcard_demo.py) : code to test onboard micro SD card interfacing, [sdcard.py](https://github.com/sbcshop/UHF_Reader_Pico_W_Software/blob/main/examples/sdcard.py) lib file is required for the code to run successfully.
   - [UHF_Module Demo]() : testing onboard UHF module, this code will need lib file [uhf.py]()
   
   Using this sample code as a guide, you can modify, build, and share codes!!  
   
## Resources
  * [Schematic](https://github.com/sbcshop/UHF_Reader_Pico_W_Hardware/blob/main/Design%20Data/UHF%20Reader%20for%20Pico%20W%20SCH.pdf)
  * [Hardware Files](https://github.com/sbcshop/UHF_Reader_Pico_W_Hardware)
  * [Step File](https://github.com/sbcshop/UHF_Reader_Pico_W_Hardware/blob/main/Mechanical%20Data/Step%20UHF%20reader%20for%20pico%20.step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related Products
   * [UHF Reader for ESP32](https://shop.sb-components.co.uk/products/readpi-an-rfid-nfc-reader-powered-with-raspberry-pi-pico-w?variant=40478483087443) - UHF Reader powered by ESP32 S3 WROOM - 1
   * [Ardi UHF Shield](https://shop.sb-components.co.uk/products/ardi-uhf-shield-for-arduino-uno?variant=40791294836819) - UHF based shield with Oled display and Buzzer onboard
   * [UHF Lite HAT](https://shop.sb-components.co.uk/products/uhf-rfid-lite-hat) - Raspberry Pi Version
   * [UHF Lite Expansion for Raspberry Pi Pico](https://shop.sb-components.co.uk/products/uhf-rfid-for-pico?_pos=5&_sid=75312e089&_ss=r): UHF Lite Expansion to use with Pico/ Pico W

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
