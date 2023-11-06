import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_and_find_player(self):
        self.assertEqual(self.stats.search("Yzerma").name, "Yzerman")

    def test_search_and_dont_find_player(self):
        self.assertEqual(self.stats.search("Kurrii"), None)

    def test_list_all_players_in_team(self):
        self.assertEqual(self.stats.team("PIT")[0].name, "Lemieux")

    def test_list_top_players(self):
        self.assertEqual(self.stats.top(4)[2].name, "Yzerman")
