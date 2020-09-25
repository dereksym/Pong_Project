# Turtle tutorial - Pong game in Python 3
# Hardcoding - No OOP
import turtle
import os
import winsound

wn = turtle.Screen()
wn.title("Pong Turtle Tutorial")
wn.bgcolor("black")
wn.setup(width=800, height =600)
wn.tracer(0,0) #stop window from updating to speed up the game


# Score
score_a = 0
score_b = 0

# Paddle Lefts
paddle_l = turtle.Turtle()
paddle_l.speed(0) #speed of animation to max
paddle_l.shape("square")
paddle_l.color("light grey")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350,0)


# Paddle Right
paddle_r = turtle.Turtle()
paddle_r.speed(0) #speed of animation to max
paddle_r.shape("square")
paddle_r.color("light grey")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation to max
ball.shape("circle")
ball.color("light grey")
ball.penup()
ball.goto(0,0)

# Move ball (delta = 2 pixels)
ball.dx = 0.34
ball.dy = 0.34

# Pen = module.method
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:{}      Player B:{}".format(score_a,score_b), align="center", font =("Courier", 18, "normal"))



# Function (Move paddle up/down)
def paddle_l_up():
    y = paddle_l.ycor()
    y += 30
    paddle_l.sety(y)

def paddle_l_dn():
    y = paddle_l.ycor()
    y -= 30
    paddle_l.sety(y)

def paddle_r_up():
    y = paddle_r.ycor()
    y += 30
    paddle_r.sety(y)

def paddle_r_dn():
    y = paddle_r.ycor()
    y -= 30
    paddle_r.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_l_up, 'w')
wn.onkeypress(paddle_l_dn, 's')
wn.onkeypress(paddle_r_up, 'Up')
wn.onkeypress(paddle_r_dn, 'Down')



# Main game loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor()+ ball.dx) #from (0,0) to (2,0),(4,0)...
    ball.sety(ball.ycor()+ ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse the direction of ball
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Play A:{}      Player B:{}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Play A:{}      Player B:{}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    # Ball bounces off the bar
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_r.ycor() + 50 and ball.ycor() > paddle_r.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_l.ycor() + 50 and ball.ycor() > paddle_l.ycor() -50):
        ball.dx *= -1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    if score_a == 3:
        break
    elif score_b == 3:
        break