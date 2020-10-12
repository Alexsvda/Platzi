moneda= int ( input("En que moneda desea convertir OP1=CL, OP2=COL, OP3=Ven, OP4=arg: "))
value=int (input("Ingrese Valor: "))
valorcl=787.60
valorcol=3638.57
valorven=9.98750 
valorarg=71.47
if moneda ==1:
    conv=value/valorcl
    conv = round (conv,2)
    conv = str (conv)
    print("su valor de coversión es : "+ conv)
elif moneda ==2:
    conv=value/valorcol
    conv = round (conv,2)
    conv = str (conv)
    print("su valor de coversión es : "+ conv)
elif moneda ==3:
    conv=value/valorven
    conv = round (conv,2)
    conv = str (conv)
    print("su valor de coversión es : "+ conv)
elif moneda ==4:
    conv=value/valorarg
    conv = round (conv,2)
    conv = str (conv)
    print("su valor de coversión es : "+ conv)
else:
    print ("valor ingresado no corresponde a uno de la selección")
