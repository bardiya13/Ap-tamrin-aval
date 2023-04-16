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

class dopa(pestandaran):
    def __init__(self, tabaghezangire, zistgah,  meghdarghazayemoredniyaz, tolgam, hagmemo, mahalezendegi,
                 toleomr, toledom, dandan, tedadmohre, vazn, arz, sen):
        super().__init__(hagmemo, mahalezendegi, toleomr, toledom, dandan, tedadmohre, vazn, arz, sen)
        self.tabaghezangire=tabaghezangire
        self.zistgah=zistgah
        self.tedade_pa=2#in moteghayer az ghabl adadi sabet ast
        self.meghdarghazayemoredniyaz=meghdarghazayemoredniyaz
        self.tolgam=tolgam

    def get_tedad_ghadam(self,masafatharekat):
        return f"{masafatharekat/self.tolgam}"#barye in tabe moteghayer gadid niyaz ast ke karbar behemon bede
    def get_tabaghe_ghazayi(self,name):#barye in tabe moteghayer gadid niyaz ast ke karbar behemon bede
        return f"{name} dar tabaghe {self.tabaghezangire} hastam"
    def get_zistgah(self):
        return f"zistgahe man {self.zistgah} hast"
    def tedad_mandeha_az_dopa(self):
        return f"{self.tedade_pa} az dopa vogod darad"


class parande(dopa):
    def __init__(self, ertefaparvaz, soratparvaz, gone, tolebal, zamanparvaz, tabaghezangire, zistgah,
                 meghdarghazayemoredniyaz, tolgam, hagmemo, mahalezendegi, toleomr, toledom, dandan, tedadmohre, vazn,
                 arz, sen):
        super().__init__(tabaghezangire, zistgah,meghdarghazayemoredniyaz, tolgam, hagmemo,
                         mahalezendegi, toleomr, toledom, dandan, tedadmohre, vazn, arz, sen)
        self.ertefaparvaz=ertefaparvaz
        self.soratparvaz=soratparvaz
        self.gone=gone
        self.tolebal=tolebal
        self.zamanparvaz=zamanparvaz
    def getertefaeparvaz(self):
        return f"man {self.ertefaparvaz} balaye sathe zamin parvaz mikonam"
    def getgone(self):
        return f"man az gone {self.gone} hastam"
    def gettolebal(self):
        return f"tole bal man {self.tolebal} hast"
    def speak(self):#polymorism
        return "ghar ghar!"


class ensan(dopa):
    def __init__(self, pol, sathtahsilat, esm, famili, tedadbache, tabaghezangire, zistgah,
                 meghdarghazayemoredniyaz, tolgam, hagmemo, mahalezendegi, toleomr, toledom, dandan, tedadmohre, vazn,
                 arz, sen):
        super().__init__(tabaghezangire, zistgah, meghdarghazayemoredniyaz, tolgam, hagmemo,
                         mahalezendegi, toleomr, toledom, dandan, tedadmohre, vazn, arz, sen)
        self.pol=pol
        self.sathtahsilat=sathtahsilat# type vorodi str ast
        self.esm=esm# type vorodi str ast
        self.famili=famili# type vorodi str ast
        self.tedadbache=tedadbache
    def getpol(self):
        return f"man {self.pol} daram"
    def getesm(self):
        return f"esme man {self.esm} hast"
    def getfamili(self):
        return f"famili man {self.famili} hast"
    def speak(self):
        return "language!"# estefadeh az polymorism


class meymon(dopa):
    def __init__(self, ertefaparesh, rang, ghazayemoredalaghe, damyebadan, toledast, tabaghezangire, zistgah,
                  meghdarghazayemoredniyaz, tolgam, hagmemo, mahalezendegi, toleomr, toledom, dandan,
                 tedadmohre, vazn, arz, sen):
        super().__init__(tabaghezangire, zistgah, meghdarghazayemoredniyaz, tolgam, hagmemo,
                         mahalezendegi, toleomr, toledom, dandan, tedadmohre, vazn, arz, sen)
        self.ertefaparesh=ertefaparesh #type vorodi str
        self.rang=rang# type vorodi str
        self.ghazayemoredalaghe=ghazayemoredalaghe# type vorodi str
        self.damyebadan=damyebadan# type voroodi int
        self.toledast=toledast# type vorodi int
    def getrang(self):
        return f"range man {self.rang} hast"
    def gettoledast(self):
        return f"tole dast man {self.toledast}"
    def getertefaparesh(self):
        return f"ertefae paresh man {self.ertefaparesh} hast"
    def speak(self):#estefade az polymorism
        return "va va va va!"
