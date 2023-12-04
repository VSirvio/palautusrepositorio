KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    @classmethod
    def _validoi_syote(cls, attribuutin_nimi, syote, oletus_arvo):
        if syote is None:
            return oletus_arvo
        elif not isinstance(syote, int) or syote < 0:
            raise Exception("Virheellinen " + attribuutin_nimi)
        else:
            return syote

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = IntJoukko._validoi_syote("kapasiteetti", kapasiteetti, KAPASITEETTI)
        self.kasvatuskoko = IntJoukko._validoi_syote("kasvatuskoko", kasvatuskoko, OLETUSKASVATUS)
        self.alkiot = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if self.alkiot[i] == n:
                return True
        return False

    def _kasvata_listaa(self):
        taulukko_old = self.alkiot
        self.alkiot = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.alkiot)

    def lisaa(self, uusi_alkio):
        if self.kuuluu(uusi_alkio):
            return False

        self.alkiot[self.alkioiden_lkm] = uusi_alkio
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm >= len(self.alkiot):
            self._kasvata_listaa()

        return True

    def poista(self, poistettava_alkio):
        for i in range(0, self.alkioiden_lkm):
            if self.alkiot[i] == poistettava_alkio:
                for j in range(i, self.alkioiden_lkm - 1):
                    self.alkiot[j] = self.alkiot[j + 1]
                self.alkiot[self.alkioiden_lkm - 1] = 0
                self.alkioiden_lkm -= 1
                return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.alkiot[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste_joukko.lisaa(b_taulu[i])

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus_joukko.lisaa(b_taulu[j])

        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus_joukko.poista(b_taulu[i])

        return erotus_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            alkiot_mjono = ""
            for i in range(0, self.alkioiden_lkm - 1):
                alkiot_mjono += str(self.alkiot[i]) + ", "
            return "{" + alkiot_mjono + str(self.alkiot[self.alkioiden_lkm - 1]) + "}"
