import random
def generador_contrasena():
    mayus= ['A','B','C','D','E','F','G']
    minus= ['a','b','c','d','e','f','g']
    numbe= ['1','2','3','4','5','6','7','8','9','0']
    simbo= ['!','$','&','(',')']
    caracteres= mayus+minus+numbe+simbo
    contrasena= []
    for i in range (15):
        caracter_randow= random.choice(caracteres)
        contrasena.append (caracter_randow)

    contrasena= "".join (contrasena)
    return contrasena

def run():
    contrasena= generador_contrasena()
    print ('tu nueva contrasena es: ' + contrasena)


if __name__ == "__main__":
    run ()