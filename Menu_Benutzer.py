from Class_Benutzer import Benutzer
from tkinter import *

class Menu_Benutzer:

    """
    MENU-Klasse
    -enthalt folgende Methoden : Einfugen, Aktualisieren, Loschen
    + zusammenfassung-menu

    """

    @staticmethod
    def einfugen(users, entry1, entry2, entry3):

        """
        Methode fur Einfugen eines neuen Benutzers in der Liste und in der Datei

        """

        print("EINFUGEN EINES NEUEN BENUTZERS")
        vorname = entry1.get()
        nachname = entry2.get()
        new_user = Benutzer(vorname, nachname)  # Erzeugt Objekt vom Typ Benutzer
        film = entry3.get()
        users.append(new_user)
        users[len(users)-1].set_bestellungen(film)
        print("Neuer Benutzer erfolgreich eingefugt ")

        # EINFUGEN DES NEUEN BENUTZERS IN DER DATEI
        with open("Users", "r") as file:
            data = file.readlines()
        data.append("\n" + str(vorname) + ", " + str(nachname) + ", "+str(film))
        with open("Users", "w") as file:
            file.writelines(data)

    @staticmethod
    def aktualisieren(users, entry1, entry2):

        """
        Methode fur Aktualisieren der Nachname des Benutzers sowohl in der Liste als auch in der Datei
        """
        try:
            found = 0
            print("Aktualisieren ")
            nachname = entry1.get()
            for i in range(0, len(users)):
                if users[i].get_nachname() == nachname or users[i].get_nachname() == nachname + ',\n':
                    found = 1
                    break
            if found == 1:
                users[i].set_nachname(entry2.get())
                print("Benutzerdaten erfolgreich aktualisiert ")
            else:
                print("Benutzer nicht gefunden")


            # AKTUALISIEREN DER NAME IN DER DATEI
            with open("Users", "w") as file:
                for user in users:
                    aux = ', '.join(str(v) for v in user.get_bestellungen())
                    file.writelines(
                        user.get_vorname() + ', ' + user.get_nachname() + ', ' + aux)
        except Exception as e:
            print(str(e))

    @staticmethod
    def loschen(users, entry1):

        """
        Methode fur Loschen eines gegebenen Benutzers sowohl in der Liste als auch in der Datei
        """
        try:
            found = 0
            nachname = entry1.get()
            for i in range(0, len(users)):
                if users[i].get_nachname() == nachname:
                    found = 1
                    break
            if found == 1:
                users.pop(i)
                print("Benutzer geloscht")
            else:
                print("Benutzer nicht gefunden")

            #LOSCHEN DES BENUTZERS IN DER DATEI
            with open("Users", "w") as file:
                for user in users:
                    aux = ', '.join(str(v) for v in user.get_bestellungen())
                    file.writelines(
                        user.get_vorname() + ', ' + user.get_nachname() + ', ' + aux)
        except Exception as e:
            print(str(e))

    def menu(self, users):

        """
        Zusammenfassungs-MENU der allen obigen Methoden enthalt
        """

        print("MENU BENUTZER")
        print("Zuruck zum Anfangsmenu: Taste 0")
        print("Fur Einfugen eines Benutzers drucken Sie Taste 1")
        print("Fur Aktualisierung der Nachname drucken Sie Taste 2")
        print("Fur Loschen eines gegebenen Benutzers drucken Sie Taste 3")

        try:
            tasta = int(input("TASTA: "))
            while tasta != 0:
                if tasta == 0:
                    break
                elif tasta == 1:  # Einfugen eines Films
                    self.einfugen(users)
                elif tasta == 2:  # Aktualisierung des Preises eines Films
                    self.aktualisieren(users)
                elif tasta == 3:  # Anzeigen aller Filmen
                    self.loschen(users)
                print("Menu Benutzer")
                print("Zuruck zum Anfangsmenu: Taste 0")
                print("Fur Einfugen eines Benutzers drucken Sie Taste 1")
                print("Fur Aktualisierung der Nachname drucken Sie Taste 2")
                print("Fur Loschen eines gegebenen Benutzers drucken Sie Taste 3")
                tasta = int(input("TASTA: "))
        except Exception as e:
            print(str(e))