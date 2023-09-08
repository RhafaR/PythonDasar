import turtle
def drawSquare ( ttl , x , y , length ):
    ttl.penup () # raise the pen
    ttl.goto (x , y) # move to starting position
    ttl.setheading (0) # point turtle east
    ttl.pendown () 
    for count in range (4) :
        ttl.forward ( length )
        ttl.right (90)
    ttl.penup ()

Bob = turtle . Turtle ()
Bob.speed (10)
Bob.pensize (3)
drawSquare ( Bob , 0 , 0, 100 )

turtle . done ()