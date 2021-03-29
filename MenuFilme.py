from tkinter import *
from Menu_Filme import *
from functools import partial


def anzeigen_filme(filme, frame):

    lista = Listbox(frame)
    i = 1
    for film in filme:
        lista.insert(i, film)
        i += 1
    lista.place(relx=0.6, rely=0.5)


def films(filme):

    film = Tk()
    film.geometry("500x800")
    film.title("MENU FILME")

    f2 = Frame(film, bd=10, bg='red')
    f2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    button = Button(f2, text='Exit', width=20, command=film.destroy)
    button.place(relx=0, rely=0)

    l1 = Label(f2, text="Titel:")
    l1.place(relx=0.4, rely=0.05)
    e1 = Entry(f2)
    e1.place(relx=0.6, rely=0.05)
    l2 = Label(f2, text="Jahr:")
    l2.place(relx=0.4, rely=0.1)
    e2 = Entry(f2)
    e2.place(relx=0.6, rely=0.1)
    l3 = Label(f2, text="Wertung:")
    l3.place(relx=0.4, rely=.15)
    e3 = Entry(f2)
    e3.place(relx=0.6, rely=0.15)
    l4 = Label(f2, text="Preis:")
    l4.place(relx=0.4, rely=.2)
    e4 = Entry(f2)
    e4.place(relx=0.6, rely=0.2)
    l5 = Label(f2, text="Actor:")
    l5.place(relx=.4,rely=0.25)
    e5 = Entry(f2)
    e5.place(relx=.6, rely=0.25)
    b1 = Button(f2, text="Einfugen", width=20, command=partial(Menu_Filme.einfugen, filme, e1, e2, e3, e4, e5))
    b1.place(relx=0, rely=0.1)

    l6 = Label(f2, text="Titel:")
    l6.place(relx=.4, rely=.3)
    e6 = Entry(f2)
    e6.place(relx=.6, rely=.3)
    l7 = Label(f2, text="Neuer Preis:")
    l7.place(relx=0.4, rely=.35)
    e7 = Entry(f2)
    e7.place(relx=0.6, rely=0.35)
    b2 = Button(f2, text="Preis-Aktualisieren", width=20, command=partial(Menu_Filme.aktualisieren, filme, e6, e7))
    b2.place(relx=0, rely=0.3)

    anzeigen_movies = Button(f2, text="Anzeigen aller Filmen", width=30, command=partial(anzeigen_filme, filme, f2))
    anzeigen_movies.place(relx=0, rely=0.5)

    film.mainloop()