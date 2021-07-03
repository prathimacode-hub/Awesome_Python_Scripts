
# Camera Application

# imported necessary library
import cv2
import time
import threading
from cv2 import cv2
from PIL import Image, ImageTk
from tkinter import Label, Button, Tk, PhotoImage
from tkinter import filedialog
import tkinter.messagebox as mbox

# created a class for camera application where main application is created
class CameraApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Camera Application")
        self.window.geometry("1000x700")
        # self.window.configure(bg="gray")
        self.window.resizable(1, 1)
        Label(self.window, width=1000, height=600, bg="light yellow").place(x=0, y=320)
        # self.topLabel = Label(self.window, text = "CAMERA" , font=("Arial", 40),fg="magenta", bg="light green")
        self.TakePhoto_b = Button(self.window, text="Take a Shot", font=("Arial", 20), bg="light green", fg = "blue", relief='raised',command=self.TakePhoto)
        self.see_b = Button(self.window, text="SEE THIS", font=("Arial", 20), bg="orange", fg = "blue", relief='raised',command=self.see_this)

        # self.prev_b = Button(self.window, text="PREVIEW", font=("Arial", 20), bg="orange", fg = "blue", relief='raised',command=self.prev_img)
        self.exit_b = Button(self.window, text="EXIT", font=("Arial", 20), bg="red", fg = "blue", relief='raised',command=self.exit_win)
        self.ImageLabel = Label(self.window, width=1000, height=500, bg="light yellow")
        self.ImageLabel.place(x=0, y=0)
        self.TakePhoto_b.place(x=150, y=560)
        # self.prev_b.place(x=440, y=560)
        self.see_b.place(x=440, y=560)
        self.exit_b.place(x = 750, y = 560)
        # self.topLabel.place(x = 250, y = 20)
        self.take_picture = False
        self.PictureTaken = False
        self.Main()

    # method for loading the camera
    @staticmethod
    def LoadCamera():
        camera = cv2.VideoCapture(0)
        if camera.isOpened():
            ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            if ret:
                yield frame
            else:
                yield False

    # method for exiting the window
    def exit_win(self):
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            self.window.destroy()

    # def prev_img(self):
    #     self.window1 = Tk()
    #     self.window1.title("Your Image")
    #     self.window1.geometry("1000x700")
    #
    #     # image on the main window
    #     path = "myimage.png"
    #     # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    #     img1 = ImageTk.PhotoImage(Image.open(path))
    #     # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    #     panel = Label(self.window1, image=img1)
    #     panel.place(x=260, y=250)

    # method to show how camera works
    def see_this(self):
        mbox.showinfo("Details", "When you click on Take a Shot, It will show a message of taking image.\n\nWhen we click on OK, it will ask user to save at any location in local system.\n\nAfter saving, it will show message, that File Saved Successfully.\n\nAfter that when user click on Take Again button, it willl give a message og reconfiguring camera, and clicking on the OK will start the camera and user can take the shot again.")

    # method defined to take the photo
    def TakePhoto(self):
        if not self.PictureTaken:
            # print('Taking a Picture')
            mbox.showinfo("Status", "Taking Picture")
            self.take_picture = True
        else:
            # print("Reconfiguring camera")
            mbox.showinfo("Status", "Reconfiguring camera")
            self.TakePhoto_b.configure(text="Take a Shot")
            self.take_picture = False

    # main method defined
    def Main(self):
        self.render_thread = threading.Thread(target=self.StartCamera)
        self.render_thread.daemon = True
        self.render_thread.start()

    # method to start the camera
    def StartCamera(self):
        frame = self.LoadCamera()
        CaptureFrame = None
        while True:
            Frame = next(frame)
            # print(self.take_picture)
            if frame and not self.take_picture:
                picture = Image.fromarray(Frame)
                picture = picture.resize((700, 450), resample=0)
                CaptureFrame = picture.copy()
                picture = ImageTk.PhotoImage(picture)
                self.ImageLabel.configure(image=picture)
                self.ImageLabel.photo = picture
                self.PictureTaken = False
                time.sleep(0.001)
            else:
                if not self.PictureTaken:
                    # print("Your camera died")
                    # mbox.showinfo("Status","Your camera died")

                    CaptureFrame.save('myimage.png')

                    img = cv2.imread('myimage.png')
                    edge = Image.fromarray(img)
                    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
                    if not filename:
                        mbox.showinfo("Success", "Image not saved!")
                        break
                    else:
                        edge.save(filename)
                    mbox.showinfo("Success", "Image Saved Successfully!")

                    self.TakePhoto_b.configure(text="Take Again")
                    self.PictureTaken = True

# function defined for exiting the window
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

root = Tk()
App = CameraApp(root)
root.protocol("WM_DELETE_WINDOW", exit_win1)
root.mainloop()