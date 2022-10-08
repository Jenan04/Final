
import turtle
wn=turtle.Screen()
wn.title("Ping Pong Game ")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.bgcolor(.1 ,.1 ,.1)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_len=1 ,stretch_wid=1)
ball.goto(x=0,y=0 )
ball.penup()
ball_dx,ball_dy =1 ,1
ball_speed= 1


center_line =turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.goto(0,0)
center_line.shapesize(stretch_len=1 ,stretch_wid=25)
center_line.penup()
center_line.color("white")




player1=turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("blue")
player1.shapesize(stretch_len=1 ,stretch_wid=5)
player1.goto(x=-350,y=0 )
player1.penup()

player2=turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_len=1 ,stretch_wid=5)
player2.goto(x=350,y=0 )
player2.penup()

score=turtle.Turtle()
score.speed(0)
score.write("player1:0 player2 :0", align="center",font=("Courier",14 ,"normal"))
score.color("white")
score.shapesize(stretch_len=1 ,stretch_wid=5)
score.goto(x=0,y=260 )
score.penup()
score.hideturtle()
p1_score , p2_score = 0,0


players_speed=20
def p1_move_up():
    player1.sety(player1.ycor()+players_speed)

def p1_move_down():
    player1.sety(player1.ycor()-players_speed)

def p2_move_up():
    player2.sety(player2.ycor()+players_speed)

def p2_move_down():
    player2.sety(player2.ycor()-players_speed)

wn.listen()
wn.onkeypress(p1_move_up ,"w")
wn.onkeypress(p1_move_down ,"d")
wn.onkeypress(p2_move_up ,"s")
wn.onkeypress(p2_move_down,"r")



while True:
    wn.update()

    ball.setx(ball.xcor() +(ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))
    if (ball.ycor()>290):
        ball.sety(290)
        ball_dy *= -1

    if (ball.ycor()<-290):
        ball.sety(-290)
        ball_dy *= -1

    if ball.xcor() < -340 and ball.xcor() > -350and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1
    if ball.xcor() > 340 and ball.xcor() < 350and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(340)
        ball_dx *= -1

    if (ball.xcor() > 390):
        ball.goto(0, 0)
        ball_dx *= -1
        score.clear()
        p1_score += 1
        score.write(f"player1:{p1_score} player2 :{p2_score}", align="center", font=("Courier", 14, "normal"))

    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1
        score.clear()
        p2_score += 1
        score.write(f"player1:{p1_score} player2 :{p2_score}", align="center", font=("Courier", 14, "normal"))
