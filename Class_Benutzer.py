class Benutzer:

    """
    Benutzer-Klasse
    - enthalt - Konstruktor fur Initialisieren von Objekten vom Typ Benutzer
    - enthalt get- und set-Methoden fur die Attribute
    - zusatzliche get- und set- Methoden fur die Liste der Bestellungen
    - zusatzliche Methode __str__ fur das Konvertieren der Objekten in strings

    """
    def __init__(self, vorname, nachname):
        """
        KONSTRUKTOR der Klasse Benutzer
        - hat als Attribute den Namen und Vornamen aller Benutzer von der Datei

        """
        self.__vorname = vorname
        self.__nachname = nachname
        self.__bestellungen = []

    def get_vorname(self):
        return self.__vorname

    def set_vorname(self, vorname):
        self.__vorname = vorname

    def get_nachname(self):
        return self.__nachname

    def set_nachname(self, nachname):
        self.__nachname = nachname

    def get_bestellungen(self):
        return self.__bestellungen

    def set_bestellungen(self, bestellungen):
        self.__bestellungen.append(bestellungen)

    def get_Bestellungen_index(self, index):
        return self.__bestellungen[index]

    def __str__(self):
        return self.__vorname + ', ' + self.__nachname