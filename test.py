import tkinter
import random

# constatint
WIDTH=1920
HEIGHT=1080
BG_COLOR="WHITE"
BAD_COLOR="red"
COLORS=['aqua','pink','green','yellow','gold',BAD_COLOR]
ZERO=0
MAIN_BALL_RADIUS=30
MAIN_BALL_COLOR='BLUE'
INIT_DX=1
INIT_DY=1
DELAY=10
COUNT_BALLS=10


# balls class
class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                           fill=self.color, outline=self.color if self.color!=BAD_COLOR else 'black')
    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                           fill=BG_COLOR, outline=BG_COLOR)
    def is_col(self,ball):
        a=abs(self.x+self.dx-ball.x)
        b=abs(self.y+self.dy-ball.y)
        return (a*a+b*b)**0.5<=self.r+ball.r
    def move(self):
        #wall
        if (self.x+self.r+self.dx >= WIDTH) or (self.x-self.r+self.dx <= ZERO):
            self.dx=-self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERO):
            self.dy=-self.dy

        #balls
        for ball in balls:
            if self.is_col(ball):
                if ball.color!=BAD_COLOR:
                    ball.hide()
                    balls.remove(ball)
                    self.dx=-self.dx
                    self.dy=-self.dy
                else:
                    self.dx=self.dy=0
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()

# mouse_event
def mouse_click(event):
    global main_ball
    if event.num==1:
        if 'main_ball' not in globals():
            main_ball=Balls(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR,INIT_DX,INIT_DY)
            main_ball.draw()
        else:
            if main_ball.dx*main_ball.dy>0:
                main_ball.dy=-main_ball.dy
            else:
                main_ball.dx=-main_ball.dx
    elif event.num==3:
        if main_ball.dx * main_ball.dy > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy

def create_list_to_ball(numbers):
    lst=[]
    while len(lst)<numbers:
        next_ball=Balls(random.choice(range(0, WIDTH)), random.choice(range(0, HEIGHT)), random.choice(range(15, 35)),
                        random.choice(COLORS))
        lst.append(next_ball)
        next_ball.draw()
    return lst

def count_bad_balls(list_of_balls):
    res=0
    for ball in list_of_balls:
        if ball.color==BAD_COLOR:
            res += 1
    return res
#main cicle
def main():
    if 'main_ball' in globals():
        main_ball.move()
        if len(balls) - num_of_bad_balls==0:
            canvas.create_text(WIDTH/2,HEIGHT/2,text="YOU WON!")
            main_ball.dx = 0
            main_ball.dy = 0
        elif main_ball.dx==0:
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text="YOU Lose!")
    root.after(DELAY, main)

root=tkinter.Tk()
root.title("Test")
canvas=tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-3>', mouse_click, "+")
if 'main_ball' in globals():
    del main_ball
balls=create_list_to_ball(COUNT_BALLS)
num_of_bad_balls=count_bad_balls(balls)
main()
root.mainloop()

