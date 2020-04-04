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
        for key in self.wrestlerDict:
            if self.wrestlerDict[key].careerBouts > 0:
                returnArr.append(self.wrestlerDict[key].getObjAsShortList())
        return returnArr

    def getPrintableTournament(self, tournament):

        return self.postTournamentRatings[tournament]
    
    def getPrintableBoutList(self):
        return self.everyBoutRatings

    def updateCareerHighs(self, newBout):
        
       # if a wrestler's highRating is none, set the newBout to as the high rating. 
       # else compare the newBout rating and the wrestlers current high rating. 
       # replace high rating if the newBout rating is higher. 
        if self.wrestlerDict[newBout.wrestlerId].highRating is None:
            updatedWrestler = self.wrestlerDict[newBout.wrestlerId]
            updatedWrestler.highRating = newBout
            self.wrestlerDict[newBout.wrestlerId] = updatedWrestler

        else: 
            if  newBout.rating > self.wrestlerDict[newBout.wrestlerId].highRating.rating:
                updatedWrestler = self.wrestlerDict[newBout.wrestlerId]
                updatedWrestler.highRating = newBout
                self.wrestlerDict[newBout.wrestlerId] = updatedWrestler
            

    def onNewPostBout(self, newBout):
        self.everyBoutRatings.append(newBout)
        self.updateCareerHighs(newBout)
        self.wrestlerDict[newBout.wrestlerId].incrementCareerBouts()

