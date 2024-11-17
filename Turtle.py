import turtle

turtle.Screen().bgcolor("Green")
sc = turtle.Screen()
sc.setup(400 , 300)

turtle.title("Welcome To Turtle")

board = turtle.Turtle()


for i in range(4):
    board.forward(100)
    board.right(90)



turtle.done()
