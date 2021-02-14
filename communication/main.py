from communication import ArduinoConnexion 
from time import sleep


avant = 'a'
tourner = 'b'

ardConn = ArduinoConnexion()
x=0

while(x<3):
    sleep(2)
    print(avant)
    ardConn.sendData(avant)
    sleep(2)
    ardConn.sendData(tourner)
    print(tourner)
    x += 1
