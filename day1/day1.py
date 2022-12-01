import os
with open(os.getcwd() + '/day1/input.txt') as f:
  contents = f.read().split("\n\n")


summary = []
for item in contents:
  itemTotal = 0 
  for number in item.split("\n"):
    if number.isnumeric(): 
      print('is a number', number)
      itemTotal += int(number)
    else: 
      print('is not a number', number)
  summary.append(itemTotal)

# First challenge answer
print(max(summary))

summary.sort()
sumThreeLargestItems = summary[-1] + summary[-2] +  summary[-3]
# second challenge answer
print(sumThreeLargestItems)

