from tkinter import *
import math

window = Tk()
c = Canvas(window, width=200, height=200, bg='white')
c.pack()

def mainLines(a):
    c.create_arc(10, 10, 190, 190,
                 start=a, extent=0)
def smallLines(x, y, a):
    c.create_arc(x+20, y+20, x-20, y-20,
                 start=a, extent=0)

for i in range(0, 360, 45):
    mainLines(i)
    if i%90 == 0:
        if i%180 == 0:
            for n in range(0, 360, 45):
                smallLines(190-i, 100, n)
        else:
            for n in range(0, 360, 45):
                smallLines(100, 190-i+90, n)
    else:
        if i%135 == 0:
            for n in range(0, 360, 45):
                smallLines(100-(45*math.sqrt(2)), 100+(45*math.sqrt(2)), n)
        elif i%315 == 0:
            for n in range(0, 360, 45):
                smallLines(100+(45*math.sqrt(2)), 100-(45*math.sqrt(2)), n)
        else:
            if i%225 == 0:
                for n in range(0, 360, 45):
                    smallLines(100-(45*math.sqrt(2)), 100-(45*math.sqrt(2)), n)
            else:
                for n in range(0, 360, 45):
                    smallLines(100+(45*math.sqrt(2)), 100+(45*math.sqrt(2)), n)
