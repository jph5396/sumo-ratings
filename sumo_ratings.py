import yaml
import csv 
from bout import bout
from verify_config import verify

def main():
    
    with open('config.yaml') as configFile:
        config = yaml.load(configFile, Loader=yaml.FullLoader)
        verify(config)


    # with open (config['FILE']) as dataSource: 
    #     data = csv.reader(dataSource, delimiter=',')   
    #     for i, row in enumerate(data):

    #         eastWin = False 
    #         westWin = False 
    #         if (row[5] == 't'):
    #             eastWin = True

    #         if(row[6] == 't'):
    #             westWin = True

    #         newBout = new bout(tournamentId= row[0], day= row[1], boutNum=row[2]
    #         eWrestler= row[3], wWrestler= row[4], eWin= eastWin, wWin= westWin)

    #         boutList.append(newBout)
             
            

if __name__ == '__main__':
    main()


            