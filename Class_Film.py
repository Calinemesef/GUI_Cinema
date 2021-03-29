class Film:
    """
    Film-Klasse
    Attribute: Titel, Jahr, Wertung, Preis, Schauspieler
    -enthalt - Konstruktor fur Initialisieren von Objekten vom Typ Film
             - entsprechende get und set Methoden fur die Attribute

    """

    def __init__(self, titel, jahr, wertung, preis):
        """
        KONSTRUKTOR der Klasse Filmm
        - hat als Attribute : Titel, Jahr, Wertung, Preis der Filmen aus der Datei
        """

        self.__titel = titel
        self.__jahr = jahr
        self.__wertung = wertung
        self.__preis = preis
        self.__schauspieler = []

    def get_titel(self):
        return self.__titel

    def set_titel(self, titel):
        self.__titel = titel

    def get_jahr(self):
        return self.__jahr

    def set_jahr(self, jahr):
        self.__jahr = jahr

    def get_wertung(self):
        return self.__wertung

    def set_wertung(self, wertung):
        self.__wertung = wertung

    def get_schauspieler(self):
        return self.__schauspieler

    def get_schauspieler_index(self, index):
        return self.__schauspieler[index]

    def set_schauspieler(self, schauspieler):
        self.__schauspieler.append(schauspieler)

    def get_preis(self):
        return self.__preis

    def set_preis(self, preis):
        self.__preis = preis

    def __str__(self):
        return self.__titel
