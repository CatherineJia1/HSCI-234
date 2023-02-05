
import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():

    p5.background(0, 0, 153)           # white background 
    p5.fill(255, 255, 153);
    p5.noStroke()
    p5.ellipse(60, 60, 60, 60);    #moon in sky
    for j in range(1,5):           #stars in sky
        for i in range(1,10):
             p5.ellipse(100+i*j*20, 60+j*5, 1, 1);
    p5.fill(255, 240, 240);
    for i in range(1,3):           #ears
        p5.triangle(80 + i * 10, 200, 160 + i * 75, 150, 200 + i * 5, 200);
    p5.fill(255, 240, 240);
    for i in range (0,2):       #body
        p5.ellipse(150+i*40, 220+i*40, 135+i*20, 80+i*20);
    x = 5
    y = 5
    p5.fill(0, 0, 0);             #eye
    p5.ellipse(140, 200, 20, 20);     
    p5.fill(255, 255, 255);
    p5.ellipse(140-x, 200-y, 10, 10);
