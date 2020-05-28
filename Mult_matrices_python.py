# -*- coding: utf-8 -*-
#from string import uppercase

from argparse import ArgumentParser
import sys
#import numpy


# ArgumentParser con una descripción de la aplicación
parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')


# Argumento posicional con descripción
parser.add_argument('fichero', help='ayuda del fichero')

# Por último parsear los argumentos
args = parser.parse_args()

d=open(args.fichero,'r+')
datos=d.readlines()

matrizA=[]  # Matriz Original
matrizB=[]	 # MatrizMultiplicada

numfilas=len(datos)
numcolumnas=len(datos[1].split(";"))-1

if numfilas!=numcolumnas:
 print("No tiene solucion debe de ser una matriz cuadrada")
else: 
 for i in range(numfilas):
  matrizA.append([0]*numcolumnas)
  matrizB.append([0]*numcolumnas)
 for j in range(numfilas):
  a=datos[j].split(";")  
  for k in range(numcolumnas):
   try:
   # Acomodar los datos en la matrizA e inicializar matrizB
    matrizA[j][k]=float(a[k]);
    matrizB[j][k]=0; 
   except ValueError:
    print("datos invalidos")
   
 for i in range(numfilas):
  for j in range(numcolumnas):
   for k in range(numcolumnas):
    try:
	 # multiplicar
     matrizB[i][k]=matrizB[i][k]+(matrizA[i][j]*matrizA[j][k])
    except ValueError:
     print("Error al multiplicar")	

print ("Matriz Original")
print (matrizA)
print ("Matriz Multiplicada por si misma")
print (matrizB)
