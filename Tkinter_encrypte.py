import tkinter
from tkinter import messagebox
import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
# UI

window = tkinter.Tk()
window.title("secret notes")
window.minsize(width=400, height=800)

#Image
'''
photos = tkinter.PhotoImage(file= "add.png")
photo_label = tkinter.Label(image= photos)
photo_label.pack()
'''

#Enter your title

label = tkinter.Label(text="Enter Your Title")
label.pack()

#entry

entry = tkinter.Entry(width=50)
entry.pack()

#Enter your secret

label1 = tkinter.Label(text="Enter Your Secret")
label1.pack()
#text

text = tkinter.Text(width=50, height=20)
text.pack()

#Enter master key

label2 = tkinter.Label(text="Enter Master Key")
label2.pack()

#entry1

entry1 = tkinter.Entry(width=50)
entry1.pack()

#fonksiyon

def create():
    folder = entry.get()
    docs = text.get("1.0",tkinter.END)
    key = entry1.get()

    if len(folder) == 0 or len(docs) == 0 or len(key) ==0:
        messagebox.showinfo("Eksik Bilgi", "Gerekli Yerleri Doldurunuz")

    docs_encrypted = encode(key ,docs)
        



    f = open(f"{folder}.txt", "a")
    f.write(f"\n{folder} \n{docs_encrypted}")
    f.close()

    #open and read the file after the overwriting:
    f = open(f"{folder}.txt", "r")
    print(f.read())

def read():
    folder = entry.get()
    docs = text.get("1.0",tkinter.END)
    key = entry1.get()

    docs_decode = decode(key, docs)

    f = open(f"{folder}.txt", "r")
    f.write(f"\n{folder} \n{docs_encrypted}")
    f.close()




#button Save and Encrypte

button = tkinter.Button(text="Save and Encrypte")
button.config(command=create)
button.pack()


#button Descrypt

button1 = tkinter.Button(text="Descrypt")
button1.config(command=read)
button1.pack()



















window.mainloop()