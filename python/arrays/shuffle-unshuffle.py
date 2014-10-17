import random
SEED = 53792

myList = [ 'list', 'elements', 'go', 'here', 'do', 'your', 'job' ]
random.seed(SEED)
print random.random()
random.shuffle(myList)

print myList

Order = list(range(len(myList)))
# Order is a list having the same number of items as myList,
# where each position's value equals its index

random.seed(SEED)
print random.random()
random.shuffle(Order)
# Order is now shuffled in the same order as myList;
# so each position's value equals its original index

originalList = [0]*len(myList)   # empty list, but the right length
for index,originalIndex in enumerate(Order):
    originalList[originalIndex] = myList[index]
    # copy each item back to its original index

print originalList
