
# a class representing a single bout between two wrestlers. 

class Bout:
    def __init__(self, tournamentId, day, boutNum, eWrestler, eRank, eWin, wWrestler,wRank, wWin):
        self.tournament = tournamentId
        self.day = day
        self.boutNum = boutNum 
        self.eWrestler = eWrestler
        self.wWrestler = wWrestler 
        self.eWin = eWin
        self.wWin = wWin
        self.eRank = eRank 
        self.wRank = wRank
