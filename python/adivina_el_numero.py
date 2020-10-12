import random
def azar (numero):
    contador = random.randint (1,10)
    return contador 

def run():
    numero = 0
    validador =1
    contador = azar(numero)    
    #menu = """
    #Bienvenido al Adivina el Numero 
    #Estas son las reglas 
    #1 - Tienes 20 Intentos 
    #2 - Solo es 1 numero entre el 1 y el 10 
    #
    #Elige una opción: """
    
    while numero < validador:
        comparador = int (input ("ingrese un numero : "))
        if comparador == contador:
            print ("Felicidades encontraste el numero")
            break
        elif comparador > contador:
            print ("Intenta con un numero menor")
        else:
            print ("intenta con un numero mayor ")


if __name__ == "__main__":
    run()