def run ():
    #for contador in range (1,1001):
    #    if contador %2 != 0:
    #        continue 
    #    print (contador)
     
    # for i in range (1,100001):
    #     print (i)
    #     if i == 5678:
    #         break   

    texto = input ("Ingrese un comentario : ")
    for letra in texto:
        print (letra)
        if letra == "o":
            break
        
if __name__ == "__main__":
    run()