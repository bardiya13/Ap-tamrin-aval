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
