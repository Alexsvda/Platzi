def run ():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    print (mi_diccionario ['llave1'])
    print (mi_diccionario ['llave2'])
    print (mi_diccionario ['llave3'])

    poblacion = {
        'Argentina': 44900000,
        'Brasil': 50000000,
        'Chile': 1500000,
    }
    
    for pais in poblacion.keys():
        print (pais)
    for pais in poblacion.values():
        print (pais)
    for pais, poblacion in poblacion.items():
        print (pais + ' tiene ' + str(poblacion) + ' habitantes ')

if __name__ == "__main__":
    run()