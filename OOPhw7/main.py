from ItemLaptops import ItemLaptops
from Laptop import Laptop
from UserFilter import UserFilter


items = ItemLaptops()
for i in range(0,10):
    items.addNew(items.createRandom())

filter = UserFilter(items.base)
filter.printbase()
while filter.userHere:
    filter.askFilter()
