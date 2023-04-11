import os
with open(os.getcwd() + '/day8/input.txt') as f:
    input = f.read().splitlines()


totalVisibleTrees = 0

def getNumberOfTreesOnEdge(trees):
    total = 0
    firstRow = len(trees[0])
    total += firstRow
    lastRow = len(trees[-1])
    total += lastRow
    treesOnSidesOfMiddleRows = (len(trees) - 2) * 2
    total += treesOnSidesOfMiddleRows
    return total

def convertToList(string):
    list1 = []
    list1[:0] = string
    return list1

totalVisibleTrees += getNumberOfTreesOnEdge(input)

del input[0]
del input[-1]
for row in input:
    threeRow = convertToList(row)
    for index, treeHeight in enumerate(threeRow):
        if index == 0 or index == len(threeRow) - 1:
            continue
            
        rangeLeft = threeRow[:index]
        rangeRight = threeRow[index + 1:]

        maxHeightLeft = max(rangeLeft)  
        maxHeightRight = max(rangeRight)
        if treeHeight > maxHeightLeft or treeHeight > maxHeightRight:
            totalVisibleTrees += 1
            continue
            

 
print('totalVisibleTrees', totalVisibleTrees)