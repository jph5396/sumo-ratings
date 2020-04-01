import csv 
from wrestler import Wrestler

def loadWrestlers(wrestlerFilePath, baseElo):

    wrestlerDict = {}
    with open (wrestlerFilePath) as file:
        wrestlers = csv.reader(file, delimiter=",")
        
        # the next function call here skips the first line of the csv, which should be headers. 
        next(wrestlers)
        for row in wrestlers:
            addWrestler = Wrestler(wrestlerId= row[0], wName=row[1], highRank= row[2], dob= row[3], elo= baseElo)
            wrestlerDict[row[0]] = addWrestler

    return wrestlerDict    


