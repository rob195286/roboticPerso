from time import sleep
from serial import *

def sendData(data, periph = "/dev/ttyACM0", baudrate = 9600):
    # Encode en binaire chaque éléments de data séparément pour l'envoyer
    # à l'arduino car impossible de faire cette opération sur toute une liste en même temps.
    ser = Serial(periph, baudrate) 
    dataStr = "<,"
    for elem in data:
        dataStr += elem+","
    dataStr += ">"
    print(dataStr)
    ser.write(dataStr.encode('ascii'))
    
avant = ['a', '2500', '70','17']
avant2 = ['2500', '70','17', 'q']
tourner = ['b', '600', '700']
tourner = ['600', '700', '14']


sendData(tourner)


