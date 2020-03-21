from tkinter import *
from tkinter.filedialog import askopenfilename
import hashlib


def select(event):
    selection_hash = choice.selection_get()
    affichage_hash.configure(text=selection_hash)


def buttonFonction():
    filename.set(askopenfilename(filetypes=FILETYPES))


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
bouton_cryptage = Button(frame_selection_fichier, text="HASH")
bouton_cryptage.pack()


# Création du HASH en SHA-1
SHA1 = hashlib.sha1() 

# Création du HASH en SHA-256
SHA256 = hashlib.sha256()

# Création du HASH en SHA-512
SHA512 = hashlib.sha512()

# Création du HASH en MD5
MD5 = hashlib.md5()

# Création du HASH en Blake2b
BLAKE = hashlib.blake2b()

def hashfile(bouton_cryptage):
    if select == "SHA1":
        with open(filename,'rb') as file:
            blk = file.read()    
            SHA1.update(blk)
        file.close()
        message_hache = SHA1.hexdigest()
        print(message_hache)
    if select == "SHA-256":
        with open(filename,'rb') as file:
            blk = file.read()    
            SHA256.update(blk)
        file.close()
        message_hache = SHA256.hexdigest()
        print(message_hache)
    if select == "SHA-512":
        with open(filename,'rb') as file:
            blk = file.read()    
            SHA512.update(blk)
        file.close()
        message_hache = SHA512.hexdigest()
        print(message_hache)
    if select == "MD5":
        with open(filename,'rb') as file:
            blk = file.read()    
            MD5.update(blk)
        file.close()
        message_hache = MD5.hexdigest()
        print(message_hache)
    if select == "Blake2b":
        with open(filename,'rb') as file:
            blk = file.read()    
            BLAKE.update(blk)
        file.close()
        message_hache = BLAKE.hexdigest()
        print(message_hache)

# Afficher
window.mainloop()