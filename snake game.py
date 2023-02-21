import turtle, random, time
stage= turtle.Screen()
stage.setup(height=600,width=600)
stage.tracer(0)
stage.bgcolor("yellow")
stage.title("snake")

#head snake
head= turtle.Turtle()
head.shape("triangle")
head.shapesize(1,1)
head. color("blue")
head.speed(0)
head.penup()
head.goto(0,0)
direction= 'stop'

#food
food= turtle.Turtle()
randomX= random.randint(-150,150)
randomY= random.randint(-150,150)
food.shape("circle")
food.color("red")
food.speed(0)
food.penup()
food.goto(randomX,randomY)
tails=[]

#score sprite
s= 0
s2= 1
score= turtle.Turtle()
score.penup()
score.goto(-200,256)
score.hideturtle()
score.write('SCORE: ' + str(s), align='center', font=('arial', 24, 'bold'))
score.speed(0)



#up, down, left, right definisi
def move():
    if direction=="up":
        head.setheading(90)
        head.sety(head.ycor()+20)
    if direction == "down":
        head.setheading(-90)
        head.sety(head.ycor() - 20)
    if direction=="right"  :
        head.setheading(0)
        head.setx(head.xcor()+20)
    if direction=="left":
        head.setheading(180)
        head.setx(head.xcor()-20)



#control up down left right
def moveUp():
    global direction
    if direction!="down":
        direction= "up"
def moveDown():
    global direction
    if direction!="up":
        direction="down"
def moveRight():
    global direction
    if direction!="left":
        direction="right"
def moveLeft():
    global direction
    if direction!="right":
        direction="left"

stage.listen()
stage.onkeypress(moveUp,"Up")
stage.onkeypress(moveDown,"Down")
stage.onkeypress(moveRight,"Right")
stage.onkeypress(moveLeft,"Left")
while True:
    if head.distance(food) < 20:
        #food random location
        randomX = random.randint(-150, 150)
        randomY = random.randint(-150, 150)
        food.goto(randomX, randomY)

        #scoring sytem
        s= s+ s2
        score.clear()
        score.write('SCORE: ' + str(s), align='center', font=('arial', 24, 'bold'))

        #new tail for snake
        newTail= turtle.Turtle()
        newTail.shape("circle")
        newTail.color("green")
        newTail.speed(0)
        newTail.penup()
        newTail.goto(0,0)
        tails.append(newTail)
    for a in range(len(tails)-1, 0 ,-1):
      tails[a].goto(tails[a - 1].xcor(), tails[a - 1].ycor())
    if len(tails)>0:
        tails[0].goto(head.xcor(), head.ycor())

    move()
    #ini jika tabrak tembok
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290:
        direction="stop"
        head.goto(0,0)
        for a in(tails):
            a.goto(1000,1000)
        tails.clear()
    #tabrak ekor
    for a in tails:
        if a.distance(head) < 20:
            direction= "stop"
            head.goto(0,0)
            for a in tails:
                a.goto(1000,1000)
            tails.clear()
            break
    time.sleep(0.2)
    stage.update()













