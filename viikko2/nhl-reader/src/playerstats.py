from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.__players = []
        for player_dict in reader.get_players():
            player = Player(player_dict)
            self.__players.append(player)

    def top_scorers_by_nationality(self, nationality):
        has_nationality = lambda p: p.nationality == nationality
        get_score = lambda p: p.score
        return sorted(filter(has_nationality, self.__players), key=get_score, reverse=True)
