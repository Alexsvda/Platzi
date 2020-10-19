"""
Menu desplegable 
@autor Alexis Saavedra
"""
import tkinter as tk
ventana=tk.Tk()
ventana.title("Lista desplegable")
ventana.geometry('380x300+1200+100')#Doble Pantalla 
ventana.configure(background='dark turquoise')
var=tk.StringVar(ventana)
var.set ('Rojo')
opciones=['Azul','Rosa', 'Amarillo', 'Verde', 'Blanco','Morado']
opcion=tk.OptionMenu(ventana,var,*opciones)
opcion.config(width=20)
opcion.pack(side='left', padx=30, pady=30)
el=tk.Label(ventana,text="Color Seleccionado: ", bg= "black", fg="white")
#el.pack(-padx=5 , pady=5 , ipax=5 , ipady=5 , fill = tk.X)
color=tk.Label(ventana,bg="plum", textvariable=var, padx=5,pady=5,width=50)
color.pack()
ventana.mainloop()




