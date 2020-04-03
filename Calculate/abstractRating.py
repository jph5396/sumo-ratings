from collections import defaultdict
from Model.PostBout import PostBout

class abstractRating:


    def __init__(self, wrestlerDict, tournamentBoutList, config):

        # data files, and config that sub classes will need to calculate ratings
        self.wrestlerDict = wrestlerDict
        self.tournamentBoutList = tournamentBoutList
        self.config = config

        # class variables used to store results of performance ratings calcuations 
        self.careerHighRatings = {}
        self.postTournamentRatings = defaultdict(list)
        self.everyBoutRatings = []
    
    def calculate(self):
        # the method that is called when its times to calculate 
        # new ratings 
        raise NotImplementedError

    
    def getPrintableCareerHighs(self):
        returnArr = []
        for key in self.careerHighRatings:
            returnArr.append(self.careerHighRatings[key].getObjAsLongList())
        return returnArr

    def getPrintableTournament(self, tournament):

        return self.postTournamentRatings[tournament]
    
    def getPrintableBoutList(self):
        return self.everyBoutRatings

    def updateCareerHighs(self, newBout):
        
        # if a wrestler exists see if the new value is their
        # career high, else set the new bout to his career
        # high since its the first value 
        if newBout.wrestlerId in self.careerHighRatings.keys():
           if newBout.elo > self.careerHighRatings[newBout.wrestlerId].elo:
               self.careerHighRatings[newBout.wrestlerId] = newBout
        else:
            self.careerHighRatings[newBout.wrestlerId] = newBout
            

    def onNewPostBout(self, newBout):
        self.everyBoutRatings.append(newBout)
        self.updateCareerHighs(newBout)

