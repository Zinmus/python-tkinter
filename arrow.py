from tkinter import *
window = Tk()
c = Canvas(window, width=100, height=100, bg='white')
c.pack()
c.create_line(10,10,90,10)
c.create_line((50,20),(50,90),
              fill='green',
              width=3,
              arrow=FIRST,
              dash=(10,2),
              activefill='red',
              arrowshape="10 25 10")
window.mainloop()
