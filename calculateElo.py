import math
from PostBoutListing import PostBoutListing
from wrestler import Wrestler
from bout import Bout

def calcWinProb(wrestlerRating, oppRating):

    winProb = 1/(1 + math.pow(10, (oppRating - wrestlerRating)/400))

    return winProb

def calcNewEloRating(oldRating, winProb, result, kVal):

    # score represents the actual outcome of the bout as an int
    score = 0 
    if (result == True):
        score = 1 
    
    newRating = oldRating + kVal * (score - winProb)

    return newRating 

def calculate(wrestlerDict, boutList, kVal):

    # an array containing all the results of the ELO calculations 
    resultsArr = [] 

    for  bout in boutList: 

        # currently I am not factoring draws into the ELO ratings. 
        # there are 10 total draws in the dataset, which is around 0.01% of bouts 
        if (bout.eWin == False and bout.wWin == False):
            print("draw")
        else:
            eastWrestler = wrestlerDict[bout.eWrestler]
            westWrestler = wrestlerDict[bout.wWrestler]

            oldEastElo = eastWrestler.elo
            oldWestElo = westWrestler.elo

            # calculating win probabilities 
            eastWinProb = calcWinProb(eastWrestler.elo, westWrestler.elo)
            westWinProb = calcWinProb(westWrestler.elo, eastWrestler.elo)

            # calculating new ratings. 
            eastWrestler.elo = calcNewEloRating(oldEastElo, eastWinProb, bout.eWin, kVal)
            westWrestler.elo = calcNewEloRating(oldWestElo, westWinProb, bout.wWin, kVal)

            # creating post bout listings and apprending to the results array 
            eWrestlerPostBout = PostBoutListing(
                tournamentId = bout.tournament, 
                day = bout.day, 
                wrestlerId = eastWrestler.wrestlerId, 
                wName= eastWrestler.wName,
                elo= eastWrestler.elo,
                change= (eastWrestler.elo - oldEastElo)
            )
            
            resultsArr.append(eWrestlerPostBout)
            
            wWrestlerPostBout = PostBoutListing(
                tournamentId= bout.tournament,
                day = bout.day,
                wrestlerId = westWrestler.wrestlerId,
                wName = westWrestler.wName,
                elo = westWrestler.elo,
                change= (westWrestler.elo - oldWestElo)
            )

            resultsArr.append(wWrestlerPostBout)



    return resultsArr

