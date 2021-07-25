import pypokedex
import PIL.Image,PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

#building the gui
window=tk.Tk()
window.geometry("600x500")
window.title("Pokedex- A big pokemon fan")
window.config(padx=10, pady=10)

pokemon_image=tk.Label(window)
pokemon_image.pack(padx=10, pady=10)
#setting the title
title_label=tk.Label(window,text="Pokedex")
title_label.config(font=("Arial",28))
title_label.pack(padx=10,pady =10)

pokemon_information=tk.Label(window)
pokemon_information.config(font=("Arial",20))
pokemon_information.pack(padx=10,pady =10)

pokemon_types=tk.Label(window)
pokemon_types.config(font=("Arial",20))
pokemon_types.pack(padx=10,pady =10)



#function to load image and information of pokemon
def load_pokemon():
    #matching id and name
    pokemon=pypokedex.get(name=text_id_name.get(1.0,"end-1c"))
    http = urllib3.PoolManager()
    #getting the image
    response= http.request('GET',pokemon.sprites.front.get('default'))
    image=PIL.Image.open(BytesIO(response.data))
     #saving the image on GUI
    img=PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image=img
     #saving the type /characteristic of character
    pokemon_information.config(text=f"{ pokemon.dex}- {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())

#applying the proper location
label_id_name=tk.Label(window,text="ID Or Name")
label_id_name.config(font=("Arial",20))
label_id_name.pack(padx=10,pady =10)

text_id_name=tk.Text(window,height=1)
text_id_name.config(font=("Arial",20))
text_id_name.pack(padx=10,pady =10)


btn_load=tk.Button(window, text="Load Pokemon",command=load_pokemon)
btn_load.config(font=("Arial",20))
btn_load.pack(padx=10,pady =10)

window.mainloop()