from tkinter import *
from Menu_Benutzer import *
from functools import partial


def anzeigen_users(users, frame):

    lista = Listbox(frame)
    i = 1
    for user in users:
        lista.insert(i, user)
        i += 1
    lista.place(relx=0.6, rely=0.7)


def benutzer(users):

    b = Tk()
    b.geometry("500x800")
    b.title("MENU BENUTZER")

    f3 = Frame(b, bd=10, bg='red')
    f3.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    button = Button(f3, text='Exit', width=20, command=b.destroy)
    button.place(relx=0, rely=0)


    l1 = Label(f3, text="Name:")
    l1.place(relx=0.4, rely=0.1)
    l2 = Label(f3, text="Vorname:")
    l2.place(relx=0.4, rely=0.15)
    l3 = Label(f3, text="Film:")
    l3.place(relx=0.4, rely=0.20)
    e1 = Entry(f3)
    e1.place(relx=0.6, rely=0.1)
    e2 = Entry(f3)
    e2.place(relx=0.6, rely=0.15)
    e3 = Entry(f3)
    e3.place(relx=0.6, rely=0.2)
    b1 = Button(f3, text="Einfugen", width=20,command=partial(Menu_Benutzer.einfugen, users, e1, e2, e3))
    b1.place(relx=0, rely=0.1)

    l4 = Label(f3, text="Nachname:")
    l4.place(relx=0.4, rely=0.3)
    l5 = Label(f3, text="Neuer Nachname:")
    l5.place(relx=0.4, rely=0.35)
    e4 = Entry(f3)
    e4.place(relx=0.68, rely=0.3)
    e5 = Entry(f3)
    e5.place(relx=0.68,rely=0.35)
    b2 = Button(f3, text="Aktualisieren", width=20, command=partial(Menu_Benutzer.aktualisieren, users, e4, e5))
    b2.place(relx=0, rely=0.3)

    l6 = Label(f3, text="Nachname User:")
    l6.place(relx=0.4, rely=0.5)
    e6 = Entry(f3)
    e6.place(relx=0.65, rely=0.5)
    b3 = Button(f3, text="Loschen", width=20, command=partial(Menu_Benutzer.loschen, users, e6))
    b3.place(relx=0, rely=0.5)

    anzeigen_benutzer = Button(f3, text="Anzeigen Benutzer", width=20, command=partial(anzeigen_users, users, f3))
    anzeigen_benutzer.place(relx=0, rely=0.7)

    b.mainloop()