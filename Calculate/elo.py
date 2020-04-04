import math
from Calculate.abstractRating import abstractRating
from Model.PostBout import PostBout
from Model.wrestler import Wrestler
from Model.bout import Bout

class elo(abstractRating):

    def calculate(self):

        for  tournament in self.tournamentBoutList: 

            
            for bout in self.tournamentBoutList[tournament]:
                # currently I am not factoring draws into the ELO ratings. 
                # there are 10 total draws in the dataset, which is around 0.01% of bouts
                # It will be better to provide a dataset that dont contain any draws if this 
                # is the case. 
                
                if (bout.eWin == False and bout.wWin == False):
                    print("draw")

                # if both wrestlers exist in wrestler dictionary run 
                elif(bout.eWrestler in self.wrestlerDict and bout.wWrestler in self.wrestlerDict):
                    eastWrestler = self.wrestlerDict[bout.eWrestler]
                    westWrestler = self.wrestlerDict[bout.wWrestler]

                    oldEastElo = eastWrestler.rating
                    oldWestElo = westWrestler.rating

                    # calculating win probabilities 
                    eastWinProb = calcWinProb(eastWrestler.rating, westWrestler.rating)
                    westWinProb = calcWinProb(westWrestler.rating, eastWrestler.rating)

                    # calculating new ratings. 
                    eastWrestler.rating = calcNewEloRating(oldEastElo, eastWinProb, bout.eWin, self.config['K_VALUE'])
                    westWrestler.rating = calcNewEloRating(oldWestElo, westWinProb, bout.wWin, self.config['K_VALUE'])

                    # creating post bout listings and apprending to the results array 
                    eWrestlerPostBout = PostBout(
                        tournamentId = bout.tournament, 
                        day = bout.day, 
                        wrestlerId = eastWrestler.wrestlerId, 
                        rank= bout.eRank,
                        wName= eastWrestler.wName,
                        rating= eastWrestler.rating,
                        change= (eastWrestler.rating - oldEastElo)
                    )
                    self.onNewPostBout(eWrestlerPostBout)

                    wWrestlerPostBout = PostBout(
                        tournamentId= bout.tournament,
                        day = bout.day,
                        wrestlerId = westWrestler.wrestlerId,
                        rank = bout.wRank,
                        wName = westWrestler.wName,
                        rating = westWrestler.rating,
                        change= (westWrestler.rating - oldWestElo)
                    )
                    self.onNewPostBout(wWrestlerPostBout)
                

def calcWinProb( wrestlerRating, oppRating):

        winProb = 1/(1 + math.pow(10, (oppRating - wrestlerRating)/400))

        return winProb

def calcNewEloRating(oldRating, winProb, result, kVal):

    # score represents the actual outcome of the bout as an int
    score = 0 
    if (result == True):
        score = 1 
    
    newRating = oldRating + kVal * (score - winProb)

    return newRating 