import js
p5 = js.window
program_time = p5.millis()
program_state = 'STATE1'
e1=150
e2=170
e3=190
x=150
change = 1
speed = 1


def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')


def draw():
    global program_time, program_state,e1,e2,e3,x,change,speed
    p5.background(255)   
    p5.fill(0)
    p5.text('program_state = ' + program_state, 10, 70)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.text('milliseconds: ' + str(program_time), 10, 35)
    sec = int(program_time / 1000)
    p5.text('seconds: ' + str(sec), 10, 55)
    p5.noFill()

    if(p5.millis() > program_time + 3000):
        program_state = 'STATE2'
        program_time = p5.millis()
       
    if(program_state == 'STATE2'):
        e1 = e1-change
        e2 = e2-change
        e3 = e3-change
        if ( e1 <= 0 or e1>x or e1>300-x):
            change =-change
        draw_circle()
        
    if(program_state == 'STATE3'):
        move_circle()
        draw_circle()
        
    if(program_state == 'STATE1'):
        p5.rect(75,75,150,150)
        
def move_circle():
    global x,e1,e2,e3,speed
    x = x+speed
    if (x>e3/2 and x<p5.width-e3/2):
        speed = speed
    else:
        speed = -speed


def draw_circle():
    global x,e1,e2,e3
    p5.ellipse(x,150,e1,e1)
    p5.ellipse(x,150,e2,e2)
    p5.ellipse(x,150,e3,e3) 
    
def keyPressed(event):
    global program_state
    if(str(p5.key) == '1'):
        program_state = 'STATE1'
    if(str(p5.key) == '2'):
        program_state = 'STATE2'
    if(str(p5.key) == '3'):
        program_state = 'STATE3'
    print('change program_state to ' + program_state)
def keyReleased(event):
    pass

def mousePressed(event):
    global program_time
    global program_state
    program_state = 'STATE3'
    print('change program_state to ' + program_state)
    program_time = p5.millis()


def mouseReleased(event):
    print('mouseReleased..')
