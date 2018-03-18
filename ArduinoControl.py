#ArduinoControl

import serial
ser = serial.Serial('/dev/ttyUSB0',9600)

key = ''



while key.upper() != 'Q':
        
    key = input('-')
        
    if key.upper() == 'W':
        ser.write('w'.encode())



    
