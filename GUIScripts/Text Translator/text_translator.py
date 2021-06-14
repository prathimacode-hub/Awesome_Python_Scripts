from googletrans import Translator
from tkinter import *
root = Tk(className='Python Translator')
root.geometry('600x600')
root.configure(bg='turquoise')

#variables

#option variable
optvar = StringVar()
text =StringVar()
OptionList = [
  'Choose Language of your choice', 
  'afrikaans',
  'amharic',
  'arabic',
  'azerbaijani',
  'belarusian',
  'bulgarian',
  'bengali',
  'bosnian',
  'czech',
  'welsh',
  'danish',
  'german',
  'greek',
  'english',
  'spanish',
  'persian',
  'finnish',
  'french',
  'gujarati',
  'hausa',
  'hawaiian',
  'hebrew',
  'hindi',
  'hungarian',
  'armenian',
  'indonesian',
  'italian',
  'hebrew',
  'japanese',
  'javanese',
  'georgian',
  'kannada',
  'korean',
  'latin',
  'malagasy',
  'maori',
  'macedonian',
  'malayalam',
  'mongolian',
  'marathi',
  'malay',
  'myanmar (burmese)',
  'nepali',
  'dutch',
  'norwegian',
  'odia',
  'punjabi',
  'polish',
  'pashto',
  'portuguese',
  'romanian',
  'russian',
  'sindhi',
  'sinhala',
  'albanian',
  'serbian',
  'sesotho',
  'sundanese',
  'swedish',
  'swahili',
  'tamil',
 'telugu',
  'tajik',
  'thai',
  'filipino',
  'turkish',
  'uyghur',
  'ukrainian',
  'urdu',
  'uzbek',
  'vietnamese',
  'xhosa',
  'yiddish',
  'yoruba',
  'chinese (simplified)',
  'chinese (traditional)',
  'zulu'

]
optvar.set(OptionList[0])

adlbl = Label(root, text='ENTER YOUR TEXT HERE', font=('Times New Roman', 15), fg='purple')
adlbl.grid(row=0, column=5, sticky='n')

#get text from user
entr = Entry(font=('Times New Roman', 23), fg='red', width=40, textvariable=text)
entr.grid(row=1, column=5, sticky='n', pady=13)

lbl1 = Label(root, text=f'Choose The Language  To Translate ?', font=('Times New Roman', 15), fg='gray10')
lbl1.grid(row=2, column=5, sticky='n')

#option list
opt = OptionMenu(root, optvar, *OptionList)
opt.grid(row=3, column=5, pady=7)

def trans():
    ttext = text.get()
    optval = optvar.get()
    translator = Translator()
    det = translator.detect(ttext)
    #display detected language
    detlbl = Label(root, text=f'Detected Language Is : {det.lang}', font=('Times New Roman', 15), fg='gray20')
    detlbl.grid(row=5, column=5, sticky='n')

    #translate language
    translated = translator.translate(ttext, dest=optval)
    print(translated)

    #display the translated text
    t = Text(root, height=20, width=70)
    t.grid(row=6, column=5, sticky='n')
    tr = translated.text
    t.insert(INSERT, tr)
    
#button
btn = Button(text='TRANSLATE', font=('Times New Roman', 20), fg='blue', command=trans)
btn.grid(row=4, column=5, sticky='n', pady=7)


root.mainloop()

