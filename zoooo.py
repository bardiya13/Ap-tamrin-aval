class akvariom:
    def __init__(self,arz,tol,ertefa):
        self.fishes=[]#dorost kardan list baraye mahi haye dakhel akvariom
        self.arz=arz#int
        self.tol=tol#int
        self.ertefa=ertefa#int

    def addfish(self,mahi:mahiha):#agrition
        self.fishes.append(mahi)
    def gethagm(self):
        return arz*tol*ertefa
    def vaznakvariom(self):
        print(f"vazn akvariom {self.arz * self.tol * self.ertefa} kilogeram")
    def getfisheslist(self):
        for i in self.fishes:
            print(i)


class ghafas:
    def __init__(self,arzgh,tolgh,ertefagh):
        self.animals=[]
        self.arzgh=arzgh
        self.tolgh=tolgh
        self.ertefagh=ertefagh
    def addanimal(self,animal:pestandaran):#agrition
        self.animals.append(animal)
    def gethagm(self):#polimorism
        return arzgh*tolgh*ertefagh
    def getlistanimals(self):
        for i in self.animals:
            print(i)



class baghvahsh:
   def __init__(self,abadakvariomha,number_ghfas,tedadheyvanatghafas,tedadmahihayeakvariom,esmbaghevahsh):

       self.akvariomlist=[]
       for arz,tol,ertefa in abadakvariomha:
           self.akvariomlist.append(akvariom(arz,tol,ertefa))#compositaion
       self.tedadheyvanatghafas = tedadheyvanatghafas
       self.tedadmahihayeakvariom = tedadmahihayeakvariom
       self.esmbaghevahsh = esmbaghevahsh
       self.number_ghfas=number_ghfas
       self.ghafaslist=[]
       for arzgh,tolgh,ertefagh in ghafasha:
           self.ghafaslist.append(ghafas(arzgh,tolgh,ertefagh))#composition
   def getlistghafas(self):
       for i in self.ghafaslist:
           print(i)
   def getabadeakvarim(self):
       for i in self.akvariomlist:
           print(i)
   def getnamezoo(self):
       return self.esmbaghevahsh
   def tedadheyvanat(self):
       print((self.tedadmahihayeakvariom)+(self.tedadheyvanatghafas))

