import js
a = -40;
b =-40
arr = []
i=0
x=0
p5 = js.window

def setup():
    p5.createCanvas(500, 500)   # 300 x 300 pixel canvas 

def draw_orange_circle(x,y):   # draw face 
    p5.noStroke();
    p5.fill(245,227,189)
    p5.ellipse(x,y,30,30)
    p5.fill(208,152,52)
    p5.ellipse(x,y,25,25)
    p5.fill(245,227,189)
    p5.ellipse(x,y,15,15)
    p5.fill(196,107,39)
    p5.ellipse(x+((p5.mouseX-x)/60),y+((p5.mouseY-y)/60),7,7)



def draw_closed_orange(x,y):
    p5.noStroke();
    p5.fill(142, 125, 102)
    p5.ellipse(x,y,30,30)
    p5.fill(99, 86, 78)
    p5.ellipse(x,y,25,25)
    p5.noFill()
    p5.stroke(48,33,12)
    p5.strokeWeight(5)
    p5.arc(x,y-28,60,60,p5.radians(70), p5.radians(110))



def draw_blue_circle(x,y):   # draw face 
    p5.noStroke();
    p5.fill(132,137,142)
    p5.ellipse(x,y,30,30)
    p5.fill(74,94,182)
    p5.ellipse(x,y,25,25)
    p5.fill(29,51,119)
    p5.ellipse(x,y,15,15)
    p5.fill(195,204,218)
    p5.ellipse(x+((p5.mouseX-x)/60),y+((p5.mouseY-y)/60),7,7)

def draw_closed_blue(x,y):
    p5.noStroke();
    p5.fill(134, 141, 145)
    p5.ellipse(x,y,30,30)
    p5.fill(91, 106, 114)
    p5.ellipse(x,y,25,25)
    p5.noFill()
    p5.stroke(41,62,78)
    p5.strokeWeight(5)
    p5.arc(x,y-28,60,60,p5.radians(70), p5.radians(110))




def draw_small_circle(x,y):   # draw face 
    p5.noStroke();
    p5.fill(196,107,39)
    p5.ellipse(x,y,7,7)

def draw():
    global a,b, arr,i
    p5.background(211,196,153) 




    for i in range(6):
        for j in range (6):
            draw_orange_circle(-30+i*60,0+j*60)

        for k in range (6):
            draw_orange_circle(i*60,-30+k*60)






    for i in range(6):
        for j in range (6):
            draw_blue_circle(+i*60,+j*60)
            
        for k in range (6):
            draw_blue_circle(30+i*60,30+k*60)
           



    for i in range(11):
        for j in range (11):
            draw_small_circle(15+i*30 ,15+j*30)

    if (p5.mouseIsPressed == True and not [p5.mouseX,p5.mouseY] in arr):
        a=p5.mouseX
        b=p5.mouseY
        arr.append([a,b])

    for i in range(len(arr)):
        if (x%2 == 0):
            if(p5.parseInt((arr[i][0]-15)/30, 10) % 2 == 1 and p5.parseInt((arr[i][1]-15)/30, 10)%2 == 0):
                draw_closed_orange(p5.parseInt((arr[i][0]-15)/30, 10)*30+30,p5.parseInt((arr[i][1]-15)/30, 10)*30+30)
            if(p5.parseInt((arr[i][0]-15)/30, 10) % 2 == 1 and p5.parseInt((arr[i][1]-15)/30, 10)%2 == 1):
                draw_closed_blue(p5.parseInt((arr[i][0]-15)/30, 10)*30+30,p5.parseInt((arr[i][1]-15)/30, 10)*30+30)
            if(p5.parseInt((arr[i][0]-15)/30, 10) % 2 == 0 and p5.parseInt((arr[i][1]-15)/30, 10)%2 == 1):
                draw_closed_orange(p5.parseInt((arr[i][0]-15)/30, 10)*30+30,p5.parseInt((arr[i][1]-15)/30, 10)*30+30)
            if(p5.parseInt((arr[i][0]-15)/30, 10) % 2 == 0 and p5.parseInt((arr[i][1]-15)/30, 10)%2 == 0):
                draw_closed_blue(p5.parseInt((arr[i][0]-15)/30, 10)*30+30,p5.parseInt((arr[i][1]-15)/30, 10)*30+30)




    if (p5.mouseIsPressed == True and [p5.mouseX,p5.mouseY] in arr):
        
        if(p5.parseInt((arr[i][0]-15)/30, 10) % 2 == 1 and p5.parseInt((arr[i][1]-15)/30, 10)%2 == 0):
            draw_orange_circle(p5.parseInt((arr[i][0]-15)/30, 10)*30+30,p5.parseInt((arr[i][1]-15)/30, 10)*30+30)
        if(p5.parseInt((arr[i][0]-15)/30, 10) % 2 == 1 and p5.parseInt((arr[i][1]-15)/30, 10)%2 == 1):
            draw_blue_circle(p5.parseInt((arr[i][0]-15)/30, 10)*30+30,p5.parseInt((arr[i][1]-15)/30, 10)*30+30)
        if(p5.parseInt((arr[i][0]-15)/30, 10) % 2 == 0 and p5.parseInt((arr[i][1]-15)/30, 10)%2 == 1):
            draw_orange_circle(p5.parseInt((arr[i][0]-15)/30, 10)*30+30,p5.parseInt((arr[i][1]-15)/30, 10)*30+30)
        if(p5.parseInt((arr[i][0]-15)/30, 10) % 2 == 0 and p5.parseInt((arr[i][1]-15)/30, 10)%2 == 0):
            draw_blue_circle(p5.parseInt((arr[i][0]-15)/30, 10)*30+30,p5.parseInt((arr[i][1]-15)/30, 10)*30+30)
