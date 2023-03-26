import js
p5 = js.window
a = False
b=1
c=0
programState = "Scene1-0"

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
Conversation1 = Conversation(0,250,"You weak up and you found yourself in a closet, and you heard some people are talking")
Choice1 = Choice(0,250,"[Girl]: I want to see those lights","Listen","Get out")
Choice2 = Choice(0,250,"[Woman]:You are going to stay in the tower forever!","Listen","Get out")
Choice3 = Choice(0,250,"You heard a doorslam","Get out","")
SceneFound = Scene("chuzi.jpg",0,0) 
Scene2 = Scene("lose.png",0,0)
Scene3 = Scene("guanguizi.png",0,0)
Scene4 = Scene("bankailianzi.jpg",0,0)
Scene5 = Scene("kailianzi.jpg",0,0)
def setup():
    
    p5.createCanvas(600, 400) 
    print('finished setup') 
    
def draw():
    global a,programState,b,c,bstring,cstring

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
        Scene3.draw()
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
    
def keyPressed(event):
    global programState
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    global b,c
    if(p5.mouseY>330 and p5.mouseY<370):
        c=c+1
    if(p5.mouseY>370 and p5.mouseY<400):
        b=2

    

def mouseReleased(event):
    global a
    a = False
    print(a)
