"""
Auteur: G van der Biezen
Naam bestand: persoon.py

Het volgende programma definieert het klasse Persoon. Instanties hier van
kunnen gemaakt worden met gegevens zoals naam, sekse, en geboortedatum.
Er zijn een aantal methoden gedefinieerd om gegevens aan te kunnen vragen.

Python versie: 3.10.2
IDE: IntelliJ IDEA Community Edition 2021.3.2
Last update: 06/06/2021
"""

from datetime import datetime


# opdracht 1
def format_date(datum: str) -> object:
    """ Maak van een datum string een datetime-object.

    :param datum: datum als een string.
    :return: een datetime object.
    """
    try:
        x = datetime.strptime(datum, "%d-%m-%Y")
        return x
    # exception als de datum format niet klopt.
    except (ValueError, TypeError):
        print("Geen geldige datum.")
# einde opdracht 1


# opdracht 2
class Persoon:
    """ Het klasse Persoon definieert aantal methoden om gegevens van
    een persoon op te slaan en aan te vragen. Zoals naam, sekse,
    geboortedatum en leeftijd."""

    def __init__(self, naam: str, sekse: str, geboortedatum: str):
        # naam mag alleen uit letters bestaan.
        if naam.isalpha() is True:
            self.__naam = naam
        else:
            self.__naam = None
            print(f"{naam} is geen geldige naam.")
        # sekse mag alleen M of V zijn.
        if sekse == 'M' or sekse == 'V' and sekse.isalpha() is True:
            self.__sekse = sekse
        else:
            self.__sekse = None
            print(f"{sekse} is geen geldige sekse. Vul M of V.")
        # geboortedatum zonder timestamp
        datum = format_date(geboortedatum)
        self.__geboortedatum = datum.date()
# einde opdracht 2

# opdracht 3
    def getNaam(self):
        """ Retourneert de naam. En 'onbekend' als de data
        niet geldig is."""
        if self.__naam is not None:
            return self.__naam
        else:
            return "Onbekend"

    def getGebDatum(self):
        """ Retourneert de geboorte datum. En 'onbekend' als
        de data niet geldig is."""
        if self.__geboortedatum is not None:
            return self.__geboortedatum
        else:
            return "Onbekend"

    def isMan(self):
        """ Retourneert True als sekse gelijk aan M is anders False.
        En 'onbekend' als de data niet geldig is."""
        if self.__sekse is not None:
            return bool(self.__sekse == 'M')
        else:
            return "Onbekend"

    def isVrouw(self):
        """ Retourneert True als sekse gelijk aan V is anders False.
        En 'onbekend' als de data niet geldig is."""
        if self.__sekse is not None:
            return bool(self.__sekse == 'V')
        else:
            return "Onbekend"
# einde opdracht 3

# opdracht 4
    def leeftijd(self):
        """ Retourneert de leeftijd door het verschil te berekenen
        tussen de huidige datum en de geboorte datum."""
        vandaag = datetime.today()  # datum van vandaag
        geb = self.__geboortedatum  # geboorte datum persoon

        # als de persoon al jarig is geweest dit jaar.
        if (vandaag.month, vandaag.day) >= (geb.month, geb.day):
            age = vandaag.year - geb.year
        # als de persoon nog niet jarig is geweest dit jaar.
        else:
            age = vandaag.year - geb.year - 1
        return age
# einde opdracht 4


# test codes
if __name__ == '__main__':

    # opdracht 1
    print(format_date("24-10-1973"))
    print()

    # opdracht 3
    p1 = Persoon('Jos', 'M', '24-10-1973')
    print(p1.getNaam(), p1.getGebDatum(), p1.isVrouw())
    print()

    # opdracht 4
    print(p1.getNaam(), p1.leeftijd())
