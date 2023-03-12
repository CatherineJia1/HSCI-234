#if players are close to each other they will became red. 
#if players are touch each other, the game would reset
#press right,left,up,down arrow to control the direction of first player


import js
p5 = js.window
speed=0.3



class Player:  
    def __init__(self, x = 100, y = 150, state = "Up"):
        self.x = x  # initialize attribute x 
        self.y = y  # initialize attribute y 
        self.state = state# initialize attribute state

    def set_player(self, x, y):  #reset position
        self.x = x  
        self.y = y

    def move_player(self, distance_x, distance_y):#move player
        self.x += distance_x
        self.y += distance_y

    def update(self,state): #chang state
        self.state=state

    # method to draw a Point object:
    def draw(self):
        if(p5.dist(player_1.x, player_1.y,player_2.x,player_2.y)<60):  #if players are close to each other turn red
            p5.fill(256,0,0)
            if(p5.dist(player_1.x, player_1.y,player_2.x,player_2.y)<50):#if players touched each other, reset
                player_1.set_player(100,150)
                player_2.set_player(200,150)
        else:
            p5.noFill()
        p5.push()
        
        p5.translate(self.x, self.y)
        if(self.state == 'Right'): #change direction of player according to state
            p5.rotate(p5.radians(360/4))
        if(self.state == 'Left'):  
            p5.rotate(p5.radians(360/4*3))  
        if(self.state == 'Down'):
            p5.rotate(p5.radians(180))
        p5.ellipse(0, 0, 50, 50)
        p5.ellipse(-10,-5,10,10)
        p5.ellipse(10,-5,10,10)
        p5.arc(0,15,10,10,1,-4)        
        p5.pop()
        
player_1 = Player()
player_2 = Player(200,150,"Up")

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
    
def draw():
    global speed
    p5.background(255)
    player_1.draw() 
    player_2.draw()
    if(player_2.x > 250 or player_2.x < 50): #make player2 move automaticlaly
        speed = -speed
    player_2.x += speed




    
def keyPressed(event): #when key is pressed cmove the player and change the state. 
    if(p5.keyCode == p5.RIGHT_ARROW):
        print('move point 10 pixels to the right..')
        player_1.move_player( 10, 0)
        player_1.update("Right")
        
    if(p5.keyCode == p5.LEFT_ARROW):
        print('move point 10 pixels to the right..')
        player_1.move_player( -10, 0)
        player_1.update("Left")
    if(p5.keyCode == p5.UP_ARROW):
        print('move point 10 pixels to the right..')
        player_1.move_player( 0, -10)
        player_1.update("Up")
    if(p5.keyCode == p5.DOWN_ARROW):
        print('move point 10 pixels to the right..')
        player_1.move_player( 0, 10)
        player_1.update("Down")
