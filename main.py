import turtle #importing library

turtle.Screen().bgcolor("Aqua")
board= turtle.Turtle()

# first triangle for star
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)

#second star
board.pendown()
board.right(90)
board.forward(100)


board.right(120)
board.forward(100)

board.right(120)
board.forward(100)
turtle.done()
