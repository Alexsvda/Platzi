#Curso de Introducción al Pensamiento computacional con Python
#Codigo reto 15 (Crear un programa que permita obtener la raiz cuadrada con diferentes metodos)
#Clase Funciones y Abstraccion 
#Profesor : David Aroesti

def aproximacion (objetivo): #metodo replicado
    objetivos = objetivo     #se cambia objetivos
    epsilon= 0.01
    paso = epsilon **2
    respuesta=0.0
    while abs (respuesta **2 - objetivos) >= epsilon and respuesta <=objetivo:
        respuesta +=paso
    if abs (respuesta **2 - objetivos) >=epsilon:
        print (f'no se encontro la raiz cuadrada de {objetivos}')
    else :
        print (f'la Raiz cuadrado de {objetivo} es {respuesta}')

def binario (objetivo):  #metodo replicado
    objetivos = objetivo #se cambia objetivo 
    epsilon=0.001
    bajo =0.0
    alto= max(1.0, objetivos)
    respuesta =(alto+bajo)/2
    while abs (respuesta**2 - objetivos ) >= epsilon:
        print (f'bajo {bajo},alto {alto},respuesta {respuesta}')
    if respuesta **2 < objetivos:
        bajo = respuesta
    else:
        alto = respuesta
        respuesta = (alto+bajo)/2   
    print (f'La raiz cuadrada de {objetivos} es {respuesta}')

objetivo = int (input ('ingrese un valor: '))
tipo= int (input('que modo desea (1- busqueda binaria - 2- busqueda aproximacion) ingrese su opcion= '))
    
if tipo == 1:
    aproximacion (objetivo)
    salida = 0 
elif tipo ==2:
    aproximacion (objetivo)
    salida = 0
else:
    print (f'Opcion no valida') #se agrega una validación 
# se evita reutilizar codigo o reescribirlo por lo que se tomo solo lo realizado antes en clases anteriores por practicas.