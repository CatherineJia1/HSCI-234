import js
p5 = js.window
angle = 0.0
x=150
y=150
angle2=0.0
angle3=0.0
i=0

#try to press a,d,left arrodddãdw and right arrow. 
#try to press mouse
#try to hover on the canvas




def setup():     
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw_head():    #Head of bb8
    p5.fill(255)
    p5.noStroke()
    p5.arc(0,0, 100, 100, p5.radians(180), p5.radians(0))
    p5.fill(200)
    p5.arc(0,0, 100, 100, p5.radians(-140), p5.radians(-40))   
    p5.fill(255)
    p5.quad(-50, -1, 50, -1, 40, 10, -40, 10)
    p5.quad(-37, -32, 37, -32, 40, -20, -40, -20)
    if(p5.mouseX<300 and p5.mouseY<300):
        p5.fill(11)          #change bb8to bb9e
    else:
        p5.fill(233,143,60) #change bb9eto bb8
    p5.quad(-44, -25, 44, -25, 47, -20, -47, -20)
    p5.fill(200)  
    p5.ellipse(0,-10,20,20)
    p5.fill(0)  
    p5.ellipse(0,-10,15,15)
    p5.fill(255,0,0)  
    p5.ellipse(-1+p5.mouseX/100,p5.mouseY/100-11,5,5)
    p5.fill(0)  
    p5.ellipse(20,0,10,10)


def draw_body():   #body of bb8
    angle = 0.0
    p5.fill(255)
    p5.noStroke()
    p5.ellipse(0, 85, 170,170)


def draw_Pattern():    #pattern on the body of bb8
    p5.noStroke()
    if(p5.mouseX<300 and p5.mouseY<300):
        p5.fill(11)
    else:
        p5.fill(233,143,60)
    p5.ellipse(-3, 1, 80,80)
    p5.fill(255)
    p5.ellipse(-3, 1, 60,60)   
    p5.fill(200)  
    p5.ellipse(-3, 1, 40,40)

    if(p5.mouseX<300 and p5.mouseY<300):    #change bb8 to bb9e
        p5.fill(11)
    else:
        p5.fill(233,143,60)
    p5.rect(-32, 1, 10, 10)
    p5.rect(-3, -30, 10, 10)
    p5.rect(-3, 30, 10, 10)
    p5.rect(28, 1, 10, 10)







def draw():
    if(p5.mouseX<300 and p5.mouseY<300): #change background color
        p5.background(255,0,0)    
    else:
        p5.background(0,0,255)
    #p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)
    global angle, angle2,x,y,angle3,i 
    
    if (p5.mouseIsPressed == True and p5.mouseX<300 and p5.mouseY<300):   #text of the name of robot
        p5.fill(11);
        p5.textSize(50)
        p5.text("BB-9E", 80,110)

    if (p5.mouseIsPressed == True and p5.mouseX>300 or p5.mouseY>300):  #text of the name of robot
        p5.fill(233,143,60);
        p5.textSize(50)
        p5.text("BB-8", 100,110)

    p5.push()  

    
    p5.translate(150+i,150)   #change position of robot
    if (p5.keyIsPressed == True):
        if (p5.key == 'd'):
            i=i+1
            x=x+1
            angle3=angle3+0.005
        if (p5.key == 'a'):
            i=i-1
            x=x-1
            angle3=angle3-0.005



    draw_body()   #change position of robot
    p5.pop()
    p5.push()
    p5.translate(134+i,214) 
    p5.rotate(angle)
    draw_Pattern()
    angle = angle+0.05
    p5.pop()





    p5.push()         #rotate robot head
    if (p5.keyIsPressed == True and angle2>=-0.5 and angle2<=0.5): # key has been pressed + set boundary
        # p5.keyCode is equal to special keys like arrows:
        if (p5.keyCode == p5.LEFT_ARROW):  # left arrow
            angle2 = angle2-0.006
            x=x-0.5
            if(angle2>0):
                y=y-0.1
            else:
                y=y+0.1
        elif (p5.keyCode == p5.RIGHT_ARROW):  # right arrow
            angle2 = angle2 +0.006
            x=x+0.5
            if(angle2>0):
                y=y+0.1
            else:
                y=y-0.1
    elif (p5.keyIsPressed == True and angle2<-0.5):  #set boundary of rotation
        angle2 = angle2 +0.006
        x=x+0.5
        if(angle2>0):
            y=y+0.1
        else:
            y=y-0.1
           
    elif (p5.keyIsPressed == True and angle2>0.5): #set boundary of rotation
        angle2 = angle2-0.006
        x=x-0.5
        if(angle2>0):
            y=y-0.1
        else:
            y=y+0.1


    p5.translate(x,y)
    p5.rotate(angle2)
    draw_head()
    p5.pop()
