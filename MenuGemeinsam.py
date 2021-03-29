from tkinter import *
from Menu_Filme import *
from Menu_Benutzer import *
from Menu_Gemeinsam import *
from functools import partial
from Class_Benutzer import Benutzer

def anzeigen_benutzer(benutzer, frame):

    lista = Listbox(frame)
    i = 1
    for ben in benutzer:
        lista.insert(i, ben)
        i += 1
    lista.place(relx=0, rely=0.7)
    lista2 = Listbox(frame)
    i = 1
    for ben in benutzer:
        lista2.insert(i, ben.get_bestellungen())
        i += 1
    lista2.place(relx=0.2, rely=0.7)

def anzeigen_filme(filme, frame):

    lista = Listbox(frame,width=40)

    i = 1
    for film in filme:
        lista.insert(i, str(i)+" "+str(film)+" - "+str(film.get_preis())+" LEI")
        i += 1
    lista.place(relx=0.6, rely=0.7)


def gemeinsam(users, filme):

    g = Tk()
    g.geometry("800x800")
    g.title("MENU GEMEINSAM")

    f1 = Frame(g, bd=10, bg='red')
    f1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    button = Button(f1, text='Exit', width=20, command=g.destroy)
    button.place(relx=0, rely=0)

    l1 = Label(f1, text="Welchen Film mochten Sie kaufen?")
    l1.place(relx=0.4, rely=0.1)
    e1 = Entry(f1, width=5)
    e1.place(relx=0.75, rely=0.1)

    b1 = Button(f1, text="Bestellung-Option", width=20, command=partial(Menu_Gemeinsam.bestellung_option, filme, e1, f1))
    b1.place(relx=0, rely=0.1)

    e2 = Entry(f1, width=5)
    e2.place(relx=0.37, rely=0.5)
    b3 = Button(f1, text="Filme mit Wertung uber:", width=30, command=partial(Menu_Gemeinsam.suchen, filme, e2, f1))
    b3.place(relx=0, rely=0.5)

    e3 = Entry(f1, width=20)
    e3.place(relx=0.37, rely=0.3)
    b4 = Button(f1, text="Filme mit dem Schauspieler: ", width=30, command=partial(Menu_Gemeinsam.schauspieler, filme, e3, f1))
    b4.place(relx=0, rely=0.3)



    b2 = Button(f1, text="Anzeigen Benutzer+Bestellungen", width=34, command=partial(anzeigen_benutzer, users, f1))
    b2.place(relx=0, rely=0.65)

    b5 = Button(f1, text="Anzeigen Film-Liste", width=20, command=partial(anzeigen_filme, filme, f1))
    b5.place(relx=0.6, rely=0.65)

    g.mainloop()