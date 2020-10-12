nombre1= input('Primera persona: ')
edad1=int (input('Edad: '))
nombre2= input('Segunda persona: ')
edad2=int (input('Edad: '))

if edad1 < edad2:
    print (nombre1 + ' Es menor que '+ nombre2)
elif edad1 > edad2:
    print (nombre2 + ' Es mayor que '+ nombre1)
else:
    print (nombre1 +' y '+nombre2 +'tiene la misma edad' )
