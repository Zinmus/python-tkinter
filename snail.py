from tkinter import*
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()
ball = canvas.create_oval(10,10,30,30, fill='red')
def midpoint(pos):
    return[(pos[0]+pos[2])/2, (pos[1]+pos[3])/2]
def move_oval(event):
    step = 3
    P1 = midpoint(canvas.coords(ball))
    if event.keysym == 'Up':
        canvas.move(ball, 0, -step)
    elif event.keysym == 'Down':
        canvas.move(ball, 0, step)
    elif event.keysym == 'Left':
        canvas.move(ball, -step, 0)
    elif event.keysym == 'Right':
        canvas.move(ball, step, 0)
    elif event.keysym == 'a':
        canvas.move(ball, -step, -step)
    elif event.keysym == 's':
        canvas.move(ball, step, -step)
    elif event.keysym == 'z':
        canvas.move(ball, -step, step)
    elif event.keysym == 'x':
        canvas.move(ball, step, step)
    canvas.create_line(P1, midpoint(canvas.coords(ball)), width=5, fill='green')
canvas.bind_all('<Key>',move_oval)
root.mainloop()
