from tkinter import *

# Création de la fenêtre
window = Tk()
window.title("e-Crypt")
window.geometry("700x530")
window.minsize(700, 530)
window.iconbitmap("icon.ico")
window.config(background='#656767')

# Frame algo
frame_algo = Frame(window, bg="#656767", bd=2, relief='solid')
frame_algo.pack(side=LEFT)
# Ajouter un premier texte
label_title = Label(
    frame_algo, text="Algorithm", font=("Arial", 10), bg='#656767', fg='#ffffff')
label_title.pack()


# Afficher
window.mainloop()
