import random

class Cromosoma():

    #bits= array de 0s y 1s
    #esta vacia porque no sabemos como vamos a crear los cromosomas
    def __init__(self, bits):
        self.bits = bits
        self.aptitud = 0

    def getAptitud(self):
        return self.aptitud

    def funcionEvaluacion(self):
        suma= 0
        for i in range(len(self.bits)):
            suma += self.bits[i]
        return suma

    def evaluar(self):
        self.aptitud = self.funcionEvaluacion()

    def solucionSuficiente(self, cromosoma, porcentaje):
        puntosAptitud = self.aptitud * porcentaje / 100
        return abs(self.aptitud - cromosoma.aptitud) < puntosAptitud

    def mutar(self, probabilidad):
        bitamutar = random.randrange(len(self.bits))
        aleatorio = random.randrange(101)
        if aleatorio >= probabilidad:
            self.bits[bitamutar] = abs(self.bits[bitamutar]-1)
