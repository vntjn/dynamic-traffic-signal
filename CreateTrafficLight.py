import time

import turtle

#import pathlib
#import os
#from PIL import Image

turtle.TurtleScreen._RUNNING=True

#Extracting CWD to create filepath
#path=pathlib.Path(__file__).parent.absolute()
#path=str(path)
#backgroundPath=os.path.join(path,'DemoBackground','DemoBackground.gif')
#im=Image.open("C:/Users/Sumangal/Desktop/MajorProject/newbg.jpg")
#im.save("C:/Users/Sumangal/Desktop/MajorProject/newbg.gif")

win = turtle.Screen()
#win.bgpic("C:/Users/Sumangal/Desktop/MajorProject/DemoBackground.gif")

class CreateTrafficLight():
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pen = turtle.Turtle()
        self.pen.color("yellow")
        self.pen.width(3)
        self.pen.hideturtle()
        self.pen.speed("fastest")
        self.pen.penup()
        self.pen.goto(x-30,y+60)
        self.pen.pendown()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.penup()
        self.pen.goto(x,y-60)
        self.pen.pendown() 
        self.pen.rt(180)
        self.pen.fd(70)
        self.pen.rt(90)
        self.pen.fd(10)
        self.pen.rt(180)
        self.pen.fd(20)
        
        #Invoking the light objects
        self.redLight = turtle.Turtle()
        self.yellowLight = turtle.Turtle()
        self.greenLight = turtle.Turtle()
        
        #Render Speed
        self.redLight.speed(0)
        self.yellowLight.speed(0)
        self.greenLight.speed(0)

        #To define shape of lights
        self.redLight.shape("circle")
        self.yellowLight.shape("circle")
        self.greenLight.shape("circle")
        
        #initial color for the shape
        self.redLight.color("grey")
        self.yellowLight.color("grey")
        self.greenLight.color("grey")
        
        #pointing the cursor
        self.redLight.penup()
        self.yellowLight.penup()
        self.greenLight.penup()
        
        #invoking the turtle cursor
        self.redLight.goto(x, y+40)
        self.yellowLight.goto(x, y)
        self.greenLight.goto(x, y-40)
        
        
    def changeColor(self,color):
        self.redLight.color("grey")
        self.yellowLight.color("grey")
        self.greenLight.color("grey")  
        
        if color == "red":
            self.redLight.color("red")
            self.color="red"

        elif color == "yellow":
            self.yellowLight.color("yellow")
            self.color="yellow"
            
        elif color == "green":
            self.greenLight.color("green")
            self.color="green"
        
        else:
            print("Unknown Color Provided")
            
    def timer(self,greenTime,waitTime):
        if self.color == "red":
            self.changeColor("green")
            win.ontimer(self.timer, greenTime)
        elif self.color == "yellow":
            self.changeColor("red")
            win.ontimer(self.timer, waitTime)
        elif self.color == "green":
            self.changeColor("yellow")
            win.ontimer(self.timer, 500)
    
    def printDensity(self,density):
        self.strDensity=str(density)
        self.density = turtle.Turtle()
        self.density.hideturtle()
        self.density.penup()
        self.density.speed(0)
        self.density.goto(self.x,self.y+65)
        self.density.write('Density='+self.strDensity,font=("Arial",10,"italic"),align="center")
    
    def clearDensity(self):
        self.density.clear()

    def countdown(self,cTime):
        self.timer = turtle.Turtle()
        self.timer.hideturtle()
        self.timer.penup()
        self.timer.goto(self.x,self.y+80)
        self.timer.color("green")
        for i in range(cTime):
            self.timer.write(cTime-i,font=("LCD",25,"normal"),align="center")
            time.sleep(1)
            self.timer.clear()
            if((i+2)==cTime):
                break
            
    @classmethod
    def printRCException(cls):
        cls.redException = turtle.Turtle()
        cls.redException.hideturtle()
        cls.redException.penup()
        cls.redException.goto(0,300)
        cls.redException.color("red")
        cls.redException.write("RedCountQueue Exception",font=("Arial",13,"bold"),align="center")
        
    @classmethod
    def clearRCException(cls):
        cls.redException.clear()

'''
light1=CreateTrafficLight(-150,150)
light1.printDensity(0.25)
CreateTrafficLight.printRCException()
time.sleep(4)
CreateTrafficLight.clearRCException()
'''
#light2=CreateTrafficLight(150,150)
#light2.printDensity(0.345678394756)
#light1.countdown(20)