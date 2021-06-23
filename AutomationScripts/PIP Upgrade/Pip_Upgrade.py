import os
import tkinter as tk

root= tk.Tk()

''' Creating window '''
canvas1 = tk.Canvas(root, width = 300, height = 350, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

'''
Creating GUI for the button
'''
label1 = tk.Label(root, text='Upgrade PIP', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 80, window=label1)


'''Main function to upgrade the pip version'''
def upgradePIP ():
    os.system('start cmd /k python.exe -m pip install --upgrade pip') 
    
button1 = tk.Button(text='      Upgrade PIP     ', command=upgradePIP, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=button1)

root.mainloop()
