class Komento:
    _edellinen_tulos = 0

    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

class SyotteellinenKomento(Komento):
    def __init__(self, sovelluslogiikka, syote_funktio):
        super().__init__(sovelluslogiikka)
        self._syote_funktio = syote_funktio

    def _lue_syote(self):
        arvo = 0

        try:
            arvo = int(self._syote_funktio())
        except Exception:
            pass

        return arvo

class Summa(SyotteellinenKomento):
    def suorita(self):
        Komento._edellinen_tulos = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.plus(self._lue_syote())

class Erotus(SyotteellinenKomento):
    def suorita(self):
        Komento._edellinen_tulos = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.miinus(self._lue_syote())

class Nollaus(Komento):
    def suorita(self):
        Komento._edellinen_tulos = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

class Kumoa(Komento):
    def suorita(self):
        if Komento._edellinen_tulos != None:
            self._sovelluslogiikka.aseta_arvo(Komento._edellinen_tulos)
            Komento._edellinen_tulos = None
