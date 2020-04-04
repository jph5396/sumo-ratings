import os
import datetime
import csv

class SaveController: 
    def __init__(self, config, ratingObj):
        self.ratingObj = ratingObj
        self.saveFmt = config["SAVE_FORMAT"]
        self.saveCareerHighs = config["SAVE_CAREER_HIGHS"]
        self.saveDaily = config["SAVE_DAILY"]
        self.saveDir = config["SAVE_DIR"]

    def save(self):

        # checks to see if given directory exists 
        # if true then creates the save files for this run
        # TODO: 
        #   add logic to create the directory if it does not exist. 
        if os.path.isdir(self.saveDir):
            d = datetime.datetime.today()
            dStr = str(d.year) + str(d.month) + str(d.day) + str(d.hour) + str(d.minute) + str(d.second)
            runSaveFolder = self.saveDir + "/" + dStr
            os.mkdir(runSaveFolder)

            if self.saveCareerHighs == True:
                fileName = "/careerhighs.csv"
                with open(file=runSaveFolder + fileName, mode='w', newline='') as targetFile:
                    writer = csv.writer(targetFile)
                    writer.writerows(self.ratingObj.getPrintableCareerHighs())
