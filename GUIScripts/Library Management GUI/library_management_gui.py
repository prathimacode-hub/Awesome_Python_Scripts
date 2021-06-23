
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


#defining the grid
class LibraryGrid(GridLayout):
    def __init__(self,**kwargs):
        super(LibraryGrid,self).__init__()
        self.cols =4


        self.add_widget(Label(text="Student Name: "))
        self.a_name=TextInput()
        self.add_widget(self.a_name)

        self.add_widget(Label(text=" Name of the book : "))
        self.a_book=TextInput()
        self.add_widget(self.a_book)

        self.add_widget(Label(text="Issue Date: "))
        self.a_issue=TextInput()
        self.add_widget(self.a_issue)

        self.add_widget(Label(text="Return date "))
        self.a_return=TextInput()
        self.add_widget(self.a_return)

        self.add_widget(Label(text="fine"))
        self.a_fine=TextInput()
        self.add_widget(self.a_fine)


        self.press = Button(text="Click here to print inforation")
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)


   # assigning the button their function
    def click_me(self,instance):
        print("Name of the student: " +self.a_name.text)
        print("Name of the book:" + self.a_book.text)
        print("Issue Date:" + self.a_issue.text)
        print("Return Date :" + self.a_return.text)
        print("Fine amount" + self.a_fine.text)


#calling the function
class LibraryApp(App):
    def build(self):
        return LibraryGrid()
if __name__== '__main__':
    LibraryApp().run()