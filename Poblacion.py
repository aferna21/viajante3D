import random
from Cromosoma import *

class Poblacion():
    
    #cromosomas = array de objetos tipo Cromosoma
    #funcion generarPoblacion es el constructor de la clase poblacion
    def __init__(self, tam):
        self.cromosomas = []
        for i in range(tam):
            cromosoma = Cromosoma([random.randrange(2), random.randrange(2), random.randrange(2), random.randrange(2), random.randrange(2), random.randrange(2), random.randrange(2), random.randrange(2)]) 
            self.cromosomas.append(cromosoma)

    def getCromosomas(self):
        return self.cromosomas


    def devuelveAptitudes(self):
        aptitudes = []
        for i in self.cromosomas:
            aptitudes.append(i.aptitud)
        return aptitudes

    def seleccionar(self):
        aptitudessumadas = []
        nuevapoblacion = []
        for i in range(len(self.cromosomas)):
            aptitudessumadas.append(self.cromosomas[i].aptitud)
            if i != 0:
                aptitudessumadas[i] += aptitudessumadas[i-1]
        
        #cuidado con los limites del random y el > del while, comprobar luego
        for i in range(len(self.cromosomas)):
           aleatorio = random.randrange(aptitudessumadas[len(aptitudessumadas)-1])
           j = 0
           while aleatorio > aptitudessumadas[j]:
               j = j + 1
           nuevapoblacion.append(self.cromosomas[j])

        self.cromosomas = nuevapoblacion
        


    def esImpar(self):
        return len(self.cromosomas) % 2 == 1

    def getMejorCromosoma(self):
    	cromosoma = self.cromosomas[0]
    	for i in self.cromosomas:
    		if i.aptitud > cromosoma.aptitud:
    			cromosoma = i

    	return cromosoma

    def cruzar(self):
        if self.esImpar():
            bitAcortar = (len(self.cromosomas[0].bits) - 1) / 2
        else:
            bitAcortar = len(self.cromosomas[0].bits) / 2
        mejor = self.getMejorCromosoma()
        tam = len(self.cromosomas[0].bits)
        nuevapoblacion = []
        while(len(self.cromosomas) > 1):
            c1 = self.cromosomas.pop()
            print(f"Cromosoma 1 escogido: {c1.bits}")
            c2 = self.cromosomas.pop()
            print(f"Cromosoma 2 escogido: {c2.bits}")
            bitshijo1 = []
            bitshijo2 = []
            for i in range(tam):
                if i < bitAcortar:
                    bitshijo1.append(c1.bits[i])
                    bitshijo2.append(c2.bits[i])
                else:
                    bitshijo1.append(c2.bits[i])
                    bitshijo2.append(c1.bits[i])
            cfinal1 = Cromosoma(bitshijo1)
            cfinal2 = Cromosoma(bitshijo2)
            print(f"Hijo 1: {cfinal1.bits}\nHijo 2:{cfinal2.bits}")
            nuevapoblacion.append(cfinal1)
            nuevapoblacion.append(cfinal2)

        if len(self.cromosomas) == 1:
        	nuevapoblacion.append(mejor)

        self.cromosomas = nuevapoblacion

    def evaluar(self):
        for i in self.cromosomas:
            i.evaluar()


    def toString(self):
    	i = 0
    	for j in self.cromosomas:
    		print(f"Cromosoma {i}: {j.bits}. Aptitud: {j.aptitud}")
    		i += 1

    def mutar(self, probabilidad):
        for i in self.cromosomas:
            i.mutar(probabilidad)

       

