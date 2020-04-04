import yaml
from tabulate import tabulate
from Utils.verify_config import verify
from Utils.load_wrestlers import loadWrestlers
from Utils.load_bouts import loadBouts 
from Utils.timer import timer
from Calculate.elo import elo
from print_controller import printContoller


def main():
    with open('config.yaml') as configFile:
        config = yaml.load(configFile, Loader=yaml.FullLoader)

        # verifying the that config is valid. The program will terminate if it is not. 
        verify(config)
        
        # loads wrestler data and bout data. 
        wrestlerDict = loadWrestlers(config)
        boutList = loadBouts(config)
        
        # calculate ratings.
        # TODO: this directly calls an elo rating at the moment, but it really needs to call a 
        #       factory once other rating systems are implemented. The factory will choose which 
        #       rating system is returned.  
        time = timer(startTimer=True)
        rating = elo(wrestlerDict=wrestlerDict, tournamentBoutList=boutList, config=config)
        rating.calculate()

        print(tabulate(rating.getPrintableCareerHighs(), tablefmt="jira"))

       #printContoller(rating.getPrintableCareerHighs(),config['PRINT_STYLE'])

        time.stopWatch()

if __name__ == '__main__':
    main()


            