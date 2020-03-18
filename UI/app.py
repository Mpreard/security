from tkinter import *
from tkinter.filedialog import askopenfilename


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
choice.insert(1, "MDA")
choice.insert(2, "SHA-1")
choice.insert(3, "SHA256")
choice.insert(4, "SHA512")
choice.insert(5, "xxxHash64")

choice.bind('<<ListboxSelect>>', select)

choice.pack()

affichage_hash = Label(frame_algo, text="")
affichage_hash.pack()

# bouton selection de fichie et affichage du chemin d'accès
bouton_fichier = Button(frame_selection_fichier,
                        text="Select Files", command=buttonFonction)
bouton_fichier.pack()

filename = StringVar(window)

entry = Entry(frame_selection_fichier, textvariable=filename, width=70)
entry.pack()

# bouton de cryptage
bouton_cryptage = Button(frame_selection_fichier, text="HASH")
bouton_cryptage.pack()

# Afficher
window.mainloop()
