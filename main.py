import turtle
import os
import math
import random
from playsound import playsound
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('laser27.wav')
sound.set_volume(0.5)

# Podesavanje ekrana
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Shape Wars')
wn.bgpic('bg.gif')
wn.setup(600, 600)

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

# Score 0
score = 0

# Napisi score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('yellow')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = 'Score: %s' %score
score_pen.write(scorestring, False, align = 'left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

# Pravimo igraca kornjacu
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -290)
player.setheading(90)

player_speed = 15

number_of_enemies = 5

enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:

    # Pravimo neprijatelja
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

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
        sound.play()
        weapon_state = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        weapon.setposition(x, y)
        weapon.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Pravimo keyboard bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire, 'space')

# Main game loop
while True:

    for enemy in enemies:
        # Pokretanje neprijatelja
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Pokretanje neprijatelja gore i dole
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1

        if enemy.xcor() < -275:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1
        
        if isCollision(weapon, enemy):
            weapon.hideturtle()
            weapon_state = 'ready'
            weapon.setposition(0, -400)
            enemy.setposition(-200, 250)
            # Score update
            score += 10
            scorestring = 'Score: %s' %score
            score_pen.clear()

            score_pen.write(scorestring, False, align = 'left', font=('Arial', 14, 'normal'))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            over_pen = turtle.Turtle()
            over_pen.speed(0)
            over_pen.color('yellow')
            over_pen.penup()
            over_pen.setposition(-200, 320)
            overstring = 'GAMEOVER - Restart the Game! Score: %s' %score
            over_pen.write(overstring, False, align = 'center', font=('Arial', 20, 'normal'))
            over_pen.hideturtle()

            print('GAME OVER!')
            break

    # Pokretanje metaka
    if weapon_state == 'fire':
        y = weapon.ycor()
        y += weapon_speed
        weapon.sety(y)

    if weapon.ycor() > 275:
        weapon.hideturtle()
        weapon_state = 'ready'

delay = input('Exit')

