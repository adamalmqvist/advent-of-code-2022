import os
with open(os.getcwd() + '/day5/input.txt') as f:
    contents = f.read().split("\n\n")
# part one:
startArray = [
['R', 'N', 'P', 'G'], 
['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'], 
['T', 'D', 'B', 'M', 'N', 'L'], 
['R', 'V', 'P', 'S', 'B'], 
['G','C','Q','S','W','M', 'V', 'H'], 
['W', 'Q', 'S', 'C', 'D', 'B', 'J'],
['F', 'Q', 'L'],
['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
['L', 'P', 'B', 'V', 'M', 'J', 'F']
]

rearrangementProcedure = contents[1].split("\n")
del rearrangementProcedure[-1]

for row in rearrangementProcedure:
    numberOfItems, index, destination = [int(i) for i in row.split() if i.isdigit()]
    itemsToMove = startArray[index - 1][-numberOfItems:]
    del startArray[index - 1][-numberOfItems:]
    startArray[destination - 1].extend(itemsToMove[::-1])

print('finnished', startArray)
for array in startArray:
    print(array[-1])
# part two:

startArray = [
['R', 'N', 'P', 'G'], 
['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'], 
['T', 'D', 'B', 'M', 'N', 'L'], 
['R', 'V', 'P', 'S', 'B'], 
['G','C','Q','S','W','M', 'V', 'H'], 
['W', 'Q', 'S', 'C', 'D', 'B', 'J'],
['F', 'Q', 'L'],
['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
['L', 'P', 'B', 'V', 'M', 'J', 'F']
]

rearrangementProcedure = contents[1].split("\n")
del rearrangementProcedure[-1]

for row in rearrangementProcedure:
    numberOfItems, index, destination = [int(i) for i in row.split() if i.isdigit()]
    itemsToMove = startArray[index - 1][-numberOfItems:]
    del startArray[index - 1][-numberOfItems:]
    startArray[destination - 1].extend(itemsToMove)

print('finnished', startArray)
for array in startArray:
    print(array[-1])