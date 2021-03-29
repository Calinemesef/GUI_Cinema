from Menu_Benutzer import *
from Menu_Filme import *
from Class_Benutzer import *
from Class_Film import *


class Main:

    """
    Die Main-Klasse, hat folgende Methoden:
        - Methode fur Erzeugen der Anfangsliste des Benutzers/Films von deren entsprechenden Datei
        - Methode furs Anzeigen des Anfangsmenu mit allen entsprechenden Methoden drin
    """

    @staticmethod
    def anfangsliste_benutzer(users):

        """
        Methode furs Erzuegen der Anfangsliste der Benutzer
        - Liest die entsprechende Datei ein und fugt sich alle Benutzern als Objekte in einer Liste ein
        """

        index_utilizator = 0
        file = open("Users", "r")
        lines = file.readlines()
        for line in lines:
            thisline = line.split(", ")
            users.append(Benutzer(thisline[0], thisline[1]))
            for i in range(2, len(thisline)):
                users[index_utilizator].set_bestellungen(thisline[i])
            index_utilizator += 1
        file.close()

    @staticmethod
    def anfangsliste_filmen(filme):

        """
        Methode furs Erzeugen der Anfangsliste der Filmen
        - liest die entsprechende Datei ein und fugt sich alle Filmen als Objekte in einer Liste ein

        """

        index_film = 0
        file = open("Movies", "r")
        lines = file.readlines()
        for line in lines:
            thisline = line.split(", ")
            filme.append(Film(thisline[0], thisline[1], thisline[2], thisline[3]))
            for i in range(4, len(thisline)):
                filme[index_film].set_schauspieler(thisline[i])
            index_film += 1
