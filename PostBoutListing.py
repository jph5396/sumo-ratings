from printable import Printable

class PostBoutListing(Printable):
    def __init__(self, tournamentId, day, wrestlerId, wName, elo, change):
        self.tournamentId = tournamentId
        self.day = day 
        self.wrestlerId = wrestlerId
        self.wName = wName 
        self.elo = elo
        self.change = change 

    def getObjAsShortList(self):

        shortList = [self.wName, self.elo, self.change]

        return shortList

    def getObjAsLongList(self):
        longList = [self.tournamentId, self.day, self.wrestlerId, self.wName, self.elo, self.change]

        return longList