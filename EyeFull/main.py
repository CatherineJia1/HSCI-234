import js
a = -40;
b =-40
arr = []
x=0
p5 = js.window




def setup():
    p5.createCanvas(1512, 982)    # 300 x 300 pixel canvas 

def draw_orange_circle(x,y):   # draw orange eye
    p5.noStroke();
    p5.fill(245,227,189)
    p5.ellipse(x,y,60,60)
    p5.fill(208,152,52)
    p5.ellipse(x,y,50,50)
    p5.fill(245,227,189)
    p5.ellipse(x,y,30,30)
    p5.fill(196,107,39)
    p5.ellipse(x+((p5.mouseX-x)/100),y+((p5.mouseY-y)/100),14,14)



def draw_closed_orange(x,y):   # draw closed orange eye
    p5.noStroke();
    p5.fill(142, 125, 102)
    p5.ellipse(x,y,60,60)
    p5.fill(99, 86, 78)
    p5.ellipse(x,y,50,50)
    p5.noFill()
    p5.stroke(48,33,12)
    p5.strokeWeight(10)
    p5.arc(x,y-56,120,120,p5.radians(70), p5.radians(110))



def draw_blue_circle(x,y):   # draw blue eye
    p5.noStroke();
    p5.fill(132,137,142)
    p5.ellipse(x,y,60,60)
    p5.fill(74,94,182)
    p5.ellipse(x,y,50,50)
    p5.fill(29,51,119)
    p5.ellipse(x,y,30,30)
    p5.fill(195,204,218)
    p5.ellipse(x+((p5.mouseX-x)/120),y+((p5.mouseY-y)/120),14,14)

def draw_closed_blue(x,y): # draw closed blue eye
    p5.noStroke();
    p5.fill(134, 141, 145)
    p5.ellipse(x,y,60,60)
    p5.fill(91, 106, 114)
    p5.ellipse(x,y,50,50)
    p5.noFill()
    p5.stroke(41,62,78)
    p5.strokeWeight(10)
    p5.arc(x,y-56,120,120,p5.radians(70), p5.radians(110))




def draw_small_circle(x,y):   # small circle
    p5.noStroke();
    p5.fill(196,107,39)
    p5.ellipse(x,y,14,14)
    

def draw():
    global a,b, arr
    p5.background(211,196,153) 

    for i in range(20):            # draw orange & blue eye in canvas using loop
        for j in range (20):
            draw_orange_circle(-60+i*120,0+j*120)

        for k in range (20):
            draw_orange_circle(i*120,-60+k*120)

    for i in range(20):
        for j in range (20):
            draw_blue_circle(+i*120,+j*120)
            
        for k in range (20):
            draw_blue_circle(60+i*120,60+k*120)
           



    for i in range(32):
        for j in range (32):
            draw_small_circle(30+i*60 ,30+j*60)






    if(p5.mouseIsPressed == True):    # when mouse is pressed, record the position of mouse 
        a = p5.parseInt((p5.mouseX-30)/60, 10) # mapping the mouse's position into range 0-6. 
#The reason I tranform mouse position using parseInt is because I need to make sure that after mapping, 
#for each eyeball shape, no matter where the user click, the position of mouse would remain the same, so that the eyeball could change
#position that in the arr, the eyeball will be close, vice versa. 
        b = p5.parseInt((p5.mouseY-30)/60, 10) 
        if ([a,b] in arr):
            arr.remove([a,b])  # removed from the arr, when it is already in the arr. That is another reason I need to do the mapping before.
        else:
             arr.append([a,b]) # add it to the arr when it is not exist. 
    if (p5.keyIsPressed == True and p5.key == 'r'):
        arr = []
        
    for i in range(len(arr)):  # draw closed eyes based on arr
        if(arr[i][0] % 2 == 1 and arr[i][1]%2 == 0):
            draw_closed_orange(arr[i][0]*60+60,arr[i][1]*60+60)
        if(arr[i][0] % 2 == 1 and arr[i][1]%2 == 1):
            draw_closed_blue(arr[i][0]*60+60,arr[i][1]*60+60)
        if(arr[i][0] % 2 == 0 and arr[i][1]%2 == 1):
            draw_closed_orange(arr[i][0]*60+60,arr[i][1]*60+60)
        if(arr[i][0] % 2 == 0 and arr[i][1] %2 == 0):
            draw_closed_blue(arr[i][0]*60+60,arr[i][1]*60+60)
