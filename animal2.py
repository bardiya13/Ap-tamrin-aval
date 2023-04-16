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


class pestandaran(mohredaran):
    def __init__(self, hagmemo, mahalezendegi, toleomr, toledom, dandan, tedadmohre, vazn, arz, sen):
        super().__init__(tedadmohre, vazn, arz, sen)
        self.hagmemo=hagmemo
        self.__mahalezendegi=mahalezendegi
        self.toleomr=toleomr
        self.toledom=toledom
        self.dandan=dandan

    def harekat(self):
        print("move")

    def afzayeshsen(self):
        self.sen+=1

    def getarz(self):
        return self.arz


    def khab(self):
        print("sleep zzz!")
        self.iskhab=True

    def bidar(self):
        self.iskhab=False

    def getmahalezendegi(self):
        return f"i from {self.__mahalezendegi}"
    def setmahalezendegi(self,mahalezendegi):
        self.__mahalezendegi=mahalezendegi
    #encapsilotion
    def gettoleomr(self):
        return f"sene ma {self.sen} hast va {self.toleomr-self.sen} sal digar zendam"
    def getdandan(self):
        return f"dandanhaye man {self.dandan} hast"
    def getdom(self):
        return f"andaze dome man {self.toledom} hast"
