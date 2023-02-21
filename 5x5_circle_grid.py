import tkinter as tk

root = tk.Tk()
w = tk.Canvas(root, width=300, height=300)
w.pack()

def draw_circle(x, y):
    w.create_oval(x-30, y-30, x+30, y+30, outline="black")

for i in range(5):
    for j in range(5):
        draw_circle(60*i+30, 60*j+30)

root.mainloop()
