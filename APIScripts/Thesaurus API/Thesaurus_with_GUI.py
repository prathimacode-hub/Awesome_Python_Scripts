# Access Merriam-Webster's Collegiate Thesaurus API with GUI

import requests
from tkinter import *
from tkinter import scrolledtext

def look_up(look_me_up):
    if look_me_up == '':
        return 'Entry is blank!'
    else:
        my_API_key = 'insert your API key here'
        endpoint = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/' + look_me_up + '?key=' + my_API_key
        response = requests.get(endpoint)

        status_code = response.status_code
        if status_code == 200:
            return_str = ''
            response_list = response.json()
            entry_num = 0
            for thes_entry_obj in response_list:
                entry_num += 1
                return_str = return_str + look_me_up + ': entry no. ' + str(entry_num) + '\n' + '\n'
                try:
                    return_str = return_str + 'Part of speech: ' + thes_entry_obj['fl'] + '\n' + '\n'
                except:
                    return_str = 'Word not found!'
                    break
                else:
                    return_str = return_str + 'Definition: ' + thes_entry_obj['shortdef'][0] + '\n' + '\n'

                    syn_list = thes_entry_obj['meta']['syns'][0]
                    if len(syn_list) > 0:
                        return_str = return_str + 'Synonyms: ' + '\n'
                        for syn in syn_list:
                            return_str = return_str + ' ' * 4 + syn + '\n'
                        return_str = return_str + '\n'

                    if 'rel_list' in thes_entry_obj['def'][0]['sseq'][0][0][1]:
                        related_list = thes_entry_obj['def'][0]['sseq'][0][0][1]['rel_list'][0]
                        if len(related_list) > 0:
                            return_str = return_str + 'Other related words: ' + '\n'
                            for rw in related_list:
                                return_str = return_str + ' ' * 4 + rw['wd'] + '\n'

                    return_str = return_str + '----------------------------------------' + '\n'
            return return_str
        else:
            return 'Request failed with status code: ' + str(status_code)

def search():
    look_me_up = entry.get()           # Get what the user eneterd into the box
    results = look_up(look_me_up)  # Do the lookup with the API and return results
    textw = scrolledtext.ScrolledText(main,width=70,height=30)
    textw.grid(column=1, row=2,sticky=W)
    textw.config(background="light grey", foreground="black",
                 font='times 18', wrap='word')
    textw.insert(END, results)

def quit():
    main.destroy()

main = Tk()
main.title("Merriam-Webster's Collegiate Thesaurus API")
main.geometry('900x750')
main.configure(background='ivory3')

entry = StringVar()

lblSearch = Label(main, text = 'Word to look up:').grid(row = 0, column = 0)
entSearch = Entry(main, textvariable = entry, width = 25).grid(row = 0,
                                                          column = 1, sticky=W)
btn = Button(main, text = 'Look it up!', bg='ivory2', width = 10,
             command = search).grid(row = 0, column = 10, sticky=E)
quit_btn = Button(main, text = 'Quit', bg='ivory2', width = 10, command = quit).grid(row = 3, column = 10, sticky=E)

main.bind('<Return>', lambda event=None: search())
main.mainloop()
