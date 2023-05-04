#program created by Nick AKA Mr PA
#snake game for stimulating programmer mind
#import from python library
import turtle
import time
import random

#time
delay = 0

#scores check on your screen
score = 0
high_score = 0

#how to set up your screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("yellow")
s.setup(width = 600, height = 600)
s.tracer(0)

#how to set snake head
h = turtle.Turtle()
h.shape("square")
h.speed(0)
h.color("black")
h.penup()
h.goto(0,0)
h.direction = "stop"

#how to set snake food
f = turtle.Turtle()
f.shape("circle")
f.speed(0)
f.color("red")
f.penup()
f.showturtle()
f.goto(-100,100)

segments = []

#how to set scoreboard title
sb = turtle.Turtle()
sb.color("black")
sb.hideturtle()
sb.goto(0,250)
sb.write("Score: 0 High Score: 0", align = "center", font = ("ds-digital",24,"normal"))

#functions
def go_up():
    if h.direction != "down":
        h.direction = "up"
def go_down():
    if h.direction != "up":
        h.direction = "down"
def go_right():
    if h.direction != "left":
        h.direction = "right"
def go_left():
    if h.direction != "right":
        h.direction = "left"       
def movestop():
    h.direction = "stop"    
def move():
    if h.direction == "up":
        y = h.ycor()
        h.sety(y+20)
    if h.direction == "down":
        y = h.ycor()
        h.sety(y-20)
    if h.direction == "right":
        x = h.xcor()
        h.setx(x+20)
    if h.direction == "left":
        x = h.xcor()
        h.setx(x-20)

#how to set control rules to be used
#in the keyboard seen on screen
s.listen()
s.onkeypress(go_up, 'q')
s.onkeypress(go_down, 'p')                                                  
s.onkeypress(go_right, 'l')
s.onkeypress(go_left, 'a')
s.onkeypress(movestop, 'z')

#main loop
while True:
    s.update()
    
    #check collision with border area
    if h.xcor()>290:
        h.setx(-290)
    if h.xcor()<-290:
        h.setx(290)
    if h.ycor()>290:
        h.sety(-290)
    if h.ycor()<-290:
        h.sety(290)
        
        time.sleep(1)
        h.goto(0,0) 
        h.direction = "stop"
        
        #how to hide segment of the body
        for segment in segments:
            segment.goto(1000,100)
            #clear the segments
        segments.clear() 
        
        #reset score
        score = 0
        #reset delay
        delay = 0.1
        
        sb.clear()
        sb.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("ds-digital",24,"normal"))
          
                   
       #check collision with food
    if h.distance(f)<20:
        #how move the food at random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        f.goto(x,y)
        
        #how to add segment after eating one apple
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("green")
        new_segment.shape("circle")
        new_segment.penup()
        segments.append(new_segment)
        
        #shorten the delay after eating apple
        delay -= 0.001
        #inrease the score after taking one apple
        score += 10
        
    #how to update score with highest score
    if score > high_score:
        high_score = score
    #update on screen board
    sb.clear()
    sb.write("Score: {} High Score: {}".format(score , high_score) ,align = "center", font = ("ds-digital",24,"normal"))        
    
    #how to move the segment in a reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head when eating
    if len(segments)>0:
        x = h.xcor()
        y = h.ycor()
        segments[0].goto(x,y)
    move() 
    
    #check collision with the body
    for segment in segments:
        if segment.distance(h)<20:
            time.sleep(1)
            h.goto(0,0)
            h.direction = "stop"
            
            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
            
            #update the score
            sb.clear()
            sb.write("Score: {} High Score: {}", align = "center", font = ("ds-digital",24,"normal"))        
    time.sleep(delay)
s.mainloop()           
            
