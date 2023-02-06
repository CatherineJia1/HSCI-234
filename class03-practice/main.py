import js
p5 = js.window
random_size = p5.random(50)


def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
def my_function():
    p5.push()
    p5.translate(50,250)
    p5.fill(255,255,0)
    p5.rect(0,0,50,50)
    p5.pop()

def draw_orange_square(x,y):
    p5.push()
    p5.translate(50,250)
    p5.fill(255,128,0)
    p5.rect(0,0,x,y)
    p5.pop()
    
def draw():
    p5.background(0, 0, 153)    
    s = 50
    s=p5.random(50)
    p5.rect(50,200,s,s)
    p5.rect(100,200,random_size,random_size)
    my_function()
    draw_orange_square(10,20)



    p5.push()
    p5.translate(50,150)
    #p5.rotate(p5.PI/3)
    p5.rotate(p5.radians(-45))
    p5.rect(0,0,50,50)
    p5.pop()

    
    p5.push()
    p5.translate(20,20)
    p5.rect(0,0,100,100)
    p5.pop()


    p5.push()
    p5.scale(2.0)
    p5.rect(0,0,50,50)
    p5.pop()

    p5.push()
    p5.translate(p5.mouseX, p5.mouseY)
    p5.rect(0,0,50,50)
    p5.pop()
