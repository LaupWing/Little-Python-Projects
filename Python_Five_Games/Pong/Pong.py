import turtle

wn = turtle.Screen()
wn.title("Pong youtube tutorial")
wn.bgcolor('green')
wn.setup(width=800, height=600)
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(0,0)

while True:
    wn.update()