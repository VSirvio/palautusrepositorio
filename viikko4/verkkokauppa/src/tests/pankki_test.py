import unittest
from unittest.mock import Mock
from pankki import Pankki

class TestPankki(unittest.TestCase):
    def test_tilisiirrosta_tehdaan_oikeanlainen_kirjaus(self):
        kirjanpito_mock = Mock()
        pankki = Pankki(kirjanpito_mock)

        pankki.tilisiirto("Jaska Jokunen", 478, "34235-96347", "54339-32899", 56)

        kirjanpito_mock.lisaa_tapahtuma.assert_called_with(
            "tilisiirto: tililtä 34235-96347 tilille 54339-32899 viite 478 summa 56e"
        )
