import turtle

# Screen Initialization
win = turtle.Screen()
win.title("Pong by @BoleoTV")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
movement = 0.1
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = movement
ball.dy = movement

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("courier", 24,"normal"))

# Paddle A movement Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_dn():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Paddle B movement Functions
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_dn():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Allowing Keyboard inputs to call functions
win.listen()
win.onkeypress(paddle_a_up, "w" or "W")
win.onkeypress(paddle_a_dn, "s" or "S")
win.onkeypress(paddle_b_up, "i" or "I")
win.onkeypress(paddle_b_dn, "k" or "K")


# Main game loop
while True:
    win.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    vertBorder = 290
    sideBorder = 390
    if ball.ycor() > vertBorder:
        ball.sety(vertBorder)
        ball.dy *= -1
        

    if ball.ycor() < -vertBorder:
        ball.sety(-vertBorder)
        ball.dy *= -1

    if ball.xcor() > sideBorder:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("courier", 24,"normal"))

    if ball.xcor() < -sideBorder:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("courier", 24,"normal"))


    # Collision Checking
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1