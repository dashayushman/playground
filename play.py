mylist = [{"name": "ads", "roll": 1}, {"name": "Dbe", "roll": 18}, {"name": "aks", "roll": 24}]

# Sort a list of dictionary objects by a key - case sensitive
from operator import itemgetter
mylist = sorted(mylist, key=itemgetter('name', "roll"))

print(list(mylist))
# Sort a list of dictionary objects by a key - case insensitive
mylist = sorted(mylist, key=lambda k: k['name'].lower())

print(list(mylist))
