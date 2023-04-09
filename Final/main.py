import js

p5 = js.window
a = False
b=1
c=0
sound = None
password = [0, 0, 0, 0]
RapunzelState=0
windowState = 0
programState = "Scene1-0"
putChair = 0
tableState = 0
gameState = 0
starState=0

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
Conversation4 = Conversation(0,250,"I got a light?")
Conversation5 = Conversation(0,250,"Finally, we saw the light togehter")
Choice1 = Choice(0,250,"[Girl]: I want to see those lights","Listen","Get out")
Choice2 = Choice(0,250,"[Woman]:You are going to stay in the tower forever!","Listen","Get out")
Choice3 = Choice(0,250,"You heard a doorslam","Get out","")
CR0 = Choice(0,250,"Who are you? Why are you here?","Err.. Flynn Rider, I was lost","")
CR1 = Choice(0,250,"Put Down My Chair!","Sorry~~","")
CR2 = Choice(0,250,"That's my Telescope. I use it to see those Lights","Lights?","")
CR3 = Choice(0,250,"You found the light?! Are you here to take me to see the lights?","I will take you to see the lights","")

Scene1124 = Scene("1124.png",0,0)
Chair = ObjectinScene("Chair.png",0,0)
myHand = Hand("Empty")
Table = Scene("Table.png",0,0)
openTable = Scene("openTable.png",0,0)
telescope = Scene("telescope.png",0,0)
nothingTable = Scene("nothingTable.png",0,0)
star = Scene("star.png",0,0)
nolight = Scene("nolight.png",0,0)
def setup():

    p5.createCanvas(600, 400) 
    global sound
    sound = p5.loadSound('Alan Menken - Waiting for the Lights.mp3')
    print('finish setup') 
  
    
    
def draw():
    global a,programState,b,c,bstring,cstring,windowState,putChair, gameState, RapunzelState, tableState,starState, sound

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
    #if(programState != "Scene1-1" and programState != "Scene1-0"and programState != "Scene1-2" and programState != "Scene2-1"):
        #sound.play()
    elif(programState == "Scene1-4"):
        SceneRoom1.draw()
    elif(programState == "Scene3-0"):
        SceneRoom1.draw()
        if(starState==1):
            star.draw()
        if(starState==2):
            nolight.draw()
            Conversation4.draw()
            myHand.grab("Light")
        if(RapunzelState==1):
            CR1.draw()
        if(RapunzelState==2):
            CR2.draw()
        if(RapunzelState==3):
            CR3.draw()
        if(RapunzelState==4):
            star.draw()
            Conversation5.draw()

            
    elif(programState == "Scene3-1"):
        SceneRoom2.draw()
        if(myHand.x == "Chair" and putChair == 1):
            Chair.draw()
        if(windowState >= 1):
            if(not myHand.x == "Chair"):
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
        if(tableState == 1):
            Table.draw()
            p5.textSize(24)
            p5.text(str(password[0]),308,168)
            p5.text(str(password[1]),342,172)
            p5.text(str(password[2]),376,176)
            p5.text(str(password[3]),410,180)
            if(password[0] == 1 and password[1]==1 and password[2]==2 and password[3]==4):
                tableState=2
        if(tableState==2):
            openTable.draw()
        if(tableState==3):
            telescope.draw()
            if(myHand.x == "Telescope"):
                nothingTable.draw()
        
    elif(programState == "Scene"):
        if(p5.mouseIsPressed == True and p5.mouseY<200 and p5.mouseY>180 and p5.mouseX>250 and p5.mouseX<300):
            programState = "Scene1-4-1"
    elif(programState == "Scene1-4-1"):
        Scene4.draw()
        if(p5.mouseIsPressed == True and p5.mouseY<200 and p5.mouseY>180 and p5.mouseX>300 and p5.mouseX<350):
            programState = "Scene1-4-2"
    elif(programState == "Scene1-4-2"):
        Scene5.draw()
    p5.textSize(12)
   # p5.text('b' + str(b), 10, 30) 
  #  p5.text('c' + str(c), 10, 40)  
    programState = "Scene"+str(b)+"-"+ str(c)
   # p5.text('program_state = ' + programState, 10, 20)  
   # p5.text("p5.mouseX = " + str(p5.mouseX), 10, 60)
   # p5.text("p5.mouseY = " + str(p5.mouseY), 10, 80)
    p5.fill('#F6D3A7'); 
    p5.stroke('#A95E3C'); 
    p5.strokeWeight(2);
    p5.rect(500, 0, 100, 100);
    p5.noStroke(); 
   # p5.text(str(windowState),10,90)
   # p5.text(str(tableState),30,90)
   # p5.text(str(gameState),50,90)
   # p5.text(str(starState),50,110)
   # p5.text(str(RapunzelState),30,110)
   # print(myHand.x)

