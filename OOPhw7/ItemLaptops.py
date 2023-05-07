from random import Random
from Laptop import Laptop
class ItemLaptops:

    def __init__(self) -> None:
        self.base = set()
        self.index = 0
    
    def addNew(self, item):
        self.base.add(item)
        self.index +=1
    def createRandom(self):
         ram = pow(2,1+Random().randint(0,7))
         rom = 1 + Random().randint(0,4)
         name = "name" + str(self.index+1)
         item = Laptop(name,ram,rom)
         return item
    
    def printbase(self):
        for i in self.base:
            print(i)