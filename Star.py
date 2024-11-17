import turtle

turtle.Screen().bgcolor("Beige")
sc = turtle.Screen()
sc.setup(400 , 300)

turtle.title("Welcome To Turtle")

board = turtle.Turtle()

board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()
