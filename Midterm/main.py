import js
p5 = js.window
#problem 1
#for the square at top left, it appears when mouse is pressed
# for the square at top right, it changed the opacity as well as created a loop of square but it is steady
#for the square at the bottom left, it would change color when the mouse is inside. Also, it create a random loop of sqaure
#for the square at the bottom right, it is created by using moveto and lineto 
random_size = p5.parseInt(p5.random(25, 125), 10) #problem 1
random_size2= p5.parseInt(p5.random(25, 125), 10)
random_size3 = p5.parseInt(p5.random(25, 125), 10)
random_size4 = p5.parseInt(p5.random(25, 125), 10)

alpha = 0

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    print('finished setup')
    p5.rectMode(p5.CENTER)
    
def draw():

    global random_size,random_size2,random_size3,random_size4, alpha
    
    p5.background(255)           # white background
    p5.noStroke()
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.strokeWeight(2)  # set stroke thickness
    p5.text(random_size, 10, 30) #problem 1

    #Square at left top
    #random_square(random_size) #call function from problem 3
    if(p5.mouseIsPressed == True): #problem 7, square only shows up when mouse is pressed
        p5.stroke(255, 127, 54)
        random_square_at(10,10,random_size)  #problem 6 call function from problem 5
       
 
    #Square at right top, the opacity of this square would change
    p5.stroke(127, 0, 255, alpha)
    random_square_loop(175,10,random_size2) #problem 6 call function from problem 5
    alpha = alpha + 1
    if(alpha ==255):
        alpha = 0
        
    #Square at left bottom the color of stroke would change the mouse is inside. 
    p5.stroke(127, 200, 0)
    if(inside_square(10,175,random_size3)):
        p5.stroke(127, 0, 255)     
    random_happy_square_loop(10,175,random_size3) #problem 6 call function from problem 5

    #create by move to and line to by using the new_random_square function
    p5.stroke(255, 0, 127)
    new_random_square_at(175,175,random_size4) #problem 6 call function from problem 5

#problem3   
def random_square(size):

    p5.line(0,0,size,0) #this is original problem2 
    p5.line(size,0,size,size)
    p5.line(size,size,0,size)
    p5.line(0,size,0,0)
    
#problem 5
def random_square_at(x, y, size):
    p5.push() 
    p5.translate(x,y)  #this is the original problem 4. 
    p5.line(0,0,size,0)
    p5.line(size,0,size,size)
    p5.line(size,size,0,size)
    p5.line(0,size,0,0)
    p5.pop()
    
#problem 10
def  inside_square(x,y,size):
    #this is the code for question 9. Just change x, y to the square position and size to square size then it would works,
    if( p5.mouseX > x and p5.mouseX< x + size and p5.mouseY > y and p5.mouseY < y+size): 
        return True
    else:
        return False
        
#problem 11
def new_random_square_at(x, y, size):
    p5.push()
    moveto(x,y)
    lineto(size,0)
    p5.pop()

    p5.push()
    moveto(x+size,y)
    lineto(0,size)
    p5.pop()

    p5.push()
    moveto(x+size,y+size)
    lineto(-size,0)
    p5.pop()
    
    p5.push()
    moveto(x,y+size)
    lineto(0,-size)
    p5.pop()
    #it can also be finished by using only one push and pop. However, i choose to do mutiply times becuase I want to keep the code in lineto simplier.
def moveto(x,y):   #problem 11 move the starting point
    p5.translate(x,y)
    
def lineto(a,b):   #problem 11 Draw from the starting point to end point(a,b)
    p5.line(0,0,a,b)

#problem 12
def random_decrease_number(num1):
    return p5.random(0, num1)#(a boucing happy square)

def random_square_loop(x, y, size):
    a = random_decrease_number(5)
    random_square_at(x,y,size)
    for i in range (3):
        #random_square_at(x+a*i,y+a*i,size-a*2*i) #(boucing happy square if you want to see it delete the "#" in the front)
        random_square_at(x+5*i,y+5*i,size-5*2*i)
        
def random_happy_square_loop(x, y, size):
    a = random_decrease_number(5)
    random_square_at(x,y,size)
    for i in range (3):
        random_square_at(x+a*i,y+a*i,size-a*2*i) #(boucing happy square if you want to see it delete the "#" in the front)
        #random_square_at(x+5*i,y+5*i,size-5*2*i)
        


    #problem 2 This is what problem 2 originally looks like. For Problem 3, the parameter was changed from random_size to size. 
    #p5.line(0,0,random_size,0)
    #p5.line(random_size,0,random_size,random_size)
    #p5.line(random_size,random_size,0,random_size)
    #p5.line(0,random_size,0,0)
