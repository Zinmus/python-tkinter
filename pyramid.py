from tkinter import *
window = Tk()
c = Canvas(window, width=200, height=200, bg='white')
c.pack()

def drawPyramid(n, r=1, x=0, y=0):
    if n > 0:
        if r > 0:
            if r%2 == 0:
                c.create_rectangle(x, y, x+40, y+20)
                drawPyramid(n, r-1, x+40, y)
            else:
                c.create_rectangle(x, y, x+40, y+20)
                drawPyramid(n, r-1, x+40, y)
        else:
            drawPyramid(n-1,12-n, 0, y+20)

drawPyramid(10)

window.mainloop()
