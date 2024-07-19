import js as p5
from js import document
import math

img1 = p5.loadImage('Frame 52.png')
img2 = p5.loadImage('Group 31.png')
img3 = p5.loadImage('Group 4.png')

position = []

running = True
last_record_time = 0
record_interval = 50  # 10ms
pop_interval = 3000  # 300ms



def setup():
  p5.createCanvas(900, 600)
  # change mode to draw rectangles from center:
  p5.rectMode(p5.CENTER)
  # change mode to draw images from center:
  p5.imageMode(p5.CENTER)
  # change stroke cap to square:
  p5.strokeCap(p5.SQUARE)

def draw():


  
  global position, last_record_time, record_interval,pop_interval
  p5.background(255)
  p5.image(img1,450,300,900,600)
  p5.noStroke()

  current_time = p5.millis()
  if current_time - last_record_time >= record_interval:
    getMousePosition()
    last_record_time = current_time

  if len(position) >60:
    position.pop(0)

  for pos in position:
    p5.fill(255,pos[0]/3,pos[1]/3)
    p5.ellipse(math.ceil(pos[0]/75)*75, math.ceil(pos[1]/50)*50, 75,75)
    p5.fill(255,pos[0]/3,pos[1]/3,80)
    p5.ellipse(math.ceil(pos[0]/75)*75, math.ceil(pos[1]/50)*50, 100,100)
    p5.fill(255,pos[0]/3,pos[1]/3,50)
    p5.ellipse(math.ceil(pos[0]/75)*75, math.ceil(pos[1]/50)*50, 150,150)
 

  p5.image(img2,58,516,80,101)
  p5.image(img3,41,38,46,46)
  # # assign content of "data" div on index.html page to variable:
  # # split data_string by comma, making a list:







  # p5.ellipse(0, 0, value_x/20, value_y/20)


def getMousePosition():
  global position
  x = p5.mouseX
  y = p5.mouseY
  position.append((x,y))

def  polygon(x, y, radius, npoints):
  angle = p5.PI*2 / npoints
  p5.beginShape()
  i = 0
  while(i<p5.PI*2):
   
    sx = x + p5.cos(i) * radius
    sy = y + p5.sin(i) * radius
    p5. vertex(sx, sy)
    i += angle
  
  p5.endShape(p5.CLOSE)
