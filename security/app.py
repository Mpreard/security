from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import hashlib
from cryptography.fernet import Fernet
import json

# Enregistre le choix de la méthode de Hash
def select(event):
    selection_hash = choice.selection_get()
    affichage_hash.configure(text=selection_hash)

# Enregistre le choix du sel ou non
def sel():
    selection = str(var.get())
    affichage_sel.config(text=selection)

# Action pour sélectionner le fichier
def buttonFonction():
    filename.set(askopenfilename(filetypes=FILETYPES))

# Méthode de Hash
def hashfile():
    check_sel = ""
    if affichage_sel['text'] == "Sans sel": # Sans Salage
        if affichage_hash['text'] == 'SHA-1':
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.sha1(blk).hexdigest()
            file.close()
            mas.set(hash)
        if affichage_hash['text'] == 'SHA-256':
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.sha256(blk).hexdigest()
            file.close()
            mas.set(hash)
        if affichage_hash['text'] == 'SHA-512':
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.sha512(blk).hexdigest()
            file.close()
            mas.set(hash)
        if affichage_hash['text'] == 'MD5':
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.md5(blk).hexdigest()
            file.close()
            mas.set(hash)
        if affichage_hash['text'] == 'Blake2B':
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.blake2b(blk).hexdigest()
            file.close()
            mas.set(hash)
    if check_sel != entry_sel.get(): # Avec Salage
        if affichage_hash['text'] == 'SHA-1':
            with open(filename.get(), 'a') as file:
                sel = entry_sel.get()
                file.write(sel)
            file.close()
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.sha1(blk).hexdigest()
            file.close()
            mas.set(hash)
        if affichage_hash['text'] == 'SHA-256':
            with open(filename.get(), 'a') as file:
                sel = entry_sel.get()
                file.write(sel)
            file.close()
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.sha256(blk).hexdigest()
            file.close()
            mas.set(hash)
        if affichage_hash['text'] == 'SHA-512':
            with open(filename.get(), 'a') as file:
                sel = entry_sel.get()
                file.write(sel)
            file.close()
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.sha512(blk).hexdigest()
            file.close()
            mas.set(hash)
        if affichage_hash['text'] == 'MD5':
            with open(filename.get(), 'a') as file:
                sel = entry_sel.get()
                file.write(sel)
            file.close()
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.md5(blk).hexdigest()
            file.close()
            mas.set(hash)
        if affichage_hash['text'] == 'Blake2B':
            with open(filename.get(), 'a') as file:
                sel = entry_sel.get()
                file.write(sel)
            file.close()
            with open(filename.get(), 'rb') as file:
                blk = file.read()
                hash = hashlib.blake2b(blk).hexdigest()
            file.close()
            mas.set(hash)

