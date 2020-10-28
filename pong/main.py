import time
import turtle

import game

SIZE = 20

game = game.Game()
screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False)
screen.title("Pong")
screen.bgcolor("purple")
screen.setup(game.width_screen, game.height_screen)
screen.tracer(0)

ball = turtle.Turtle()
ball.shape("turtle")
ball.color("green")
ball.penup()

# left paddle
paddle_left = turtle.Turtle()
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.penup()
paddle_left.shapesize(game.paddle_height / SIZE, game.paddle_width / SIZE)

# right paddle
paddle_right = turtle.Turtle()
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.penup()
paddle_right.shapesize(game.paddle_height / SIZE, game.paddle_width / SIZE)

# text
text = turtle.Turtle()
text.penup()
text.goto(0, game.height_screen / 2 - 50)
text.write("Player One: 0 | Player Two: 0", align="center", font=("Courier", 20, "bold"))
text.hideturtle()


# keyboard
def left_player_up():
    game.left_paddle_up()


def left_player_down():
    game.left_paddle_down()


def right_player_up():
    game.right_paddle_up()


def right_player_down():
    game.right_paddle_down()


screen.listen()
screen.onkeypress(left_player_up, "w")
screen.onkeypress(left_player_down, "s")
screen.onkeypress(right_player_up, "Up")
screen.onkeypress(right_player_down, "Down")

sleep = 0.001


prev_points_left = None
prev_points_right = None
while True:
    game.tick()
    ball.goto(game.ball_pos())
    if prev_points_left != game.left_player_points or \
            prev_points_right != game.right_player_points:
        text.clear()
        text.write(f"Player One: {game.left_player_points} | Player Two: {game.right_player_points}", align="center",
                   font=("Courier", 20, "bold"))
        prev_points_left = game.left_player_points
        prev_points_right = game.right_player_points
    paddle_left.goto(game.paddle_left_position)
    paddle_right.goto(game.paddle_right_position)
    screen.update()
    time.sleep(sleep)
