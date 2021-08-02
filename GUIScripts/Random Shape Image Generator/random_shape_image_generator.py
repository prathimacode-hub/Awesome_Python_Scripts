
# Random Shape Image Generator

from tkinter import *
import tkinter.messagebox as mbox
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageDraw, ImageTk
from random import randint, randrange

# created a main window
window = Tk()
window.title("Random Shape Image Generator")
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "Random Shape Image\nGenerator", font=("Arial", 50, "underline"), fg="magenta") # same way bg
start1.place(x = 150, y = 10)

# top label
start1 = tk.Label(text = "Click on below button to generate\nrandom shape images", font=("Arial", 40), fg="green") # same way bg
start1.place(x = 100, y = 180)

# function defined to generate random images with some overlapping
def overlap_fun():
    window.destroy()
    WIDTH, HEIGHT = 1000, 700
    COUNT = 40

    # Use datetime (somehow), to generate random int.
    def datetimeToInt():
        y, m, d, hour, min, sec = datetime.now().timetuple()[0:6]
        return y + m + d + hour + min + sec

    def randRgb():
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    def randTriangle():
        x1, y1 = randrange(0, WIDTH), randrange(0, HEIGHT)
        x2, y2 = randrange(0, WIDTH), randrange(0, HEIGHT)
        x3, y3 = randrange(0, WIDTH), randrange(0, HEIGHT)
        return [(x1, y1), (x2, y2), (x3, y3)]

    def randRect():
        x1, y1 = randrange(0, WIDTH), randrange(0, HEIGHT)
        x2, y2 = randrange(0, WIDTH), randrange(0, HEIGHT)
        return [(x1, y1), (x2, y2)]

    randEllipse = randRect

    # Map: random shape creation functions -> ImageDraw methods
    shapeFactories = [
        (randTriangle, ImageDraw.ImageDraw.polygon),
        (randRect, ImageDraw.ImageDraw.rectangle),
        (randEllipse, ImageDraw.ImageDraw.ellipse)
    ]
    shapeFactoriesCount = len(shapeFactories)

    composite = Image.new('RGBA', (WIDTH, HEIGHT), '#00000000')
    draw = ImageDraw.Draw(composite)
    for x in range(COUNT):
        # Get random index, within full range:
        # randIdx = randrange(0, shapeFactoriesCount)
        # Use random int, generated from datetime (somehow):
        randIdx = datetimeToInt() % shapeFactoriesCount
        shapeFactory, drawMethod = shapeFactories[randIdx]

        drawMethod(  # passing 'self'/'draw' explicitly to method:
            draw, shapeFactory(), fill=randRgb(), outline=randRgb()
        )

    root1 = tk.Tk()
    root1.title("Random Shape Images with Overlapping")
    compositeTk = ImageTk.PhotoImage(composite)
    tk.Label(root1,image=compositeTk).pack()
    root1.mainloop()

# created button
exitb = Button(window, text="GENERATE WITH OVERLAPPING",command=overlap_fun,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =275 , y =350 )

# function defined to generate random images without some overlapping
def normal_fun():
    window.destroy()
    WIDTH, HEIGHT = 50, 60
    COUNT = 100

    # Use datetime (somehow), to generate random int.
    def datetimeToInt():
        y, m, d, hour, min, sec = datetime.now().timetuple()[0:6]
        return y + m + d + hour + min + sec

    def randRgb():
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    def randTriangle():
        x1, y1 = randrange(0, WIDTH), randrange(0, HEIGHT)
        x2, y2 = randrange(0, WIDTH), randrange(0, HEIGHT)
        x3, y3 = randrange(0, WIDTH), randrange(0, HEIGHT)
        return [(x1, y1), (x2, y2), (x3, y3)]

    def randRect():
        x1, y1 = randrange(0, WIDTH), randrange(0, HEIGHT)
        x2, y2 = randrange(0, WIDTH), randrange(0, HEIGHT)
        return [(x1, y1), (x2, y2)]
        return

    randEllipse = randRect

    # Map: random shape creation functions -> ImageDraw methods
    shapeFactories = [
        (randTriangle, ImageDraw.ImageDraw.polygon),
        (randRect, ImageDraw.ImageDraw.rectangle),
        (randEllipse, ImageDraw.ImageDraw.ellipse)
    ]
    shapeFactoriesCount = len(shapeFactories)

    imgOpenList = []
    imgClosedList = []
    for x in range(COUNT):
        # Get random index, within full range:
        # randIdx = randrange(0, shapeFactoriesCount)
        # Use random int, generated from datetime (somehow):
        randIdx = datetimeToInt() % shapeFactoriesCount
        shapeFactory, drawMethod = shapeFactories[randIdx]

        im_open = Image.new('RGBA', (WIDTH, HEIGHT), '#00000000')
        draw = ImageDraw.Draw(im_open)
        drawMethod(  # passing 'self'/'draw' explicitly to method:
            draw, shapeFactory(), fill=randRgb(), outline=randRgb()
        )

        imgOpenList.append(im_open)
        imgClosedList.append(im_open.rotate(90))

    # The rest is just for displaying the resulting images.

    import tkinter as tk

    from math import floor, sqrt

    root2 = tk.Tk()
    root2.title("Random Shape Images without Overlapping")

    imgOpenList = [
        ImageTk.PhotoImage(img) for img in imgOpenList
    ]
    imgClosedList = [
        ImageTk.PhotoImage(img) for img in imgClosedList
    ]

    imgsPerAxis = floor(sqrt(COUNT))  # rough approximation
    canvas = tk.Canvas(
        root2,
        width=WIDTH * imgsPerAxis * 2,  # x2: open & closed images
        height=HEIGHT * imgsPerAxis
    )
    canvas.pack()

    for i in range(imgsPerAxis):
        for j in range(imgsPerAxis):
            canvas.create_image(
                2 * j * WIDTH, i * HEIGHT,
                image=imgOpenList[i * imgsPerAxis + j],
                anchor=tk.NW
            )
            canvas.create_image(
                (2 * j + 1) * WIDTH, i * HEIGHT,
                image=imgClosedList[i * imgsPerAxis + j],
                anchor=tk.NW
            )

    root2.mainloop()

# created button
exitb = Button(window, text="GENERATE WITHOUT OVERLAPPING",command=normal_fun,font=("Arial", 20), bg = "yellow", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =250 , y =450 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =460 , y =580 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
