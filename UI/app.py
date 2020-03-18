from tkinter import *
from tkinter.filedialog import askopenfilename


def select(event):
    selection_hash = choice.selection_get()
    affichage_hash.configure(text=selection_hash)


def buttonFonction():
    askopenfilename()


# Création de la fenêtre
window = Tk()
window.title("e-Crypt")
window.geometry("700x530")
window.minsize(700, 530)
window.config(background='#656767')

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

# bouton selection de fichier
bouton_fichier = Button(window, text="Select Files", command=buttonFonction)
bouton_fichier.pack()

# Afficher
window.mainloop()