# Action du menu Générer des clés
def show_key():
    about_key = Toplevel(mb)
    about_key.title("Générer des clés")
    about_key.geometry("1200x400")
    about_key.minsize(1200, 400)

    # Enregistre le choix de la taille de la clé AES
    def select_key(event):
        selection_key = choice_key.selection_get()
        result_key.configure(text=selection_key)

    # Action pour generer la clé
    def genera_key():
        if result_key['text'] == '128 bits':
            with open('table_key.json', 'a') as file:
                key = Fernet.generate_key()
                nbr_key = key.decode()
                global pseudo
                global password
                pseudo = pseudo_entry.get()
                password = password_entry.get()
                x = {'Pseudo': pseudo, 'Password': password,'Key': nbr_key}
                y = json.dumps(x, indent=1)
                file.write(y)
                table.insert('',END,values=(pseudo, nbr_key))
                file.close()
        if result_key['text'] == '192 bits':
            with open('table_key.json', 'a') as file:
                key = Fernet.generate_key()
                nbr_key = key.decode()
                pseudo = pseudo_entry.get()
                password = password_entry.get()
                x = {'Pseudo': pseudo, 'Password': password,'Key': nbr_key}
                y = json.dumps(x, indent=1)
                file.write(y)
                table.insert('',END,values=(pseudo, nbr_key))
                file.close()
        if result_key['text'] == '256 bits':
            with open('table_key.json', 'a') as file:
                key = Fernet.generate_key()
                nbr_key = key.decode()
                pseudo = pseudo_entry.get()
                password = password_entry.get()
                x = {'Pseudo': pseudo, 'Password': password,'Key': nbr_key}
                y = json.dumps(x, indent=1)
                file.write(y)
                table.insert('',END,values=(pseudo, nbr_key))
                file.close()

    # Action pour supprimer une clé
    def delete_key():
        select_table = table.selection()
        for selected_item in select_table:
            table.delete(selected_item)
            with open('table_key.json', 'w') as file:
                data_delete = json.load(file)
                board = (data['Pseudo'], data['Key'])
                boards = (data['Pseudo'], data['Password'], data['Key'])
                if selected_item == board:
                    file.pop(boards)
                file.close()
        

    # Titre "Générer des clés"
    titre_key = Label(about_key, text="Générer des clés",font=("Arial", 18), fg='#000000')
    titre_key.pack()

    # Frame des clés
    frame_key = Frame(about_key, bg="#D6D6D6", bd=2, relief='solid')
    frame_key.pack(side=LEFT)

    # Texte "Taille des clés AES" de la listebox
    text_key = Label(frame_key, text="Taille des clés AES",font=("Arial", 10), bg='#D6D6D6', fg='#000000')
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

    # Frame Pseudo + mot de passe
    frame_genera = Frame(about_key, relief='solid')
    frame_genera.pack(side=LEFT, padx=110)

    pseudo_text = Label(frame_genera, text="Votre pseudo")
    pseudo_text.pack()
    pseudo_entry = Entry(frame_genera, textvariable="", width=20)
    pseudo_entry.pack()

    password_text = Label(frame_genera, text="Votre mot de passe")
    password_text.pack()
    password_entry = Entry(frame_genera, textvariable="", width=20)
    password_entry.pack()

    # Bouton générer la clé
    bouton_key = Button(about_key, text="Générer", width=10,height=3, font=("Arial", 10), command=genera_key)
    bouton_key.pack(pady=150, side=LEFT)

    # Tableau affiche les clés au lancement
    frame_table = Frame(about_key, relief='solid')
    frame_table.pack()
    table=ttk.Treeview(about_key, show="headings")
    table["columns"]=(1, 2)
    table.column("#0", width=0)
    table.column(1, width=150, minwidth=150)
    table.column(2, width=350, minwidth=350)
    table.heading(1, text="Pseudo",anchor=W)
    table.heading(2, text="Key",anchor=W)
    selected_item = table.selection()
    table.pack()
    with open('table_key.json') as f:
        data = json.load(f)
        table.insert('',END,values=(data['Pseudo'],data['Key']))
    f.close()

    # Bouton Supprimer
    supprime_key = Button(about_key, text="Supprimer", width=10,height=3, font=("Arial", 10), command=delete_key)
    supprime_key.pack(side=TOP)

    # Frame Texte NOM et PRENOM
    frame_nom = Frame(about_key)
    frame_nom.pack()
    Name_label = Label(frame_nom, text="Valentin Morin & Maxime Préard", font=("Arial", 7))
    Name_label.pack()

# Action du menu Chiffrer un fichier
def show_chiff():
    about_chiff = Toplevel(mb)
    about_chiff.title("Chiffrer un fichier")
    about_chiff.geometry("600x600")
    about_chiff.minsize(600, 600)

    def buttonFonction2():
        filename2.set(askopenfilename(filetypes=FILETYPES))

    # Titre "Chiffrer / Déchiffrer un fichier"
    titre_type = Label(about_chiff, text="Chiffrer / Déchiffrer un fichier", font=("Arial", 18), fg='#000000')
    titre_type.pack()

    # Tableau pour afficher les clés
    frame_table = Frame(about_chiff, relief='solid')
    frame_table.pack()
    demande_type = Label(about_chiff, text="Sélectionnez votre clé", font=("Arial", 10), fg='#000000')
    demande_type.pack(pady=20)
    table=ttk.Treeview(about_chiff, show="headings")
    table["columns"]=(1, 2)
    table.column("#0", width=0)
    table.column(1, width=150, minwidth=150)
    table.column(2, width=350, minwidth=350)
    table.heading(1, text="Pseudo",anchor=W)
    table.heading(2, text="Key",anchor=W)
    selected_item = table.selection()
    table.pack()
    with open('table_key.json') as f:
        data = json.load(f)
        table.insert('',END,values=(data['Pseudo'],data['Key']))
    f.close()

    # Bouton de chiffrement
    def btn_chiffr():
        with open('table_key.json', 'r') as f:
            data = json.load(f)
            verif = (data['Password'])
            entry_verif = password_entry.get()
            if entry_verif == verif:
                select_table = table.selection()
                for selected_item in select_table:
                    select_key = selected_item('Key')
                    final_key = select_key.encode()
                    with open(filename2.get(), 'rb') as file:
                        token = final_key.encrypt(file)
                    file.close()
        f.close()

    # Bouton de déchiffrement
    def btn_dechiffr():
        with open('table_key.json', 'r') as f:
            data = json.load(f)
            verif = (data['Password'])
            entry_verif = password_entry.get()
            if entry_verif == verif:
                select_table = table.selection()
                for selected_item in select_table:
                    select_key = selected_item('Key')
                    final_key = select_key.encode()
                    with open(filename2.get(), 'rb') as file:
                        token = final_key.decrypt(file)
                    file.close()
        f.close()


    # Frame sélectionner un fichier chiffrement
    frame_select_fic = Frame(about_chiff, relief='solid')
    frame_select_fic.pack(side=BOTTOM, ipady=20)
    bouton_fichier = Button(frame_select_fic, text="Sélectionnez un fichier", command=buttonFonction2)
    bouton_fichier.pack()

    filename2 = StringVar(window)

    entry2 = Entry(frame_select_fic, textvariable=filename2, width=100)
    entry2.pack()

    # Frame + Bouton chiffrement / déchiffrement
    frame_chiff = Frame(about_chiff, relief='solid')
    frame_chiff.pack()
    button_chiffrer = Button(frame_chiff, text="Chiffrer", width=10,height=2, font=("Arial", 10), command=btn_chiffr)
    button_chiffrer.pack(side=LEFT)

    button_dechiffrer = Button(frame_chiff, text="Déchiffrer", width=10,height=2, font=("Arial", 10), command= btn_dechiffr)
    button_dechiffrer.pack(side=RIGHT)

    # Mot de passe
    frame_pass = Frame(about_chiff, relief='solid')
    frame_pass.pack(pady=50)
    password_text = Label(frame_pass, text="Mot de passe")
    password_text.pack()
    password_entry = Entry(frame_pass, textvariable="", width=20)
    password_entry.pack()

    # Frame Texte NOM et PRENOM
    frame_nom = Frame(frame_pass)
    frame_nom.pack()
    Name_label = Label(frame_nom, text="Valentin Morin & Maxime Préard", font=("Arial", 7))
    Name_label.pack()

