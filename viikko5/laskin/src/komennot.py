class Komento:
    def __init__(self, sovelluslogiikka, syote_funktio):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_funktio = syote_funktio

    def _lue_syote(self):
        arvo = 0

        try:
            arvo = int(self._syote_funktio())
        except Exception:
            pass

        return arvo

class Summa(Komento):
    def suorita(self):
        self._sovelluslogiikka.plus(self._lue_syote())

class Erotus(Komento):
    def suorita(self):
        self._sovelluslogiikka.miinus(self._lue_syote())

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumoa(Komento):
    def suorita(self):
        pass
