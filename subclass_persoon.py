"""
Auteur: G van der Biezen
Naam bestand: subclass_persoon.py

Het volgende programma definieert het subklasse Docent en Student van de
hoofdklasse Persoon. Elke subklasse heeft als extra zijn eigen methoden
gedefinieerd.

Python versie: 3.10.2
IDE: IntelliJ IDEA Community Edition 2021.3.2
Last update: 06/06/2021
"""

from persoon import Persoon  # importeert de baseclass Persoon


# opdracht 5
class Docent(Persoon):
    """ Definieert de subklasse Docent met een extra attribute 'salaris'.
     Als dit waarde is niet gegeven dan is het standaard 0"""
    def __init__(self, naam, sekse, geboortedatum, salaris=0):
        super().__init__(naam, sekse, geboortedatum)
        self.salaris = salaris

    def setSalaris(self, bedrag):
        """ Stel de waarde van het salaris met het gegeven bedrag in.
        De methode controlleert of `bedrag` een geldige waarde is van
        het type int of float en de laatste uit twee decimalen achter
        de punt bestaat.

        :param bedrag: bedrag
        """
        # Check of de data geen geldige format is bv. een string.
        if type(bedrag) is not int and type(bedrag) is not float:
            print("Geen geldige data formaat.")
            self.salaris = None
        # En check of een float bedrag uit 2 decimalen bestaat.
        else:
            x = round(bedrag, 2)
            check = bool(bedrag == x)
            if check is True:
                self.salaris = bedrag
            # Fout melding indien float meer dan 2 decimalen.
            else:
                self.salaris = None
                print(f"{bedrag} is geen geldige bedrag.")

    def getSalaris(self):
        """ Retourneert de salaris."""
        if self.salaris is not None:
            return float(self.salaris)

    def verhoogSalaris(self, p):
        """ Verhoogd het salaris met het percentage `p`.
        Rond het nieuwe bedrag op 2 decimalen.

        :param p: percentage voor de verhoging.
        """
        try:
            new_salaris = self.salaris * (100 + p) / 100
            self.salaris = round(new_salaris, 2)
        # exception als een van de gegevens niet kloppen.
        except TypeError:
            print("Verhoging mislukt - Controleer gegevens.")
# einde opdracht 5


# opdracht 6
class Student(Persoon):
    """ Definieert de subklasse Student. Elke student krijgt zijn eigen
     nummer. """
    __id = 0  # beginwaarde voor studentnummer

    def __init__(self, naam, sekse, geboortedatum):
        super().__init__(naam, sekse, geboortedatum)
        Student.__id += 1  # verhoog __id na elke instantie
        self.__student_nummer = Student.__id  # studentnummer
        self.opl_lijst = []  # lege lijst voor opleiding

    def getStudentnr(self):
        """ Retourneert de studentennummer."""
        return self.__student_nummer

    def voegOpleidingToe(self, opleiding):
        """ Voeg een `opleiding` toe aan het profiel van de student.

        :param opleiding: drie letter opleiding code
        """
        # check of de code uit letters bestaat en 3 letters lang.
        if opleiding.isalpha() is not True or len(opleiding) > 3:
            print("Toevoeging mislukt - Code moet 3 letters zijn.")
        else:
            self.opl_lijst.append(opleiding)

    def verwijderOpleiding(self, opleiding):
        """ Verwijder een `opleiding` van het profiel van de student.

        :param opleiding: drie letter opleiding code
        """
        # check of de code uit letters bestaat en 3 letters lang.
        if opleiding.isalpha() is not True or len(opleiding) > 3:
            print("Verwijdering mislukt - Code moet 3 letters zijn.")
        else:
            try:
                self.opl_lijst.remove(opleiding)
            # exception als de code niet in de lijst bestaat
            except ValueError:
                pass

    def volgtOpleiding(self, opleiding):
        """ Controleert of een opleiding in het profiel van de student
        bestaat. Retourneert True indien waar.

        :param opleiding: drie letter opleiding code
        :return: True of False
        """
        return bool(opleiding in self.opl_lijst)
# einde opdracht 6


# test code
if __name__ == '__main__':
    # opdracht 5
    d1 = Docent("Marcela", "V", "25-12-1988")
    print(d1.getNaam(), d1.leeftijd(), d1.isVrouw(), d1.getSalaris())

    d1.setSalaris(2500)
    print(d1.getSalaris())

    d1.verhoogSalaris(5)
    print(d1.getSalaris())
    print()

    # opdracht 6
    s1 = Student("Dennis", "M", "02-04-1995")
    print(s1.getStudentnr(), s1.getNaam(), s1.leeftijd())

    s2 = Student("Karima", "V", "15-12-1998")
    print(s2.getStudentnr(), s2.getNaam(), s2.leeftijd())

    s2.voegOpleidingToe("Inf")
    s2.voegOpleidingToe("TWi")
    print(s2.getNaam(), s2.volgtOpleiding("ChT"))
    print(s2.getNaam(), s2.volgtOpleiding("Inf"))

    s2.verwijderOpleiding("Inf")
    print(s2.getNaam(), s2.volgtOpleiding("Inf"))
