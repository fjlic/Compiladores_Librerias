# -*- coding: utf-8 -*-
#from string import uppercase


from argparse import ArgumentParser
import sys
import os
import os.path as path


def libreria_valida(cadena):
 if cadena in lib_estandar:	
  return True  
 arreglo=str(cadena.replace('"', ''))
 if arreglo!="null":
  if path.exists(arreglo):
#   print ("existe libreria")
   d=open(arreglo,'r+')
   matriz_datos_libreria.append(d.readlines())
   d.close()
   return True
  return False 
 else:
  print ("no funciono leer libreria")
  return False
  
def remplaza(linea,cons,valor,linea_termino):
#linea= liinea a partir  de donde se va remplazar la constante
#cons= constante que se va a remplazar
#valor= valor de la constante
#linea de termino= linea hasta la cual se realizara el remplazo (si se encuentra)
 inicio=linea
 cons=str(cons)
#define si tiene  limite  de linea de remplazo
 if linea_termino!=-1:
  # si tiene se asigna
  termino=linea_undef[linea_termino]
 else:
 # si no  hasta la ultima linea del codigo
  termino=len(matriz_linea)

# se recorre el codigo desde la linea de inicio hasta la de termino
 for i in range(inicio,termino):
  comillas=0 
  numelementos=len(matriz_linea[i])
  for j in range(numelementos):
   string5=matriz_linea[i][j]
  # se buscan comillas para saber si la connstante esta dentro de string
   if '"' in string5:  # si la constante esta dentro de comillas se ignora
    if comillas==1:
     comillas=0
    else:
     comillas=1
    if string5.count('"')==2:
     comillas=0

   if cons in string5 and comillas==0:
#    print("se encontro  la constante termino a evaluar")
#    print(cons)
    if string5 in palabras_reservadas:
     print("palabra reservada")
    else:
     string7=string5.split(cons)
#     print("se realiza la separacion")
#     print(string7)
     if string7[0]=="" or string7[1]=="":
      string6=string5.replace(cons,valor)
     else:
      string6=string5
     matriz_linea[i][j]=string6
#   print("----------------------")

 return False 




def evalua_if(linea_1):
 linea=''.join(linea_1)
# print(linea)
 while '#if' in linea:
  linea=linea.replace('#if','')
  print(linea)
 if linea=="0" or linea==False:
  return False
 if linea.isdigit() or linea=="1":
  return True 
 if "==" in linea:
#  print("igual")
  compara=linea.split("==")
  try:
   num1=float(compara[0])
   num2=float(compara[1])
   if num1==num2:
    return True

  except ValueError:
   return False
  else:
   return False
 if "<=" in linea:
  print("menor o igual")
  compara=linea.split("<=")
  try:
   num1=float(compara[0])
   num2=float(compara[1])
   if num1<=num2:
    return True
  except ValueError:
   return False
  else:
   return False
 if ">=" in linea:
  print("mayor o igual")
  compara=linea.split(">=")
  try:
   num1=float(compara[0])
   num2=float(compara[1])
   if num1>=num2:
    return True
  except ValueError:
   return False
  else:
   return False
 if ">" in linea:
  print("mayor ")
  compara=linea.split(">")
  try:
   num1=float(compara[0])
   num2=float(compara[1])
   if num1>num2:
    return True
  except ValueError:
   return False
  else:
   return False
 if "<" in linea:
  print("menor o igual")
  compara=linea.split("<")
  try:
   num1=float(compara[0])
   num2=float(compara[1])
   if num1<num2:
    return True
  except ValueError:
   return False
  else:
   return False
   
 if linea!="null":
#  print("linea")
#  print(linea)
  return True
 return False


# ArgumentParser con una descripción de la aplicación
parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')


# Argumento posicional con descripción
parser.add_argument('fichero', help='ayuda del fichero')

# Por último parsear los argumentos
args = parser.parse_args()

d=open(args.fichero,'r+')
datos=d.readlines()
d.close()

linea_include=[]  #almacena  las lineas que son librerias
linea_libreria_valida=[]  # almacena si las lineas de libreria son validas
linea_define=[]  # almacena  las lineas que son #define
directivas_define=[]	 
directivas_define_valor=[]
linea_undef=[]  # almacena  las lineas que son #undef
directivas_undefine=[] # guarda el dato del undef 
linea_endif=[]  # almacena  las lineas que son end #if
linea_if=[]  # almacena  las lineas que son #if
linea_if_evaluado=[] # guarda el valor del if evaluado (verdadera o falso)
linea_else=[]  # almacena  las lineas que son #else
linea_comentario=[] # almacena  las lineas que son comentario
encontar_main=[]
palabras_reservadas=["int","float", "main","print","scan",","]
forma_de_main=["main(){","main(){","main ( )","main()","main(){", "main(void){","main(void){"]
lib_estandar=["<stdio.h>","<stdlib.h>","<string.h>","<time.h>","<float.h>", "<assert.h>","<errno.h>"]
matriz_datos_libreria=[] #guarda la cadena que
numlineas=len(datos)
matriz_datos_libreria=[]
lineas_errores=[]


