from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image as Im

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"


def select_watermark():
    # RETRIEVE PATH OF IMAGE
    filename = askopenfilename(filetypes=(("jpg file", "*.jpg"), ("png file", '*.png')))
    image1 = Im.open(filename)
    # RE-SIZE
    size = (150, 150)
    image1.thumbnail(size)
    # SAVE
    image1.save("water_mark.png")
    messagebox.showinfo('DONE', 'The Selected imaged is ready to be inserted to your main image as a 150px by 150px '
                                'watermark\n\n Select your main Image.')


def add_watermark():
    # RETRIEVE PATH OF IMAGE
    filename = askopenfilename(filetypes=(("jpg file", "*.jpg"), ("png file", '*.png')))

    # OPEN SELECTED FILE WITH PILLOW
    base = Im.open(filename)

    # OPEN DESIRED WATERMARK (SMALL PICTURE FILE INSIDE SAME LEVEL DIRECTORY)
    watermark = Im.open('water_mark.png')

    # GET DIMENSIONS OF SELECTED FILE AND USE THEM TO POSITION WATERMARK
    width, height = base.size
    pos = (int(width * .85), int(height * .85))

    # PASTE WATERMARK INTO IMAGE
    base.paste(watermark, pos)
    # SAVE WATERMARKED IMAGE AT SPECIFIED DIRECTORY
    output = 'images/' + 'watermarked.png'
    base.save(output)
    messagebox.showinfo('SUCCESS', 'Success!\nYour image has been watermarked and saved.\n\n '
                                   'You can find it in the images folder as: "watermarked.png" ')
    window.quit()


# ---------------------------GUI-------------------------------
window = Tk()
window.title("Water Mark Inserter")
window.config(padx=50, pady=50, bg='black')

# ------------------------------ LABEL--------------------------
heading_label = Label(text='WATERMARK INSERTER', font=(FONT_NAME, 40, 'bold'), bg='BLACK', fg=GREEN)
heading_label.grid(row=0, column=1, columnspan=3)

label = Label(window, text="Add the the following watermark to the bottom corner of your images", fg=YELLOW, bg='black')
label.grid(row=1, column=1, columnspan=3)

# ----------------------------- BUTTONS--------------------------
b1 = Button(window, text="CHOOSE WATER MARK PICTURE FILE", font=40, command=select_watermark, highlightthickness=1)
b1.grid(row=3, column=2, pady=10)
b1 = Button(window, text="CHOOSE MAIN PICTURE", font=40, command=add_watermark, highlightthickness=1)
b1.grid(row=4, column=2, pady=10)

window.mainloop()
