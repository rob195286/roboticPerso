import serial


class ArduinoConnexion(object):
    """
        Class permettant de créer une connexion série avec le robot.
    """
    def __init__(self, periph = "/dev/ttyACM1", baudrate = 9600, to = 1):
        self.__serial = serial.Serial(periph, baudrate, timeout=to)        

    def sendData(self, data):
        # Encode en binaire chaque éléments de data séparément pour l'envoyer
        # à l'arduino car impossible de faire cette opération sur toute une liste en même temps.
        self.__serial.write(data.encode('ascii'))
