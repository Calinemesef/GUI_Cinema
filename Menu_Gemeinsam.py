from tkinter import *


class Menu_Gemeinsam:

    """
    MENU-Gemeinsam
    - keine Attribute
    - enthalt folgende Methoden: Bestellung-Option, Anzeigen, Suchen, Schauspieler
    + zusammenfassungs-menu
    """

    @staticmethod
    def bestellung_option(filme, entry1, f1):

        """
        Methode fur Bestellen der Filmen
        """
        try:
            #print("Bestellung-Option")
            nr = 1
            #print("Liste von Filmen und ihren Preis ")
            #for i in range(0, len(filme)):
            #    print(nr)
            #    nr += 1
            #    print(filme[i].get_titel() + ' ' + filme[i].get_preis() + " LEI")

            preis = 0
            #print("Wahlen Sie sich die Filme an, indem Sie die entsprechende Zahl angeben:")
            x = int(entry1.get())
            preis = preis + int(filme[x - 1].get_preis())
            #print("Gesamtpreis: " + str(preis) + " LEI")
            label_preis = Label(f1,width=40, text="Gesamtpreis: " + str(preis) + " LEI")
            label_preis.place(relx=0.4, rely=0.15)
        except Exception as e:
            print(str(e))

    @staticmethod
    def suchen(filme, entry, frame):

        """
        Methode furs Suchen nach Filmen mit der Wertung >= als eingegeben
        """
        try:
            wert = float(entry.get())
            k = 1
            lista = Listbox(frame, width=40, height=5)

            for film in filme:
                if float(film.get_wertung()) >wert:
                    lista.insert(k, film.get_titel() + ' ' + film.get_wertung())
                k += 1
            lista.place(relx=0.5, rely=0.5)
        except Exception as e:
            print(str(e))

    @staticmethod
    def schauspieler(filme, entry, frame):

        """
        Methode furs Anzeigen aller Filmen in denen ein Schauspieler spielt
        """
        try:
            ok = 0
            index = 1
            nume = entry.get()
            for film in filme:
                if nume in film.get_schauspieler():
                    ok = 1
                    lista = Listbox(frame, width=40, height=5)
                    lista.insert(index, film.get_titel())
                    lista.place(relx=0.6, rely=0.3)
                    index += 1
            if ok == 0:
                lista = Listbox(frame, width=40, height=5)
                lista.insert(index, " Kein Schauspieler gefunden")
                lista.place(relx=0.6, rely=0.3)
        except Exception as e:
            print(str(e))

    """
    @staticmethod
    def anzeigen(benutzer):

        
        # Methode furs Anzeigen aller Benutzern und ihre Bestellungen
        
        try:
            print("Anzeigen der Benutzern mit aktuellen Bestellungen: ")
            for i in range(0, len(benutzer)):
                print("Benutzer: " + benutzer[i].get_vorname() + ' ' + benutzer[i].get_nachname() + ' ' + " - Bestellungen: " + ' '.join(benutzer[i].get_bestellungen()))
        except Exception as e:
            print(str(e))
    """



    def menu_gemeinsam(self, benutzer, filme):

        """
        Zusammenfassungs-Menu der allen obigen Methoden enthalt und sie aufruft
        """
        try:
            print("Gemeinsames Menu")
            print("Zuruck zum Anfangsmenu: Taste 0")
            print("Furs Bestellung-Option drucken Sie Taste 1")
            print("Furs Anzeigen der Liste von Benutzern mit aktuellen Bestellungen drucken Sie Taste 2")
            print("Furs Suchen nach Filme mit einer spezifischen Wertung drucken Sie Taste 3")
            print("Furs Anzeigen aller Filmen mit einem gegebenen Schauspieler drucken Sie Taste 4")
            tasta = int(input("Tasta: "))
            while tasta != 0:
                if tasta == 0:
                    break
                elif tasta == 1:  # Bestellung-Option
                    self.bestellung_option(filme)
                elif tasta == 2:  # Liste von Benutzern mit aktuellen Bestellungen
                    self.anzeigen(benutzer)
                elif tasta == 3:  # Suchen nach Filmen mit einer spezifischen Wertung
                    self.suchen(filme)
                elif tasta == 4:  # Anzeigen aller Filmen mit einem gegebenen Schauspieler
                    self.schauspieler(filme)
                print("Menu Gemeinsam")
                print("Zuruck zum Anfangsmenu: Taste 0")
                print("Furs Bestellung-Option drucken Sie Taste 1")
                print("Furs Anzeigen der Liste von Benutzern mit aktuellen Bestellungen drucken Sie Taste 2")
                print("Furs Suchen nach Filme mit einer spezifischen Wertung drucken Sie Taste 3")
                print("Furs Anzeigen aller Filmen mit einem gegebenen Schauspieler drucken Sie Taste 4")
                tasta = int(input())
        except Exception as e:
            print(str(e))
