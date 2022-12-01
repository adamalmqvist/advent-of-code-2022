import os
with open(os.getcwd() + '/day1/input.txt') as f:
  contents = f.read()

output = contents.split("\n\n")

arr = []
for item in output:
  itemTotal = 0 
  for number in item.split("\n"):
    if number.isnumeric(): 
      print('is a number', number)
      itemTotal += int(number)
    else: 
      print('is not a number', number)
  arr.append(itemTotal)

# First challenge answer:
print(max(arr))

arr.sort()
sum = arr[-1] + arr[-2] +  arr[-3]
# second challenge answer:
print(sum)

