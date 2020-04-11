import turtle

wn = turtle.Screen()
wn.title("Pong youtube tutorial")
wn.bgcolor('green')
wn.setup(width=800, height=600)
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)

while True:
    wn.update()