import turtle
import os
import time

# Podesavanje ekrana
wn = turtle.Screen()
wn.bgcolor('Black')
wn.title('Space Invaders')

# Podesavanje bordera
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Pravimo igraca kornjacu
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

# Pravimo neprijatelja
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemy_speed = 2

# Pravimo nase oruzje
weapon = turtle.Turtle()
weapon.color('yellow')
weapon.shape('triangle')
weapon.penup()
weapon.speed(0)
weapon.setheading(90)
weapon.shapesize(0.5, 0.5)
weapon.hideturtle()

weapon_speed = 20

# Weapon state
# ready
# fire
weapon_state = 'ready'

# Pokretanje igraca lijevo i desno
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire():
    global weapon_state
    if weapon_state == 'ready':
        weapon_state = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        weapon.setposition(x, y)
        weapon.showturtle()

# Pravimo keyboard bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire, 'space')

# Main game loop
while True:

    # Pokretanje neprijatelja
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # Pokretanje neprijatelja gore i dole
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    # Pokretanje metaka
    if weapon_state == 'fire':
        y = weapon.ycor()
        y += weapon_speed
        weapon.sety(y)

    if weapon.ycor() > 275:
        weapon.hideturtle()
        weapon_state = 'ready'

delay = input('Exit')

