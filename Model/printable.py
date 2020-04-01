import abc

# abstract class serving as an interface for printing
class Printable(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def getObjAsShortList(self):
        #get a minified list of the object for printing 
        raise NotImplementedError

    @abc.abstractmethod
    def getObjAsLongList(self):
        #get a full version of the object as a list for printing
        raise NotImplementedError 
    
    # @abc.abstractmethod
    # def getHeaders(self):
    #     # get headers for the printable object.
    #     # raise NotImplementedError
    #     pass