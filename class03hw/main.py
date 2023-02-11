import js
p5 = js.window
random_x = p5.random(300)
random_y = p5.random(300)
random_a = p5.random(50,120)

random_x1 = p5.random(300)
random_y1 = p5.random(300)
random_a1 = p5.random(120,200)

random_x2 = p5.random(300)
random_y2 = p5.random(300)
random_a2 = p5.random(200,300)

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw_face():   # draw face 
    p5.fill(255,255,255)
    p5.arc(70, 30, 150, 180, p5.radians(0), p5.radians(180))
    p5.arc(70, 40, 150, 180, p5.radians(180), p5.radians(0))

def draw_eyes_left():   # draw eyes

    p5.fill(255,255,255,0)


    p5.arc(0,40, 100, 100, p5.radians(-95), p5.radians(-85))
    p5.arc(0,9.5, 50, 40, p5.radians(-165), p5.radians(-105))
    p5.arc(-6,4, 35, 40, p5.radians(145), p5.radians(180))
    p5.arc(-9,7.5, 50, 40, p5.radians(-50), p5.radians(-30))
    p5.arc(0,-30, 100, 100, p5.radians(85), p5.radians(115))

    p5.stroke(0)


    p5.fill(1,1,1)
    p5.arc(-5,14, 12, 40, p5.radians(150), p5.radians(30))
    p5.arc(-5,14, 12, 12, p5.radians(10), p5.radians(170))

    p5.fill(255,255,255)
    p5.ellipse(-7+p5.mouseX/50,0+p5.mouseY/30,4,8)




def draw_eyes_right():   # draw eyes
    
    p5.fill(255,255,255,0)
    p5.arc(65,40, 100, 100, p5.radians(-95), p5.radians(-85))
    p5.arc(60,9, 50, 40, p5.radians(-65), p5.radians(-15))
    p5.arc(67,4, 35, 40, p5.radians(0), p5.radians(35))
    p5.arc(73.5,7.5, 50, 40, p5.radians(-150), p5.radians(-130))
    p5.arc(65,-31, 100, 100, p5.radians(70), p5.radians(105))
    p5.stroke(0)
    
    p5.fill(1,1,1)
    p5.arc(68,14, 14, 40, p5.radians(150), p5.radians(30))
    p5.arc(68,14, 12, 12, p5.radians(10), p5.radians(170))

    p5.fill(255,255,255) # draw highlight in eyes that moves
    p5.ellipse(68+p5.mouseX/50,0+p5.mouseY/30,4,8)


def draw_eyebrow(x,y,r): # draw eyebrow
    p5.fill(255,255,255,0)
    p5.arc(x,y, 100, 100, p5.radians(-r-90), p5.radians(-90+r))
    
def draw_mouth(x,y,r,t): # draw eyebrow
    p5.fill(255,0,0,30)
    p5.ellipse(x,y,r,t)
    

def draw():
    p5.background(212,168,233) 

    p5.ellipse(random_x,random_y,random_a,random_a)
    p5.ellipse(random_x1,random_y1,random_a1,random_a1)
    p5.ellipse(random_x2,random_y2,random_a2,random_a2)  #generate 3 circles as random geometric background
        
    for i in range(150):

        s=p5.random(100)
        p5.line(75+i,100,75+i,150+s)

    p5.push()  # save coordinates  
    p5.translate(80, 100) 
          # white background
    draw_face() 
    p5.pop()

    p5.push()
    p5.translate(120, 130)
    draw_eyes_left()
    draw_eyes_right()
    draw_eyebrow(-5,30,20)
    draw_eyebrow(68,30,20)
    p5.pop()

    draw_mouth(150,190,p5.mouseX/10,p5.mouseY/10)
    
    for i in range(20): # draw hairs that moves randomly, it creates an organic feeling. 
        s = 70
        s=p5.random(100)
        p5.line(75+i,80,75+i,150+s)
        
    for i in range(20):
        s = 70
        s=p5.random(100)
        p5.line(205+i,80,205+i,150+s)

    for i in range(150):
        s = 70
        s=p5.random(20)
        p5.line(75+i,50,75+i,90+s)
