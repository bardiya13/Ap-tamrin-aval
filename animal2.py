# Python program showing
# abstract base class work
from abc import ABC, abstractmethod

class mohredaran(ABC):

    @abstractmethod
    def __init__(self,tedadmohre,vazn,arz,sen):
        slef.tedadmohre=tedadmohre
        self.vazn=vazn
        self.arz=arz
        self.iskhab=False
        self.sen=sen

    @abstractmethod
    def harekat(self):
        pass

    @abstractmethod
    def afzayeshsen(self):
        pass

    @abstractmethod
    def getarz(self):
        pass

    @abstractmethod
    def khab(self):
        pass

    @abstractmethod
    def bidar(self):
        pass
