__author__ = 'rizki'

#import sys
import puremvc.patterns.facade


ASIDE_FACADE = "asideFacade"

class AsideFacade(puremvc.patterns.facade.Facade):

    def __init__(self, multitonKey):
        #self.initializeFacade()
        super(AsideFacade, self).__init__(multitonKey)

    @classmethod
    def getInstance(cls, key=ASIDE_FACADE):
        multitonKey = key
        if cls.instanceMap.get(multitonKey) == None:
            cls.instanceMap[multitonKey] = cls(multitonKey)

        return cls.instanceMap.get(multitonKey)

    def initializeFacade(self):
        super(AsideFacade, self).initializeFacade()
        self.initializeController()

    def initializeController(self):
        super(AsideFacade, self).initializeController()
