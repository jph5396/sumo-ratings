import yaml
from verify_config import verify
from load_wrestlers import loadWrestlers
from load_bouts import loadBouts 
from timer import timer
from calculateElo import calculate
from print_controller import printContoller
from wrestler import Wrestler
from bout import Bout
from PostBoutListing import PostBoutListing



def main():
    with open('config.yaml') as configFile:
        config = yaml.load(configFile, Loader=yaml.FullLoader)

        # verifying the that config is valid. The program will terminate if it is not. 
        verify(config)
        
        # loads wrestler data and bout data. 
        wrestlerDict = loadWrestlers(config['WRESTLERS_PATH'], config['BASE_RATING'])
        boutList = loadBouts(config['BOUTS_PATH'])
        
        # calculate ELO ratings. 
        time = timer(startTimer=True)
        eloRatings = calculate(wrestlerDict, boutList, config['K_VALUE'])

        print(len(eloRatings), " total ratings were recorded")

        printContoller(eloRatings[len(eloRatings) - 70 : len(eloRatings) - 1],config['PRINT_STYLE'])

        time.stopWatch()

if __name__ == '__main__':
    main()


            