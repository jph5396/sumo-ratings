from tabulate import tabulate
from PostBoutListing import PostBoutListing

def returnObjAsArrays(listToConvert, printStyle):

    convertedList = [] 
    if printStyle == 'short':
        for item in listToConvert: 
             
            convertedList.append(item.getObjAsShortList())
    
    if printStyle == 'long':
        for item in listToConvert:
            
            convertedList.append(item.getObjAsLongList())
    
    return convertedList


def printContoller(listToPrint, printStyle):
    printThis = returnObjAsArrays(listToPrint, printStyle)

    print(tabulate(printThis, tablefmt="fancy_grid"))
    