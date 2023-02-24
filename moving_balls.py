from tkinter import *
from random import *
from time import *

tk = Tk()
canvas = Canvas(tk, width = 500, height = 400)
canvas.pack()

class Ball:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x+50, y+50, fill = color)
        self.dy = 2

    def ruh(self):
        pos = canvas.coords(self.id)
        if pos[1] > 348 or pos[1] < 2: self.dy = -1*self.dy
        canvas.move(self.id, 0, self.dy)

list_ball = []
colors = ['red', 'orange', 'yellow', 'green', 'blue']
for i in range(10):
    x = randint(10, 400)
    y = randint(10, 350)
    list_ball.append(Ball(canvas, x, y, colors[i%5]))

def play():
    for i in range(len(list_ball)):
        list_ball[i].ruh()
    tk.update()
    tk.after(10, play)

play()
tk.mainloop()
