from tkinter import *
from tkinter.filedialog import askopenfilename
import hashlib
import Crypto.Cipher

# Enregistre le choix de la méthode de Hash
def select(event):
    selection_hash = choice.selection_get()
    affichage_hash.configure(text=selection_hash)

# Action pour sélectionner le fichier
def buttonFonction():
    filename.set(askopenfilename(filetypes=FILETYPES))

# Selectionner le choix du Hash
def hash(selection_hash):
    hash = selection_hash

# Méthode de Hash
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

# Action du menu Générer des clés
def show_key():
    about_key = Toplevel(mb)
    about_key.title("Générer des clés")
    about_key.geometry("600x430")
    about_key.minsize(600, 430)

    # Titre
    titre_key= Label(about_key, text="Générer des clés", font=("Arial", 18), fg='#000000')
    titre_key.pack()

    # Frame clés
    frame_key = Frame(about_key, bg="#D6D6D6", bd=2, relief='solid')
    frame_key.pack(side=LEFT)

    # Ajouter un premier texte
    text_key = Label(frame_key, text="Taille des clés", font=("Arial", 10), bg='#D6D6D6', fg='#000000')
    text_key.pack()

    # Choix de la taille
    choice_key = Listbox(frame_key, width=10, height=5)
    choice_key.insert(1, "128 bits")
    choice_key.insert(2, "192 bits")
    choice_key.insert(3, "256 bits")

    choice_key.bind('<<ListboxSelect>>', select_key)
    choice_key.pack()
    result_key = Label(frame_key, text="")
    result_key.pack()

def select_key(event):
    selection_key = choice_key.selection_get()
    result_key.configure(text=selection_key)

# Action du menu Chiffrer un fichier
def show_chiff():
    about_chiff = Toplevel(mb)
    about_chiff.title("Chiffrer un fichier")
    about_chiff.geometry("600x430")
    about_chiff.minsize(600, 430)

    # Titre
    titre_type= Label(about_chiff, text="Chiffrer un fichier", font=("Arial", 18), fg='#000000')
    titre_type.pack()

# Type de fichiers
FILETYPES = [("text files", "*.txt")]

# Création de la fenêtre
window = Tk()
window.title("e-Crypt")
window.geometry("600x430")
window.minsize(600, 430)

# Widgets
mb = Menubutton(window,text="Menu")
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.config(background='#D6D6D6', fg='#000000')

mb.menu.add_command(label="Générer des clés", command=show_key)
mb.menu.add_command(label="Chiffrer un fichier", command=show_chiff)
mb.menu.add_separator()
mb.menu.add_command(label="Quitter", command=mb.quit)
mb.pack(side=TOP)

# Titre Fenêtre
titre_type= Label(window, text="Hasher un fichier", font=("Arial", 18), fg='#000000')
titre_type.pack(pady= 20)

# Frame selection fichiers
frame_selection_fichier = Frame(window, relief='solid')
frame_selection_fichier.pack(side=RIGHT, padx=110)

# Frame algo
frame_algo = Frame(window, bg="#D6D6D6", bd=2, relief='solid')
frame_algo.pack(side=LEFT)

# Ajouter un premier texte
label_type = Label(frame_algo, text="Methode", font=("Arial", 10), bg='#D6D6D6', fg='#000000')
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
bouton_fichier = Button(frame_selection_fichier,text="Sélectionnez un fichier", command=buttonFonction)
bouton_fichier.pack()

filename = StringVar(window)

entry = Entry(frame_selection_fichier, textvariable=filename, width=50)
entry.pack()

# bouton de cryptage
bouton_cryptage = Button(frame_selection_fichier, text="Hasher", command=hashfile)
bouton_cryptage.pack()

# Afficher
window.mainloop()