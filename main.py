##ALGORITMO GENETICO##
from Poblacion import *




#*********************FUNCION MAIN**********************
#1)Generar poblacion inicial
print("\n\n*************GENERAR POBLACION Y EVALUAR*************")
poblacion = Poblacion(5)

#2)Evaluar
poblacion.evaluar()
poblacion.toString()
#3)Solucion suficiente (while)


#4)Seleccionar
poblacion.seleccionar()
print("\n\n*************SELECCION*************")
poblacion.toString()


#5)Cruzar
poblacion.cruzar()
print("\n\n*************CRUZAMIENTO*************")
poblacion.toString()