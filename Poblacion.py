import random
from Cromosoma import *
import copy 
#el copy es para crear nuevos objetos, no pasarles la referencia 
class Poblacion():
    

    def __init__(self, num_individuos, num_puntos):
        self.cromosomas = []
        for i in range(num_individuos):
            cromosoma = Cromosoma(num_puntos, None)
            self.cromosomas.append(cromosoma)



    def devuelveAptitudes(self):
        aptitudes = []
        for i in self.cromosomas:
            aptitudes.append(i.aptitud)
        return aptitudes

    
    def toString(self):
    	i = 0
    	for j in self.cromosomas:
    		print(f"Cromosoma {i}: {j.camino}. Aptitud: {j.aptitud}")
    		i += 1


    def seleccionar(self):
        aptitudessumadas = []
        nuevapoblacion = []
        mejor_cromosoma = self.getMejorCromosoma()
        for i in range(len(self.cromosomas)):
            aptitudessumadas.append(self.cromosomas[i].aptitud)
            if i != 0:
                aptitudessumadas[i] += aptitudessumadas[i-1]
        #print("La poblacion actual es: ")
        #self.toString()
        #print("La lista de aptitudes sumadas para la ruleta con pesos es: ")
        #print(aptitudessumadas)
        for i in range(len(self.cromosomas) - 1): 
           aleatorio = random.uniform(0, aptitudessumadas[-1])
           #print(f"El aleatorio ha sido {aleatorio}")
           j = 0
           while aleatorio > aptitudessumadas[j]:
               j = j + 1
           nuevapoblacion.append(copy.deepcopy(self.cromosomas[j]))
           #print(f"El cromosoma añadido a la nueva población es: {self.cromosomas[j].camino} de la posicion en poblacion {j}")

        nuevapoblacion.append(copy.deepcopy(mejor_cromosoma))
        self.cromosomas = nuevapoblacion
        

    
    def esImpar(self):
        return len(self.cromosomas) % 2 == 1

    def getMejorCromosoma(self):
    	cromosoma = self.cromosomas[0]
    	for i in self.cromosomas:
    		if  i.aptitud != None and i.aptitud > cromosoma.aptitud:
    			cromosoma = i

    	return cromosoma

    def getMediaAptitudes(self):
        suma = 0
        tam = len(self.cromosomas)
        for i in self.cromosomas:
            suma += i.aptitud
        return suma/tam


    def evaluarPoblacion(self, puntos):
        for i in self.cromosomas:
            i.evaluar(puntos)

    #hay que evitar que mute el mejor, pero solo uno de ellos.
    def mutarPoblacion(self, probabilidad):
        mejor_cromosoma = self.getMejorCromosoma()
        for i in self.cromosomas:
            if not(i is mejor_cromosoma):
                i.mutar(probabilidad)


    def cruzar(self):
        mejor_cromosoma = self.getMejorCromosoma()
        nueva_poblacion = [mejor_cromosoma]
        self.cromosomas.remove(mejor_cromosoma)


        tam_cromosoma = len(self.cromosomas[0].camino)
        if tam_cromosoma == 3:
            particion1 = 1
            particion2 = 2
        else:
            mitad_cromosoma = round(tam_cromosoma/2)-1
            particion1 = random.randint(1, mitad_cromosoma)
            particion2 = random.randint(mitad_cromosoma+1, tam_cromosoma-2)

        while(len(self.cromosomas) > 1):
            cromosoma1 = self.cromosomas.pop()
            cromosoma2 = self.cromosomas.pop()
            #print(f"Cromosoma 1 escogido: {cromosoma1.camino}\nCromosoma 2 escogido: {cromosoma2.camino}")

            #division de cromosoma1
            parte_intermedia_cromosoma1 = cromosoma1.camino[particion1:particion2]
            puntos_restantes_cromosoma1 = []
            for i in parte_intermedia_cromosoma1:
                cromosoma1.camino.remove(i)
            puntos_restantes_cromosoma1 = cromosoma1.camino
            #print(f"Cromosoma 1 -> Parte intermedia: {parte_intermedia_cromosoma1}, bits restantes: {puntos_restantes_cromosoma1}")

            #division de cromosoma2
            parte_intermedia_cromosoma2 = cromosoma2.camino[particion1:particion2]
            puntos_restantes_cromosoma2 = []
            for i in parte_intermedia_cromosoma2:
                cromosoma2.camino.remove(i)
            puntos_restantes_cromosoma2 = cromosoma2.camino
            #print(f"Cromosoma 2 -> Parte intermedia: {parte_intermedia_cromosoma2}, bits restantes: {puntos_restantes_cromosoma2}")

        
            hijo1 = []
            hijo2 = []
            i = 0
            while i < tam_cromosoma:
                if i >= particion1 and i < particion2:
                    if parte_intermedia_cromosoma2[0] in hijo1:
                        indice = hijo1.index(parte_intermedia_cromosoma2[0])
                        hijo1[indice] = None
                    hijo1.append(parte_intermedia_cromosoma2.pop(0))
                    if parte_intermedia_cromosoma1[0] in hijo2:
                        indice = hijo2.index(parte_intermedia_cromosoma1[0])
                        hijo2[indice] = None
                    hijo2.append(parte_intermedia_cromosoma1.pop(0))
                else:
                    if not(puntos_restantes_cromosoma1[0] in hijo1): hijo1.append(puntos_restantes_cromosoma1[0])
                    del puntos_restantes_cromosoma1[0]
                    if not(puntos_restantes_cromosoma2[0] in hijo2): hijo2.append(puntos_restantes_cromosoma2[0])
                    del puntos_restantes_cromosoma2[0]
                i += 1
            
            #relleno con las puntos que falten
            for i in range(tam_cromosoma):
                if not(i in hijo1) and (len(hijo1) != tam_cromosoma or None in hijo1):
                    if None in hijo1:
                        indice = hijo1.index(None)
                        hijo1[indice] = i
                    else:
                        hijo1.append(i)
                if not(i in hijo2) and (len(hijo2) != tam_cromosoma or None in hijo2):
                    if None in hijo2:
                        indice = hijo2.index(None)
                        hijo2[indice] = i
                    else:
                        hijo2.append(i)
            #print(f"Hijo 1: {hijo1}\nHijo 2: {hijo2}")
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)
        
        #si falta uno, anado el mejor otra vez
        if len(self.cromosomas) == 1:
            nueva_poblacion.append(copy.deepcopy(mejor_cromosoma))

        #hacer nueva_poblacion una lista de objetos de tipo Cromosoma
        #el if es porque hemos anadido objetos de tipo cromosoma y listas de puntos.
        nueva_poblacion_cromosomas = []

        for i in nueva_poblacion:
            if type(i) is Cromosoma:
                nueva_poblacion_cromosomas.append(i)
            else:
                nueva_poblacion_cromosomas.append(Cromosoma(None, i))
        
        self.cromosomas = nueva_poblacion_cromosomas


        

       

