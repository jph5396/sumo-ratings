import yaml
from verify_config import verify
from load_wrestlers import loadWrestlers
from load_bouts import loadBouts 
from timer import timer
from calculateElo import calculate
from wrestler import Wrestler
from bout import Bout
from PostBoutListing import PostBoutListing



def main():
    with open('config.yaml') as configFile:
        config = yaml.load(configFile, Loader=yaml.FullLoader)

        # verifying the that config is valid. The program will terminate if it is not. 
        verify(config)
        
        # loads wrestler data and bout data. 
        wrestlerDict = loadWrestlers(config['WRESTLERS_PATH'])
        boutList = loadBouts(config['BOUTS_PATH'])
        
        # calculate ELO ratings. 
        time = timer(startTimer=True)
        eloRatings = calculate(wrestlerDict, boutList, config['K_VALUE'])

        print(len(eloRatings))

        for listItem in range( len(eloRatings) - 70, len(eloRatings)):
            print(listItem)
            item = eloRatings[listItem]

            print(item.wName, item.elo, item.change)

        time.stopWatch()

if __name__ == '__main__':
    main()


            