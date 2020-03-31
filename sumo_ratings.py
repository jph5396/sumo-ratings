import yaml
from verify_config import verify
from load_wrestlers import loadWrestlers
from load_bouts import loadBouts 
from wrestler import Wrestler
from bout import Bout


def main():
    
    with open('config.yaml') as configFile:
        config = yaml.load(configFile, Loader=yaml.FullLoader)

        # verifying the that config is valid. The program will terminate if it is not. 
        verify(config)
        wrestlerList = loadWrestlers(config['WRESTLERS_PATH'])
        boutList = loadBouts(config['BOUTS_PATH'])


        


if __name__ == '__main__':
    main()


            