class TennisGame:
    __WINNING_LIMIT = 4

    def __init__(self, player1_name, player2_name):
        self.__player1_name = player1_name
        self.__player2_name = player2_name
        self.__score1 = self.__score2 = 0

    def won_point(self, player_name):
        if player_name == self.__player1_name:
            self.__score1 += 1
        else:
            self.__score2 += 1

    @classmethod
    def __get_score_str_when_both_scores_same(cls, score_num):
        match score_num:
            case 0: return "Love-All"
            case 1: return "Fifteen-All"
            case 2: return "Thirty-All"
            case _: return "Deuce"

    @classmethod
    def __get_score_str_when_past_winning_limit(cls, score1, score2):
        if score1 > score2:
            score_difference = score1 - score2
            if score_difference >= 2:
                return "Win for player1"
            else:
                return "Advantage player1"
        else:
            score_difference = score2 - score1
            if score_difference >= 2:
                return "Win for player2"
            else:
                return "Advantage player2"

    @classmethod
    def __get_score_str_in_basic_case(cls, score_num):
        match score_num:
            case 0: return "Love"
            case 1: return "Fifteen"
            case 2: return "Thirty"
            case 3: return "Forty"

    def get_score(self):
        if self.__score1 == self.__score2:
            return TennisGame.__get_score_str_when_both_scores_same(self.__score1)
        elif self.__score1 >= TennisGame.__WINNING_LIMIT or\
             self.__score2 >= TennisGame.__WINNING_LIMIT:
            return TennisGame.__get_score_str_when_past_winning_limit(self.__score1, self.__score2)
        else:
            return TennisGame.__get_score_str_in_basic_case(self.__score1) + "-" +\
                   TennisGame.__get_score_str_in_basic_case(self.__score2)
