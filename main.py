# noinspection SpellCheckingInspection,PyShadowingBuiltins,PyPep8Naming,PyShadowingNames,PyUnresolvedReferences
from tkinter import *
from functools import partial
from MenuBenutzer import *
from MenuFilme import *
from MenuGemeinsam import *
from init_fisiere import *


m = Tk()                            #  MAIN WINDOW
m.geometry("500x500")
m.title('MAIN WINDOW')


users = []                          # LISTA USERI
filme = []                          # LISTA FILME
Main.anfangsliste_benutzer(users)   # initializare lista useri
Main.anfangsliste_filmen(filme)     # initializare lista filme



f = Frame(m, bd=20, bg='red')
f.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)
button = Button(f, text='Exit', width=30, command=m.destroy)
button.pack()


txt = ' MENIU PRINCIPAL'
meniuprincipal = Label(m, font=50, text=txt)
meniuprincipal.pack()

txt2= 'SELECTATI OPTIUNEA: '
optiunea = Label(m, font=20, text=txt2)
optiunea.place(relheight=0.2)


menu_benutzer = Button(f, text="Menu Benutzer", width=30, command=partial(benutzer, users))
menu_benutzer.pack()
menu_filme = Button(f, text="Menu Filme", width=30, command=partial(films, filme))
menu_filme.pack()
menu_gemeinsam = Button(f, text="Menu Gemeinsam", width=30, command=partial(gemeinsam, users, filme))
menu_gemeinsam.pack()


menu = Menu(m)                              # HELP & QUIT FILE-MENU
m.config(menu=menu)
menu.add_cascade(label='Exit', command=m.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')


m.mainloop()
