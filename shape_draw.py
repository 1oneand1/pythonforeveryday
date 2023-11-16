import tkinter as tk
import turtle 

def draw_shape(turtle, lenght):
    for _ in range(17):
        turtle.forward(lenght)
        turtle.right(190)

root = tk.Tk()
canvas = tk.Canvas(master = root, width = 700, height = 700)
canvas.pack()

t = turtle.RawTurtle(canvas)
draw_shape(t, 100)

def continue_drawing():
    draw_shape(t, 200)
    canvas.after(200, continue_drawing)

def continious_drawing():
    draw_shape(t, 250)
    canvas.after(250, continious_drawing)


continue_drawing()
continious_drawing()

root.mainloop()