import serial
import time


def talkToServo(object_width, port_id):
    arduino = serial.Serial(port=port_id, timeout=0)
    time.sleep(2)
    arduino.write(str.encode(str(round(object_width, 0)) + "\n"))
    # arduino.write(str.encode("\n"))
    print(f"Communicate with arduino: {object_width}")
