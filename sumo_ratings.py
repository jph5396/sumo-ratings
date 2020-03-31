import yaml
import csv 
from bout import bout
from verify_config import verify

def main():
    
    with open('config.yaml') as configFile:
        config = yaml.load(configFile, Loader=yaml.FullLoader)

        # verifying the that config is valid. The program will terminate if it is not. 
        verify(config)



if __name__ == '__main__':
    main()


            