# Type de fichiers
FILETYPES = [("text files", "*.txt")]

# Création de la fenêtre
window = Tk()
window.title("e-Crypt")
window.geometry("1200x630")
window.minsize(1200, 630)

# Widgets Menu de l'interface
mb = Menubutton(window, text="Menu")
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.config(background='#D6D6D6', fg='#000000')

mb.menu.add_command(label="Générer des clés", command=show_key)
mb.menu.add_command(label="Chiffrer un fichier", command=show_chiff)
mb.menu.add_separator()
mb.menu.add_command(label="Quitter", command=mb.quit)
mb.pack(side=TOP)

# Titre Fenêtre
titre_type = Label(window, text="Hasher un fichier", font=("Arial", 18), fg='#000000')
titre_type.pack(pady=20)

# Frame selection fichiers
frame_selection_fichier = Frame(window, relief='solid')
frame_selection_fichier.pack(side=RIGHT, padx=110)

# Frame méthode
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
choice.insert(5, "Blake2B")

choice.bind('<<ListboxSelect>>', select)

choice.pack()

affichage_hash = Label(frame_algo, text="")
affichage_hash.pack()

# Bouton selection de fichier et affichage du chemin d'accès
bouton_fichier = Button(frame_selection_fichier, text="Sélectionnez un fichier", command=buttonFonction)
bouton_fichier.pack()

filename = StringVar(window)

entry = Entry(frame_selection_fichier, textvariable=filename, width=100)
entry.pack()

# Insérer le sel
label_sel = Label(frame_selection_fichier, text="Entrez votre sel (optionnel)")
entry_sel = Entry(frame_selection_fichier)
label_sel.pack()
entry_sel.pack()

# Bouton de hashage
bouton_hash = Button(frame_selection_fichier, text="Hasher", command=hashfile)
bouton_hash.pack()

# Instancier le résultat du Hash
mas = StringVar()
text_hash = Entry(frame_selection_fichier, textvariable=mas, width=150, font=("Arial", 8), fg='#000000')
text_hash.pack()

# Radio button sel
var = StringVar()
R1 = Radiobutton(frame_algo, text="Avec sel", variable=var, value="Avec sel", command=sel,  bg='#D6D6D6')
R1.pack()
R2 = Radiobutton(frame_algo, text="Sans sel", variable=var, value="Sans sel", command=sel,  bg='#D6D6D6')
R2.pack()

affichage_sel = Label(frame_algo, text="")
affichage_sel.pack()

# Frame Texte NOM et PRENOM
frame_nom = Frame(frame_selection_fichier)
frame_nom.pack()
Name_label = Label(frame_nom, text="Valentin Morin & Maxime Préard", font=("Arial", 7))
Name_label.pack()

# Afficher la fenêtre principale
window.mainloop()