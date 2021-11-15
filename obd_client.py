from time import sleep
import RPi.GPIO as GPIO
import serial
ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=1)
ser.write(b'ATZ\r')
data = ser.read(100)

ser.write(b'ATE0\r')
data = ser.read(100)

ser.write(b'ATH1\r')
data = ser.read(100)

ser.write(b'ATL0\r')
data = ser.read(100)

ser.write(b'0100\r')
data = ser.read(100)

while data.decode()[0:24] != "7E8 06 41 00 98 3B A0 13":
    ser.write(b'0100\r')
    data = ser.read(100)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

while True:
    ser.write(b'010D1\r')
    speed_data = ser.read(100)
    if len(speed_data) == 19:
        vehicle_speed = int(speed_data[13:15], base=16)
        print(vehicle_speed)
        if vehicle_speed > 20:
            print("Turn OFF parking sensor")
            GPIO.output(11, GPIO.LOW)
        else:
            print("Turn ON parking sensor")
            GPIO.output(11, GPIO.HIGH)
    sleep(1)
