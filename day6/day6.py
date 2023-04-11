
import os
with open(os.getcwd() + '/day6/input.txt') as f:
    contents = f.read()

# Part one    

matchingItemsPartOne = []
for element in range(0, len(contents)):
   if contents[element] in matchingItemsPartOne:
    matchingItemsPartOne = []
   else:
    matchingItemsPartOne.append(contents[element])
    if len(matchingItemsPartOne) == 4:
        print(element + 1)
        break


# Part two

matchingItemsPartTwo = []
for element in range(0, len(contents)):
   if contents[element] in matchingItemsPartTwo:
    matchingItemsPartTwo = []
   else:
    matchingItemsPartTwo.append(contents[element])
    if len(matchingItemsPartTwo) >= 14:
        print(element + 1)
        break
        


