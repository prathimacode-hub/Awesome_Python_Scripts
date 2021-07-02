

# imported necessary libraries
import tkinter as tk
import tkinter.ttk
import tkinter.messagebox as mbox

# created 5 screens
screens = ["Screen 1", "Screen 2", "Screen 3", "Screen 4", "Screen 5", "Screen 6"]

# created list of movies according to genre
movies = {"Horror": ["The Nun", "Dracula Untold", "Feral", "Shin Godzilla", "Black Death"],
          "Action": ["Venom", "Robin Hood", "Aquaman", "Artemis Fowl", "The Predator"],
          "Drama": ["Creed", "Creed 2", "Outlaw King", "Peppermint", "Sicario: Day of the Soldado"],
          "Comedy": ["Step Brothers", "The Hangover", "Horrible Bosses", "The Other Guys", "Let's Be Cops"],
          "Sci-Fi": ["The Matrix", "Solaris", "Blade Runner", "Interstellar", "Sunshine"],
          "Romance": ["Ghost", "Sliding Doors", "50 Shades of Grey", "Titanic", "La La Land"]}

# created list of time
times = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
         "22:00", "23:00"]

# declared global variable
seatList = []
seatSelected = []
s = ""
t = ""
genre = ""
movie = ""


# created a class application where main application is created
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.title('MOVIE BOOKING')
        self.createWidgets()

    # function defined to update the movies according to genre
    def updateMovies(self, event=None):
        self.movieCombo['values'] = movies[self.genreCombo.get()]

    # function defined to create different widgets
    def createWidgets(self):
        headingLabel = tk.Label(self, text="MOVIE BOOKING", font=("Arial", 50), fg="magenta",underline=0)
        headingLabel.place(x = 200, y = 20)

        daylbl = tk.Label(self, text="TODAY", font=("Arial", 40), fg="brown")

        daylbl.place(x = 50, y = 150)

        # created label for genre
        generelbl = tk.Label(self, text="GENRE", font=("Arial", 40), fg="brown")
        generelbl.place(x = 345, y = 150)
        self.genreCombo = tkinter.ttk.Combobox(self, width=15, values=list(movies.keys()), font=("Arial", 20), state="readonly")
        self.genreCombo.set("SELECT GENRE")
        self.genreCombo.bind('<<ComboboxSelected>>', self.updateMovies)
        self.genreCombo.place(x=320, y=230)

        # created label for movie
        movielbl = tk.Label(self, text="MOVIE", font=("Arial", 40), fg="brown")
        movielbl.place(x = 680, y = 150)
        self.movieCombo = tkinter.ttk.Combobox(width=15, font=("Arial", 20), state="readonly")
        self.movieCombo.bind('<<ComboboxSelected>>', self.createTimeButtons)
        self.movieCombo.set("SELECT MOVIE")
        self.movieCombo.place(x=650, y=230)

    # function defined to display time button
    def createTimeButtons(self, event=None):
        global genre, movie
        genre = self.genreCombo.get()
        movie = self.movieCombo.get()

        # label created for time
        timelbl = tk.Label(self, text='Select Time Slot', font=("Arial", 30), fg="green")
        timelbl.place(x = 350, y = 300)

        # created 14 different time buttons
        tk.Button(self, text=times[0], command=lambda : self.seatSelection(times[0]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 80, y = 380)
        tk.Button(self, text=times[1], command=lambda : self.seatSelection(times[1]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 200, y = 380)
        tk.Button(self, text=times[2], command=lambda : self.seatSelection(times[2]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 320, y = 380)
        tk.Button(self, text=times[3], command=lambda : self.seatSelection(times[3]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 440, y = 380)
        tk.Button(self, text=times[4], command=lambda : self.seatSelection(times[4]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 560, y = 380)
        tk.Button(self, text=times[5], command=lambda : self.seatSelection(times[5]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 680, y = 380)
        tk.Button(self, text=times[6], command=lambda : self.seatSelection(times[6]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 800, y = 380)
        tk.Button(self, text=times[7], command=lambda : self.seatSelection(times[7]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 80, y = 450)
        tk.Button(self, text=times[8], command=lambda : self.seatSelection(times[8]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 200, y = 450)
        tk.Button(self, text=times[9], command=lambda : self.seatSelection(times[9]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 320, y = 450)
        tk.Button(self, text=times[10], command=lambda : self.seatSelection(times[10]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 440, y = 450)
        tk.Button(self, text=times[11], command=lambda : self.seatSelection(times[11]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 560, y = 450)
        tk.Button(self, text=times[12], command=lambda : self.seatSelection(times[12]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 680, y = 450)
        tk.Button(self, text=times[13], command=lambda : self.seatSelection(times[13]),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 800, y = 450)

    # function defined for selecting seats
    def seatSelection(self,ti):
        global t
        t = t + ti

        # created a pop up window
        window1 = tk.Toplevel()
        window1.title("Select Seats")
        window1.geometry("1000x600")
        checkoutHeading = tk.Label(window1, text="SEATS SELECTION", font=("Arial", 50), fg="magenta")
        checkoutHeading.place(x = 180, y = 20)

        # created buttons for each seats
        tk.Button(window1, text = "01", bg='Green',command=lambda : self.selected("01"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 100, y = 180)
        tk.Button(window1, text = "02", bg='Green',command=lambda : self.selected("02"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 180, y = 180)
        tk.Button(window1, text = "03", bg='Green',command=lambda : self.selected("03"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 260, y = 180)
        tk.Button(window1, text = "04", bg='Green',command=lambda : self.selected("04"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 340, y = 180)
        tk.Button(window1, text = "05", bg='Green',command=lambda : self.selected("05"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 420, y = 180)
        tk.Button(window1, text = "06", bg='Green',command=lambda : self.selected("06"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 500, y = 180)
        tk.Button(window1, text = "07", bg='Green',command=lambda : self.selected("07"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 580, y = 180)
        tk.Button(window1, text = "08", bg='Green',command=lambda : self.selected("08"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 660, y = 180)
        tk.Button(window1, text = "09", bg='Green',command=lambda : self.selected("09"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 740, y = 180)
        tk.Button(window1, text = "10", bg='Green',command=lambda : self.selected("10"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 820, y = 180)

        tk.Button(window1, text = "11", bg='Green',command=lambda : self.selected("11"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 100, y = 260)
        tk.Button(window1, text = "12", bg='Green',command=lambda : self.selected("12"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 180, y = 260)
        tk.Button(window1, text = "13", bg='Green',command=lambda : self.selected("13"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 260, y = 260)
        tk.Button(window1, text = "14", bg='Green',command=lambda : self.selected("14"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 340, y = 260)
        tk.Button(window1, text = "15", bg='Green',command=lambda : self.selected("15"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 420, y = 260)
        tk.Button(window1, text = "16", bg='Green',command=lambda : self.selected("16"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 500, y = 260)
        tk.Button(window1, text = "17", bg='Green',command=lambda : self.selected("17"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 580, y = 260)
        tk.Button(window1, text = "18", bg='Green',command=lambda : self.selected("18"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 660, y = 260)
        tk.Button(window1, text = "19", bg='Green',command=lambda : self.selected("19"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 740, y = 260)
        tk.Button(window1, text = "20", bg='Green',command=lambda : self.selected("20"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 820, y = 260)

        tk.Button(window1, text = "21", bg='Green',command=lambda : self.selected("21"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 100, y = 340)
        tk.Button(window1, text = "22", bg='Green',command=lambda : self.selected("22"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 180, y = 340)
        tk.Button(window1, text = "23", bg='Green',command=lambda : self.selected("23"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 260, y = 340)
        tk.Button(window1, text = "24", bg='Green',command=lambda : self.selected("24"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 340, y = 340)
        tk.Button(window1, text = "25", bg='Green',command=lambda : self.selected("25"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 420, y = 340)
        tk.Button(window1, text = "26", bg='Green',command=lambda : self.selected("26"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 500, y = 340)
        tk.Button(window1, text = "27", bg='Green',command=lambda : self.selected("27"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 580, y = 340)
        tk.Button(window1, text = "28", bg='Green',command=lambda : self.selected("28"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 660, y = 340)
        tk.Button(window1, text = "29", bg='Green',command=lambda : self.selected("29"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 740, y = 340)
        tk.Button(window1, text = "30", bg='Green',command=lambda : self.selected("30"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 820, y = 340)

        tk.Button(window1, text = "31", bg='Green',command=lambda : self.selected("31"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 100, y = 420)
        tk.Button(window1, text = "32", bg='Green',command=lambda : self.selected("32"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 180, y = 420)
        tk.Button(window1, text = "33", bg='Green',command=lambda : self.selected("33"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 260, y = 420)
        tk.Button(window1, text = "34", bg='Green',command=lambda : self.selected("34"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 340, y = 420)
        tk.Button(window1, text = "35", bg='Green',command=lambda : self.selected("35"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 420, y = 420)
        tk.Button(window1, text = "36", bg='Green',command=lambda : self.selected("36"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 500, y = 420)
        tk.Button(window1, text = "37", bg='Green',command=lambda : self.selected("37"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 580, y = 420)
        tk.Button(window1, text = "38", bg='Green',command=lambda : self.selected("38"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 660, y = 420)
        tk.Button(window1, text = "39", bg='Green',command=lambda: self.selected("39"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 740, y = 420)
        tk.Button(window1, text = "40", bg='Green',command=lambda : self.selected("40"),font=("Arial", 20) ,fg = "yellow", borderwidth=3, relief="raised").place(x = 820, y = 420)

        tk.Button(window1, text = "BOOK SEAT", bg='light green',command=self.bookseat,font=("Arial", 20) ,fg = "blue", borderwidth=3, relief="raised").place(x = 400, y = 500)

    # function to check if seat is selected or not
    def selected(self, s1):
        global s
        s = s + s1
        s = s + " "

    # function defined to book the selected seat
    def bookseat(self):
        mbox.showinfo("Booked Seat", "For Time  :  " + t + "\n\nGenre  :  " + genre + "\n\nMovie  :  " + movie + "\n\nSeat " + s + " booked successfully.")


# main window created
window = Application()
window.geometry("1000x700")
window.title("Movie Booking Application")

# function for exiting window
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()