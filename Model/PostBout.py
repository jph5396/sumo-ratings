from Model.printable import Printable

class PostBout(Printable):
    def __init__(self, tournamentId, day, wrestlerId, wName, rating, change, rank):
        self.tournamentId = tournamentId
        self.day = day 
        self.wrestlerId = wrestlerId
        self.rank = rank
        self.wName = wName 
        self.rating = rating
        self.change = change 

    def getObjAsShortList(self):

        shortList = [self.tournamentId, self.day, self.rank, self.rating]

        return shortList

    def getObjAsLongList(self):
        longList = [self.tournamentId, self.day, self.wrestlerId, self.wName, self.rating, self.change]

        return longList