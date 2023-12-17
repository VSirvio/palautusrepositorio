from luo_peli import PeliTyyppi, luo_peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = None

        if vastaus.endswith("a"):
            peli = luo_peli(PeliTyyppi.PELAAJA_VS_PELAAJA)
        elif vastaus.endswith("b"):
            peli = luo_peli(PeliTyyppi.TEKOALY)
        elif vastaus.endswith("c"):
            peli = luo_peli(PeliTyyppi.PAREMPI_TEKOALY)
        else:
            break

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        peli.pelaa()


if __name__ == "__main__":
    main()
