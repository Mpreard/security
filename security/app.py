from tkinter import *
from tkinter.filedialog import askopenfilename
import hashlib



def select(event):
    selection_hash = choice.selection_get()
    affichage_hash.configure(text=selection_hash)

def buttonFonction():
    filename.set(askopenfilename(filetypes=FILETYPES))

def hash(selection_hash):
    hash = selection_hash

def hashfile():
    if affichage_hash['text'] == 'SHA-1':
        with open(filename.get(),'rb') as file:
            blk = file.read()
            hash = hashlib.sha1(blk).hexdigest()
        file.close()
        print(hash)
    if affichage_hash['text'] == 'SHA-256':
        with open(filename.get(),'rb') as file:
            blk = file.read()
            hash = hashlib.sha256(blk).hexdigest()
        file.close()
        print(hash)
    if affichage_hash['text'] == 'SHA-512':
        with open(filename.get(),'rb') as file:
            blk = file.read()
            hash = hashlib.sha512(blk).hexdigest()
        file.close()
        print(hash)
    if affichage_hash['text'] == 'MD5':
        with open(filename.get(),'rb') as file:
            blk = file.read()
            hash = hashlib.md5(blk).hexdigest()
        file.close()
        print(hash)
    if affichage_hash['text'] == 'Blake2b':
        with open(filename.get(),'rb') as file:
            blk = file.read()
            hash = hashlib.blake2b(blk).hexdigest()
        file.close()
        print(hash)

FILETYPES = [("text files", "*.txt")]

# Création de la fenêtre
window = Tk()
window.title("e-Crypt")
window.geometry("700x530")
window.minsize(700, 530)
window.config(background='#656767')

# frame selection fichiers
frame_selection_fichier = Frame(
    window, relief='solid'
)
frame_selection_fichier.pack(side=RIGHT)
# Frame algo
frame_algo = Frame(
    window, bg="#656767", bd=2, relief='solid')
frame_algo.pack(side=LEFT)


# Ajouter un premier texte
label_type = Label(
    frame_algo, text="Algorithm", font=("Arial", 10), bg='#656767', fg='#ffffff')
label_type.pack()

# Choix du Hash
choice = Listbox(frame_algo, width=10, height=5)
choice.insert(1, "SHA-1")
choice.insert(2, "SHA-256")
choice.insert(3, "SHA-512")
choice.insert(4, "MD5")
choice.insert(5, "Blake2b")

choice.bind('<<ListboxSelect>>', select)

choice.pack()

affichage_hash = Label(frame_algo, text="")
affichage_hash.pack()

# bouton selection de fichier et affichage du chemin d'accès
bouton_fichier = Button(frame_selection_fichier,
                        text="Select Files", command=buttonFonction)
bouton_fichier.pack()

filename = StringVar(window)

entry = Entry(frame_selection_fichier, textvariable=filename, width=70)
entry.pack()

# bouton de cryptage
bouton_cryptage = Button(frame_selection_fichier, text="HASH", command=hashfile)
bouton_cryptage.pack()


# Afficher
window.mainloop()