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