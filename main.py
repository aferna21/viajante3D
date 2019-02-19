##ALGORITMO GENETICO##
from Poblacion import *
import time

"""
    def solucionSuficiente(self, cromosoma, porcentaje):
        puntosAptitud = self.aptitud * porcentaje / 100
        return abs(self.aptitud - cromosoma.aptitud) < puntosAptitud
"""
def mejorCromosoma(listacromosomas):
	mejorcromosoma = listacromosomas[0]
	for i in listacromosomas:
		if i.aptitud > mejorcromosoma.aptitud:
			mejorcromosoma = i
	return mejorcromosoma

def solucionSuficiente(mejorescromosomas, cromosomaactual, generaciones, porcentaje):
	mejor_cromosoma = mejorCromosoma(mejorescromosomas)
	puntos_aptitud = cromosomaactual.aptitud * porcentaje / 100
	ha_mejorado = abs(mejor_cromosoma.aptitud - cromosomaactual.aptitud) > puntos_aptitud
	supera_generaciones = len(mejorescromosomas) - mejorescromosomas.index(mejor_cromosoma) > generaciones
	return ha_mejorado and supera_generaciones


#*********************FUNCION MAIN**********************
#1)Generar poblacion inicial
print("\n\n*************GENERAR POBLACION Y EVALUAR*************")
poblacion = Poblacion(5)

#2)Evaluar
poblacion.evaluar()
poblacion.toString()


#3)Solucion suficiente (while)
mejores_generacion = []
mejores_generacion.append(poblacion.getMejorCromosoma())
numerogeneracion = 0
while not solucionSuficiente(mejores_generacion, poblacion.getMejorCromosoma(), 3, 5):
	time.sleep(2)
	numerogeneracion += 1
	print(f"\n\n\n\nGeneracion {numerogeneracion}. El mejor cromosoma es {mejorCromosoma(mejores_generacion).bits} con aptitud {mejorCromosoma(mejores_generacion).aptitud} de la generacion {mejores_generacion.index(mejorCromosoma(mejores_generacion)) + 1}")
	#4)Seleccionar
	print("\n\n*************SELECCION*************")
	poblacion.seleccionar()
	poblacion.toString()


	#5)Cruzar
	print("\n\n*************CRUZAMIENTO*************")
	poblacion.cruzar()
	poblacion.toString()


	#6)Mutar
	print("\n\n*************MUTACION*************")
	poblacion.mutar(5)
	poblacion.toString()

	#7)Evaluar
	print("\n\n*************EVALUACION*************")
	poblacion.evaluar()
	poblacion.toString()
	mejores_generacion.append(poblacion.getMejorCromosoma())

print(f"Encontrada solucion suficiente. El mejor cromosoma es {mejorCromosoma(mejores_generacion).bits} con aptitud {mejorCromosoma(mejores_generacion).aptitud} de la generacion {mejores_generacion.index(mejorCromosoma(mejores_generacion)) + 1}")
