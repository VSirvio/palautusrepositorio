from enum import Enum
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

PeliTyyppi = Enum('PeliTyyppi', ['PELAAJA_VS_PELAAJA', 'TEKOALY', 'PAREMPI_TEKOALY'])

def luo_peli(tyyppi : PeliTyyppi):
    match tyyppi:
        case PeliTyyppi.PELAAJA_VS_PELAAJA:
            return KPSPelaajaVsPelaaja()
        case PeliTyyppi.TEKOALY:
            return KPSTekoaly()
        case PeliTyyppi.PAREMPI_TEKOALY:
            return KPSParempiTekoaly()