def keyPressed(event):
    global programState
    pass

def keyReleased(event):
    pass

def mousePressed(event):

    global b,c,windowState,putChair, gameState, RapunzelState, tableState,starState
    if(p5.mouseY>330 and p5.mouseY<370 and b==1):
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
    if(programState == "Scene3-0"):
        if(myHand.x == "Telescope" and p5.mouseX>110 and p5.mouseX<330 and p5.mouseY>80 and p5.mouseY<350):
            starState=1
        if(starState == 1 and p5.mouseX>340 and p5.mouseX<380 and p5.mouseY>207 and p5.mouseY<223):
                starState=2
                
        if(starState == 1 and p5.mouseX>250 and p5.mouseX<350 and p5.mouseY<70):
            starState=0
        if(starState == 2 and p5.mouseX>250 and p5.mouseX<350 and p5.mouseY<70):
            starState=0
        if(myHand.x =="Chair" and p5.mouseX>300 and p5.mouseX<420 and p5.mouseY>142 and p5.mouseY<350):
            RapunzelState=1
        if(myHand.x =="Telescope" and p5.mouseX>380 and p5.mouseX<420 and p5.mouseY>142 and p5.mouseY<350):
            RapunzelState=2
        if(myHand.x =="Light" and p5.mouseX>300 and p5.mouseX<420 and p5.mouseY>142 and p5.mouseY<350):
            RapunzelState=3
        if(RapunzelState==3 and p5.mouseX<200 and p5.mouseY>350 and p5.mouseY<400):
            RapunzelState=4
        if( p5.mouseX>420):
            RapunzelState=0
    if(programState == "Scene1-4" and p5.mouseY>180 and p5.mouseY<220 and p5.mouseX>560 and p5.mouseX<580):
        b=3
        c=1
        
    if(programState == "Scene1-0"):
        sound.play()
            
    if(programState == "Scene3-3"):
        if(p5.mouseX>40 and p5.mouseX<170 and p5.mouseY<388 and p5.mouseY>190):
            myHand.grab("Chair")
        if(p5.mouseX>470 and p5.mouseX<600 and p5.mouseY<350 and p5.mouseY>270):
            tableState=1
        if(p5.mouseY<70 and p5.mouseX>240 and p5.mouseX<360):
            tableState=0
        if(tableState==1):
            if(p5.mouseX>300 and p5.mouseX<320 and p5.mouseY<170 and p5.mouseY>150):
                password[0] = (password[0]+1)%10
            if(p5.mouseX>340 and p5.mouseX<355 and p5.mouseY<174 and p5.mouseY>158):
                password[1] = (password[1]+1)%10
            if(p5.mouseX>375 and p5.mouseX<390 and p5.mouseY<176 and p5.mouseY>161):
                password[2] = (password[2]+1)%10
            if(p5.mouseX>410 and p5.mouseX<430 and p5.mouseY<180 and p5.mouseY>163):
                password[3] = (password[3]+1)%10

        if(tableState==2 and p5.mouseX>290 and p5.mouseX<455 and p5.mouseY<181 and p5.mouseY>139):
            tableState=3
            
        if(tableState==3 and p5.mouseX>400 and p5.mouseX<500 and p5.mouseY<130 and p5.mouseY>90):
            myHand.grab("Telescope")
def mouseReleased(event):
    global a
    a = False
    print(a)
