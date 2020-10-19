import turtle 

myturtle = turtle.Turtle()
mywin = turtle.Screen()

def draw (myturtle, length):
    """
    dibujo en base a recursividad 
    """
    if length > 0:
        myturtle.forward (length)
        myturtle.left(90)
        draw(myturtle, length -10)

draw (myturtle, 100)
mywin.exitonclick()
