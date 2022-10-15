import serial
import time

arduino = serial.Serial('COM5', 9600)

while True:
    linha = str(arduino.readline())
    umidade: float = linha
    print(umidade)

    time.sleep(10)
