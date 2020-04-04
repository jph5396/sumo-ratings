from Model.printable import Printable

class Wrestler(Printable): 
    def __init__(self, wrestlerId, wName, highRank, dob, rating):
        self.wrestlerId = wrestlerId
        self.wName = wName
        self.highRank = highRank
        self.dob = dob 
        self.rating = rating
        self.careerBouts = 0
        self.highRating = None 

    def incrementCareerBouts(self):
        self.careerBouts += 1 

    def getObjAsShortList(self):
        #get a minified list of the object for printing 
        returnArr = [self.wName, self.highRank] + self.highRating.getObjAsShortList()
        return returnArr 

    def getObjAsLongList(self):
        #get a full version of the object as a list for printing
        pass

    