print ("leer archivo")
print (datos)
#print ("\n")
num_lineas_validas=-1
matriz_linea=[]  # tiene las palabrabras de cada  linea en un arreglo
linea_valida=0   # lineas que si tienen conenido
asigna_if_else=0 # se utilizan para la logica de asigancion de if
asigna_if_end=0 # se utilizan para la logica de asigancion de if
if numlineas!=0:
 for i in range(numlineas):
  if "\n" in datos[i]:
   datos[i]=datos[i].replace("\n","")
  if "\t" in datos[i]:
   datos[i]=datos[i].replace("\t"," ")
  # posibles lineas con una sola cadena 
  a=datos[i].count(" ")
  b=datos[i].count("else")
  c=datos[i].count("endif")
  d=datos[i].count("}")
  print (datos[i])
  #  si es una  llinea valida  empezara a hacer separaciones
  if a!=0 or b!=0 or c!=0 or d!=0:
   matriz_linea.append([0]*(a+1))
   num_lineas_validas=num_lineas_validas+1
   if a!=0:
    matriz_linea[linea_valida]=datos[i].split(" ")
    list=datos[i].split(" ")
   else:
    matriz_linea[linea_valida]=datos[i].split("\t")
   while '' in matriz_linea[linea_valida]:
    matriz_linea[linea_valida].remove('')
#   print (matriz_linea[linea_valida])
   tamlinea=len(matriz_linea[linea_valida])
   if tamlinea!=0:
   
    string1=matriz_linea[linea_valida][0]
    string2=matriz_linea[linea_valida][tamlinea-1]
# casos que solo necesitan una palabra
    if string1=="#endif":
     aux=linea_if[len(linea_if)-1+asigna_if_end]
     linea_endif.append([aux,num_lineas_validas])
     asigna_if_end=asigna_if_end-1
    if string1=="//":
     linea_comentario.append(num_lineas_validas)
    if string1=="#else":
     aux=linea_if[len(linea_if)-1+asigna_if_else]
     linea_else.append([aux,num_lineas_validas])
     asigna_if_else=asigna_if_end-1


# casos que se necesitan mas de dos palabras   
   if tamlinea>1:
    string3=matriz_linea[linea_valida][1] # ver si es main	o define o undef
 
    # revisa si es una direcciva del preprocesador
    if string1=="#include":
     linea_include.append(num_lineas_validas)
     res=libreria_valida(matriz_linea[linea_valida][1])
     linea_libreria_valida.append(res)
     if res==False:
      lineas_errores.append(num_lineas_validas)
	

    if string1=="#define":
     linea_define.append(num_lineas_validas)
     directivas_define.append(string3) # agrega el define
     if tamlinea>2:
      directivas_define_valor.append(matriz_linea[linea_valida][2]) # agrega el define
     else:
      directivas_define_valor.append("null")
      lineas_errores.append(num_lineas_validas)
	
    if str(string3) in forma_de_main:	
     encontar_main.append(num_lineas_validas)  
  
    if string1=="#undef":
     linea_undef.append(num_lineas_validas)
     directivas_undefine.append(string3)
    if string1=="#if":
     linea_if.append(num_lineas_validas)	
  
   linea_valida=linea_valida+1
    
  
else: 
 print("Error:archivo en blanco")	 

num=len(directivas_define)
j=0

# remplazo de las variables
while j!=num:
 if directivas_define[j] in directivas_undefine:
  linea_termino=directivas_undefine.index(directivas_define[j])
 else:  
  linea_termino=-1
 remplaza(linea_define[j],directivas_define[j],directivas_define_valor[j],linea_termino)
 linea_termino=0
 j=j+1


# evalua los if 
j=0
i=0
num=len(linea_if)
while i<num:
  string1=evalua_if(matriz_linea[linea_if[i]])
  linea_if_evaluado.append(string1)
  i=i+1


#------------- imprimir  datos obtenidos--------

