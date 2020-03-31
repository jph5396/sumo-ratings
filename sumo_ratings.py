import yaml
from verify_config import verify
from load_wrestlers import loadWrestlers
from load_bouts import loadBouts 
from calculateElo import calculate
from wrestler import Wrestler
from bout import Bout



def main():
    
    with open('config.yaml') as configFile:
        config = yaml.load(configFile, Loader=yaml.FullLoader)

        # verifying the that config is valid. The program will terminate if it is not. 
        verify(config)

        # loads wrestler data and bout data. 
        wrestlerList = loadWrestlers(config['WRESTLERS_PATH'])
        boutList = loadBouts(config['BOUTS_PATH'])

        # calculate ELO ratings. 
        eloRatings = calculate(wrestlerList,boutList, config['SAVE_DETAILS'])



if __name__ == '__main__':
    main()


            