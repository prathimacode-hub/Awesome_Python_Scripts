import tkinter 
import random
from tkinter import Label, messagebox

#assigining background colours
bg_grid_color = {
    2: "light blue",
    4: "light green",
    8: "yellow",
    16: "orange",
    32: "red",
    64: "magenta",
    128: "blue",
    256: "green",
    512: "#00FFFF",
    1024: "#856ff8",
    2048: "pink"
    }
#assigning colours for the number
number_colour ={
    2: "red",
    4: "blue",
    8: "#856ff8",
    16: "black",
    32: "yellow",
    64: "green",
    128: "light green",
    256: "light blue",
    512: "red",
    1024: "#00FFFF",
    2048: "magenta"
}

class Game(tkinter.Frame):
    #creating the framework
    def __init__(self):
        tkinter.Frame.__init__(self)
        self.grid()
        self.master.title('2048')

        self.mainGrid = tkinter.Frame(
            self, bg="grey", bd=3, width=400, height=400)
        self.mainGrid.grid(pady=(100, 0))
        self.make_grid()
        self.begin_game()
        #commands to be followed when corresponding keys r pressed
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()


    #creating the grids
    def make_grid(self):
        self.cells = []
        #making a 4 X 4 grid
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tkinter.Frame(
                    self.mainGrid,
                    bg="azure4",
                    width=100,
                    height=100)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tkinter.Label(self.mainGrid, bg="azure4")
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "value": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        # Displaying the score
        score_frame = tkinter.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tkinter.Label(
            score_frame,
            text="Score"
            ).grid(
            row=0)
        self.score_label = tkinter.Label(score_frame, text="0")
        self.score_label.grid(row=1)


    def begin_game(self):
        
        self.matrix = [[0] * 4 for i in range(4)]

        # rondomly placing 2 2's in 2 grids
        row = random.randint(0, 3)
        column = random.randint(0, 3)
        #changing their bg colour and displaying the value
        self.matrix[row][column] = 2
        self.cells[row][column]["frame"].configure(bg=bg_grid_color[2])
        self.cells[row][column]["value"].configure(
            bg=bg_grid_color[2],
            fg=number_colour[2],
            text="2")
        while(self.matrix[row][column] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        #changing their bg colour and displaying the value
        self.matrix[row][column] = 2
        self.cells[row][column]["frame"].configure(bg=bg_grid_color[2])
        self.cells[row][column]["value"].configure(
            bg=bg_grid_color[2],
            fg=number_colour[2],
            text="2")

        self.score = 0


   

    def stack(self):
    #finding out all grids which are empty
        filled_box_matrix = [[0] * 4 for i in range(4)]
        for i in range(4):
            pos = 0
            for j in range(4):
                if (self.matrix[i][j] != 0):
                    filled_box_matrix[i][pos] = self.matrix[i][j]
                    pos += 1
        self.matrix = filled_box_matrix


    def combine(self):
        #combining values in 2 grids if they have the same value
        for i in range(4):
            for j in range(3):
                if (self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]):
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]


    #to reverse the order of each row   
    def reverse(self):
        newMat = []
        for i in range(4):
            newMat.append([])
            for j in range(4):
                newMat[i].append(self.matrix[i][3 - j])
        self.matrix = newMat


    #To flip the matrix over diagonal
    def transpose(self):
        tempMat = [[0] * 4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                tempMat[i][j] = self.matrix[j][i]
        self.matrix = tempMat


    # Add a new 2 or 4 tile randomly to an empty cell

    def new_tile(self):
        row = random.randint(0, 3)
        column = random.randint(0, 3)
        while(self.matrix[row][column] != 0):
            row = random.randint(0, 3)
            column = random.randint(0, 3)
        self.matrix[row][column] = random.choice([2, 4])


   #updating the matrix
    def updation(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if (cell_value == 0):
                    self.cells[i][j]["frame"].configure(bg="azure4")
                    self.cells[i][j]["value"].configure(bg="azure4",text=" ")
                else:
                    self.cells[i][j]["frame"].configure(bg=bg_grid_color[cell_value])
                    self.cells[i][j]["value"].configure(
                        bg=bg_grid_color[cell_value],
                        fg=number_colour[cell_value],
                        text=str(cell_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks()


    

    #when you press left
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.new_tile()
        self.updation()
        self.check_end()


    #when you press right
    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.new_tile()
        self.updation()
        self.check_end()


    #when you press up
    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.new_tile()
        self.updation()
        self.check_end()


    #when you press down
    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.new_tile()
        self.updation()
        self.check_end()


    

     #To check if any moves r left
    def hori_possible(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False


    def verti_possible(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False


    

    #checking if game over
    def check_end(self):
        if any(2048 in row for row in self.matrix):
             messagebox.showinfo("YOU WIN","your score is {}".format(self.score))
        elif not any(0 in row for row in self.matrix) and not self.hori_possible() and not self.verti_possible():
            messagebox.showinfo("YOU LOOSE","your final score is {}".format(self.score))
           


Game()


