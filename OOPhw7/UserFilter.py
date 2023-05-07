from Laptop import Laptop 
class UserFilter:

    def __init__(self,dataBase) -> None:
        self.userHere = True
        self.base = set()
        self.filterBase = set()
        self.filter = Laptop()
        self.base = set(dataBase)

    def printFilter(self):
        for i in self.filterBase:
            print(i)
    def printbase(self):
        for i in self.base:
            print(i)

    def printOptions(self):
        print("0 - exit")
        print("1 - model (" + self.filter.getOption("name") + ")")
        print("2 - RAM (" + str(self.filter.getOption("ram")) + ")")
        print("3 - ROM (" + str(self.filter.getOption("rom")) + ")")


    def askFilter(self):
        self.printOptions()
        userChoice = int(input("Option: "))
        self.askOption(userChoice)
        self.runFilter()
        self.printFilter()

    def askOption(self,userChoice):
        if(userChoice == 1): 
            optionName = "name"
            value = str(input("name: "))
        elif(userChoice == 2): 
            value = int(input("RAM: "))
            optionName = "ram"
        elif(userChoice == 3): 
            value = int(input("Rom: "))
            optionName = "rom"
        self.filter.setOption(optionName,value)

    def runFilter(self):
        self.filterBase = self.base.copy()
        self.filterByRam()
        self.filterByRom()
        self.filterByName()
    def filterByOption(self,optionName):
        for item in self.base:
            if item in self.filterBase:
                if self.filter.compare(item,optionName):
                    self.filterBase.remove(item)
                    
    def filterByRam(self):
        self.filterByOption("ram")
    def filterByRom(self):
        self.filterByOption("rom")
    def filterByName(self):
        self.filterByOption("name")
    





            

    

        

