#ArduinoControl

import serial
import curses, time
ser = serial.Serial('/dev/ttyUSB0',9600)

key = ''

def input_key(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getch()
            if ch in range(32, 127): break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)

while key.upper() != 'Q':
        
    key = input_key('-')
        
    if key.upper() == 'W':
        ser.write('w'.encode())



    
