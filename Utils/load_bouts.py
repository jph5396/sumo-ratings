import csv 
from collections import defaultdict
from Model.bout import Bout

def loadBouts(config):

    boutList = defaultdict(list)
    with open(config["BOUTS_PATH"]) as file: 
        bouts = csv.reader(file, delimiter=",")

        # skips first line because it should be headers. 
        next(bouts)
        for row in bouts:

            # When exporting data from the database, all booleans are 
            # represented as character values (t or f), so we need to get boolean 
            # values again.
            eWin = False
            wWin = False
            if(row[5] == 't'):
                eWin = True

            if(row[6] == 't'):
                wWin = True

            newBout = Bout(
                tournamentId= row[0],
                day= row[1],
                boutNum= row[2],
                eWrestler= row[3],
                wWrestler= row[4],
                eWin= eWin,
                wWin= wWin
            )

            boutList[newBout.tournament].append(newBout)

    return boutList
