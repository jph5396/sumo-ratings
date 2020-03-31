from datetime import datetime
from datetime import timedelta

class timer():
    
    def __init__(self, startTimer =False):
        if startTimer == True:
            self.start = datetime.now()
            print('Start time: ' + self.start.strftime("%H:%M:%S"))
        else:
            self.start = None

        self.stop = None

    
    def startWatch(self):
        if self.start == None:
            self.start = datetime.now()
        else:
            raise ValueError('Timer was already started. You have to reset it before starting it again')
    
    def stopWatch(self):
        self.stop = datetime.now()
        print('end time: ' + self.stop.strftime("%H:%M:%S"))
        print('____time elapsed: ' + str(self.stop - self.start))
    
    def reset(self):
        self.start = None
        self.stop = None 