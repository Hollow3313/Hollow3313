import requests
import tkinter
import wget
from tkinter import PhotoImage
import os

# Tkinter
window = tkinter.Tk()
window.title("Pokemon")
window.minsize(width=400, height=500)

# Label
label = tkinter.Label(text="Enter Pokemon Name")
label.pack()

# Entry
entry = tkinter.Entry()
entry.pack()

def entry_input():
    user_input = entry.get()
    
    def get_pokemon_data(pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_pokemon_gif(pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon-form/{pokemon_name.lower()}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            sprite_url = data["sprites"]["front_default"]


            try:
                os.remove("pokemon.gif")
            except FileNotFoundError:
                pass
            
            wget.download(sprite_url, 'pokemon.gif')
       

            photo = PhotoImage(file='pokemon.gif')
            photo_label.config(image=photo)
            photo_label.image = photo
            photo_label.pack()
        else:
            return None
        
    pokemon_data = get_pokemon_data(user_input)

    if pokemon_data:
        pokemon_name = pokemon_data["name"]
        print("Pokémon Adı:", pokemon_name)
        
        gif_url = get_pokemon_gif(user_input)
        
        if gif_url:
            print("Pokémon Gif URL:", gif_url)
        else:
            print("Pokémon Gifi bulunamadı.")
    else:
        print("Pokémon bulunamadı veya API isteği başarısız oldu.")

# Label for displaying the Pokemon image
label2 = tkinter.Label(text="Your Pokemon")
label2.pack()

photo_label = tkinter.Label()
photo_label.pack()

# Button
button = tkinter.Button(text="Show", command=entry_input)
button.pack()

window.mainloop()
