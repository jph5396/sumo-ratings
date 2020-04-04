import csv 
from Model.wrestler import Wrestler

def loadWrestlers(config):

    wrestlerDict = {}
    with open (config["WRESTLERS_PATH"]) as file:
        wrestlers = csv.reader(file, delimiter=",")
        
        # the next function call here skips the first line of the csv, which should be headers. 
        next(wrestlers)
        for row in wrestlers:
            addWrestler = Wrestler(wrestlerId= row[0], wName=row[1], highRank= row[2], dob= row[3], rating= config["BASE_RATING"])
            wrestlerDict[row[0]] = addWrestler

    return wrestlerDict    


