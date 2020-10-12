#def imprimir_mensaje():
#    print ("Mensaje especial: ")
#    print ("Estoy aprendiendo a usar funciones ")
#
#imprimir_mensaje();
#imprimir_mensaje();

def conversación (mensaje):
    print("hola ")
    print ("como estas ")
    print (mensaje)
    print ("Adios")

opcion=int (input("Elige una opción 1,2,3: "))
if opcion ==1:
    conversación("Elegiste la opcion 1")
elif opcion ==2:
    conversación("Elegiste la opcion 2")
elif opcion ==3:
    conversación("Elegiste la opcion 3")
else:
    print ("Elige la opción conrrecta ")