print ("--------------------------")
print ("\nArchivo Leido:")
print (datos)
print ("\nCadena limpia:")
print (matriz_linea)
print ("\n-----procesamiento de lineas------")
print ("\nSe encontro #define en las lineas:")
print (linea_define)
print ("Las constantes son:")
print (directivas_define)
print ("Su respectivo valor es:")
print (directivas_define_valor)
print ("\nSe encontro #include en las lineas:")
print (linea_include)
print ("Se evaluo la libreria como:")
print (linea_libreria_valida)
print ("\nSe encontro comentarios en las lineas:")
print (linea_comentario)
print ("\nSe encontro if en las lineas:")
print (linea_if)
print ("Se evaluo cada if como:")
print (linea_if_evaluado)
print ("\nSe encontro  #if , #else en las lineas:")
print (linea_else)
print ("\nSe encontro  #if , #endif en las lineas:")
print (linea_endif)
print ("\nSe encontro #undef en las lineas:")
print (linea_undef)

print ("\nSe encontro main en la linea:")
print (encontar_main)

print ("---se adjunto la libreria----")
print ("datos libreria")
print (matriz_datos_libreria)

#------------- se  revisa que lineas se agrgaran al archivo de salida--------

# inicializa las lineas que llevara el codigo
num=len(matriz_linea)
lineas_imprimir=[]
for i in range(num):
 lineas_imprimir.append(i)
 
# elimina las lineas con #include
for i in range(len(linea_include)):
 lineas_imprimir.remove(linea_include[i])
 
# elimina las lineas con #define
for i in range(len(linea_define)):
 lineas_imprimir.remove(linea_define[i])
 
# elimina las lineas con comentarios
for i in range(len( linea_comentario)):
 lineas_imprimir.remove( linea_comentario[i])

# elimina las lineas con #undef
for i in range(len( linea_undef)):
 lineas_imprimir.remove( linea_undef[i]) 
  
# elimina las lineas con #if
for j in range(len( linea_if)):
 if linea_if[j] in lineas_imprimir:
  lineas_imprimir.remove(linea_if[j])
  
# elimina las lineas con #endif
for i in range(len(linea_endif)):
 if linea_endif[i][0] in lineas_imprimir:
  lineas_imprimir.remove(linea_endif[i][0])
 if linea_endif[i][1] in lineas_imprimir:
  lineas_imprimir.remove(linea_endif[i][1])

# elimina las lineas con #else
for i in range(len(linea_else)):
 if linea_else[i][0] in lineas_imprimir:
  lineas_imprimir.remove(linea_else[i][0])
 if linea_else[i][1] in lineas_imprimir:
  lineas_imprimir.remove(linea_else[i][1])

#cuenta si hay suficientes if end
if len(linea_if)!=len(linea_endif):
 lineas_errores.append(linea_if)
else:
#  empieza a evaluar si el codigo del if se incluye  dentro del codigo
 i=0
 while i<len(linea_else):
  inicio_if=linea_else[i][0]
  inicio_else=linea_else[i][1]
  # encontar el fin
  for j in range(len(linea_endif)):
   if linea_endif[j][0]==inicio_if:
    fin_if=linea_endif[j][1]
    linea_endif[j][1]=-1
    linea_endif[j][0]=-1
  for j in range(len(linea_if)):
   if linea_if[j]==inicio_if:
    valor_if=linea_if_evaluado[j]	

  if valor_if==True:
   for j in range(inicio_else,fin_if):
    if j in lineas_imprimir:
     lineas_imprimir.remove(j)
  else:
   for j in range(inicio_if,inicio_else):
    if j in lineas_imprimir:
     lineas_imprimir.remove(j)
  
  i=i+1
 i=0 
# compracion en if (sin else)
 while i<len(linea_endif):
  if linea_endif[i][0] !=-1:
   inicio_if=linea_endif[i][0]
   # encontar el fin
   fin_if=linea_endif[i][1]
   # encontrar el valor de if
   for j in range(len(linea_if)):
    if linea_if[j]==inicio_if:
     valor_if=linea_if_evaluado[j]	
   if valor_if==False:
    for j in range(inicio_if,fin_if):
     if j in lineas_imprimir:
      lineas_imprimir.remove(j)
  i=i+1

 

#crea archivo de salida
file = open("salida.c", "w")
num=len(matriz_datos_libreria)
i=0
j=0
while i<num:
 num_1=len(matriz_datos_libreria[i])
 while j <num_1:
  arreglo_1=matriz_datos_libreria[i][j].replace('\n', '')
  file.write(arreglo_1+ os.linesep)
  j=j+1
 i=i+1

print("num de lineas validas a imprimir")
print(lineas_imprimir)
num=len(lineas_imprimir)
i=0
while i<num:
 num_1=lineas_imprimir[i]
 string1=" ".join(matriz_linea[num_1])
 file.write(string1+ os.linesep)
 i=i+1
file.close()
