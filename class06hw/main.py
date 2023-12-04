import js

class Bullet:  
  def __init__(self, x = 150, y = 250, speed = 2):
    self.x = x  
    self.y = y
    self.speed = speed

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.fill(255, 0, 127)
    p5.rect(0, 0, 40, 80)
    p5.pop()

   def update(self):
       distance = p5.dist(self.x, self.y, p5.mouseX, p5.mouseY)
       if(distance < 10):
            self.y = self.y - self.speed
           

bullet = Bullet(150, 0, 2)  

def setup():
  p5.createCanvas(300, 300)  
  p5.rectMode(p5.CENTER)
  p5.imageMode(p5.CENTER)
  p5.textFont(font)
  p5.textSize(18)
  p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)

def draw():
  p5.background(0) 
  bullet.draw()

def keyPressed(event):#keys 1,2,3 to change state
    pass
def keyReleased(event):
    pass

def mousePressed(event): #press to change state
    pass

def mouseReleased(event):
    pass
