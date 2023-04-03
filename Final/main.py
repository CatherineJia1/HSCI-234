import js
p5 = js.window
a = False
b=1
c=0
windowState = 0
programState = "Scene1-0"
putChair = 0
class Scene:  
    def __init__(self,img,x,y):
        self.img = p5.loadImage(img)
        self.x = 0
        self.y = 0
        
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img,0, 0, self.img.width, self.img.height)
        p5.pop()
class Hand:
    def __init__(self,x):
        self.x = x

    def grab(self,object):
        self.x = object
class ObjectinScene(Scene):
    pass
    
class Conversation:
    def __init__(self,x,y,text):
        self.x = 0
        self.y = 330
        self.text = text
        
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.fill(0)
        p5.rect(0,0,600,70,0)
        p5.fill(255)
        p5.text(self.text, 20, 20)
        p5.pop()

class Choice:
    def __init__(self,x,y,text,choice1,choice2):
        self.x = 0
        self.y = 330
        self.text = text
        self.choice1 = choice1
        self.choice2 = choice2
        
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.fill(0)
        p5.rect(0,0,600,70,0)
        p5.fill(255)
        p5.text(self.text, 20, 20)
        p5.text(self.choice1,20,40)
        p5.text(self.choice2,20,60)
        p5.pop()
       
Scene1 = Scene("guizi.png",0,0)
SceneFound = Scene("chuzi.jpg",0,0) 
Scene2 = Scene("lose.png",0,0)
Scene3 = Scene("guanguizi.png",0,0)
Scene4 = Scene("bankailianzi.png",0,0)
Scene5 = Scene("kailianzi.png",0,0)
SceneRoom1 = Scene("Room1.png",0,0)
SceneRoom2 = Scene("Room2.png",0,0)
SceneRoom3 = Scene("Room3.png",0,0)
SceneRoom4 = Scene("Room4.png",0,0)
SceneRoom4noChair = Scene("Room4-noChair.png",0,0)

Conversation1 = Conversation(0,250,"You weak up and you found yourself in a closet, and you heard some people are talking")
Conversation2 = Conversation(0,250,"It is too high... I cannot reach it")
Conversation3 = Conversation(0,250,"Nov.24th emmm is that her birthday? What are those LIGHTS...?")
Choice1 = Choice(0,250,"[Girl]: I want to see those lights","Listen","Get out")
Choice2 = Choice(0,250,"[Woman]:You are going to stay in the tower forever!","Listen","Get out")
Choice3 = Choice(0,250,"You heard a doorslam","Get out","")

Scene1124 = Scene("1124.png",0,0)
Chair = ObjectinScene("Chair.png",0,0)
myHand = Hand("Empty")

def setup():
    
    p5.createCanvas(600, 400) 
    print('finished setup') 
    
def draw():
    global a,programState,b,c,bstring,cstring,windowState,putChair

    p5.background(255)  
    if(programState =="Scene1-0"):
         Scene1.draw()
         Conversation1.draw()  
    if(programState=="Scene1-1"):
        Scene1.draw()
        Choice1.draw()
        #if(p5.mouseIsPressed == True and p5.mouseY>370 and p5.mouseY<400):
            #programState = "Scene2-1"
        #if(p5.mouseIsPressed == True  and p5.mouseY>330 and p5.mouseY<370):
            #programState = "Scene1-2"        
    elif(programState == "Scene2-1" ):
        Scene2.draw()
    elif(programState == "Scene1-2"):
        Scene1.draw()
        Choice2.draw()
        #if(p5.mouseIsPressed == True and p5.mouseY>370 and p5.mouseY<400):
          #  programState = "Scene2"
        #if(p5.mouseIsPressed == True and p5.mouseY>330 and p5.mouseY<370):
          #  programState = "Scene1-3"
    elif(programState == "Scene1-3"):
        Scene1.draw()
        Choice3.draw()
        #if(p5.mouseIsPressed == True and p5.mouseY>370 and p5.mouseY<400):
          #  programState = "Scene3"
        #if(p5.mouseIsPressed == True and p5.mouseY>330 and p5.mouseY<370):
            #programState = "Scene2-2"
    elif(programState == "Scene2-2"):
        Scene2.draw() 
        
    elif(programState == "Scene1-4"):
        SceneRoom1.draw()
    elif(programState == "Scene3-0"):
        SceneRoom1.draw()
    elif(programState == "Scene3-1"):
        SceneRoom2.draw()
        if(myHand.x == "Chair" and putChair == 1):
            Chair.draw()
        if(windowState >= 1):
            if(myHand.x == "Empty"):
                Conversation2.draw()
            if(myHand.x == "Chair" and windowState == 2):
                Scene4.draw()
                Chair.draw()
            if(myHand.x == "Chair" and windowState == 3):
                Scene5.draw()
                Chair.draw()
            if(myHand.x == "Chair" and windowState == 4):
                Scene1124.draw()
                Chair.draw()
                Conversation3.draw()
                
    elif(programState == "Scene3-2"):
        SceneRoom3.draw()
    elif(programState == "Scene3-3"):
        SceneRoom4.draw()
        if(myHand.x == "Chair"):
            SceneRoom4noChair.draw()
    
    elif(programState == "Scene"):
        if(p5.mouseIsPressed == True and p5.mouseY<200 and p5.mouseY>180 and p5.mouseX>250 and p5.mouseX<300):
            programState = "Scene1-4-1"
    elif(programState == "Scene1-4-1"):
        Scene4.draw()
        if(p5.mouseIsPressed == True and p5.mouseY<200 and p5.mouseY>180 and p5.mouseX>300 and p5.mouseX<350):
            programState = "Scene1-4-2"
    elif(programState == "Scene1-4-2"):
        Scene5.draw()
    p5.text('b' + str(b), 10, 30) 
    p5.text('c' + str(c), 10, 40)  
    programState = "Scene"+str(b)+"-"+ str(c)
    p5.text('program_state = ' + programState, 10, 20)  
    p5.text("p5.mouseX = " + str(p5.mouseX), 10, 60)
    p5.text("p5.mouseY = " + str(p5.mouseY), 10, 80)
    p5.text('You have '+ myHand.x + " in your hand", 400, 10)
    p5.text(str(windowState),10,90)
    print(myHand.x)

def keyPressed(event):
    global programState
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    global b,c,windowState,putChair
    if(p5.mouseY>330 and p5.mouseY<370):
        c=c+1
    if(p5.mouseY>370 and p5.mouseY<400):
        b=2
    if(b == 1 ):
        if (p5.mouseY>180 and p5.mouseY<220 and p5.mouseX>20 and p5.mouseX<40):
            b=3
            c=0
    if(b == 3):
        if (p5.mouseY>180 and p5.mouseY<220 and p5.mouseX>20 and p5.mouseX<40):
            c=(c-1)%4
        if (p5.mouseY>180 and p5.mouseY<220 and p5.mouseX>560 and p5.mouseX<580):
            c=(c+1)%4
    if(programState == "Scene3-1"):
        if(p5.mouseX>263 and p5.mouseX<330 and p5.mouseY<190 and p5.mouseY>100):
            windowState = windowState + 1
        else:
            windowState = 0
        if(myHand.x == "Chair" and p5.mouseX>263 and p5.mouseX<330 and p5.mouseY<350 and p5.mouseY>240):
            putChair = putChair + 1

    if(programState == "Scene3-3"):
        if(p5.mouseX>40 and p5.mouseX<170 and p5.mouseY<388 and p5.mouseY>190):
            myHand.grab("Chair")
    

def mouseReleased(event):
    global a
    a = False
    print(a)
