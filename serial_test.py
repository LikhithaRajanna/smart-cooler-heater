import serial
import time

try:
    ser = serial.Serial(
                      'COM3',
                      baudrate = 9600,
                      parity=serial.PARITY_NONE,
                      stopbits=serial.STOPBITS_ONE,
                      bytesize=serial.EIGHTBITS,
                      timeout=1
                      )
    time.sleep(1)
except Exception as e:
    ser = None
    print("Serial Error:", e)

def Send(temp):
    temp = str(temp)
    if ser is not None and ser.is_open:
        ser.write(str.encode(temp))
        print("Data sent : ", temp)
    else:
        print("Serial not connected, could not send : ", temp)
