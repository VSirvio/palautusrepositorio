from matchers import And, Or, PlaysIn, HasAtLeast, HasFewerThan, All, Not

class QueryBuilder:
    def __init__(self):
        self._query = All()

    def build(self):
        return self._query

    def playsIn(self, team):
        self._query = And(self._query, PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._query = And(self._query, HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._query = And(self._query, HasFewerThan(value, attr))
        return self
