import os
with open(os.getcwd() + '/day2/input.txt') as f:
    contents = f.read().split("\n")

total_score = 0

def getScoreBasedOnShape(shape):
    if shape == 'X':
        return 1
    elif shape == 'Y':
        return 2
    elif shape == 'Z':
        return 3

for round in contents:
    choises = round.split(' ')
    if len(choises) == 1:
        print('choises', choises)
        break
    
    opponent_choice = choises[0]
    our_choice = choises[1]


    if (opponent_choice == 'A' and our_choice == 'X') or (opponent_choice == 'B' and our_choice == 'Y') or (opponent_choice == 'C' and our_choice == 'Z'):
        # Draw
        score = 3
    elif (our_choice == 'X' and opponent_choice == 'C') or (our_choice == 'Y' and opponent_choice == 'A') or (our_choice == 'Z' and opponent_choice == 'B'):
        # We win
        score = 6
    else:
        # We lose
        score = 0
    total_score += score + getScoreBasedOnShape(our_choice)
    

    print(total_score)

# round two

    def getWinningShape(shape):
      if shape == 'A':
        return 'Y'
      elif shape == 'B':
        return 'Z'
      elif shape == 'C':
        return 'X'
    
    def getLosingShape(shape):
        if shape == 'A':
            return 'Z'
        elif shape == 'B':
            return 'X'
        elif shape == 'C':
            return 'Y'
    
    def getDrawShape(shape):
        if shape == 'A':
            return 'X'
        elif shape == 'B':
            return 'Y'
        elif shape == 'C':
            return 'Z'
      
    def getScoreBasedOnOpponent(shape, desiredOutcome):
        if (shape == 'A' or 'B' or 'C') and desiredOutcome == 'Z':
         myShape = getWinningShape(shape)
         return getScoreBasedOnShape(myShape) + 6
        if (shape == 'A' or 'B' or 'C') and desiredOutcome == 'Y':
         myShape = getDrawShape(shape)
         return getScoreBasedOnShape(myShape) + 3
        if (shape == 'A' or 'B' or 'C') and desiredOutcome == 'X':
         myShape = getLosingShape(shape)
         return getScoreBasedOnShape(myShape) + 0
    
total_score_part_two = 0  
for round in contents:
    # Choose our move based on the strategy guide
    choises = round.split(' ')
    if len(choises) == 1:
        print('choises', choises)
        break

    opponentChoice = choises[0]
    desiredOutcome = choises[1]
    print(getScoreBasedOnOpponent(opponentChoice, desiredOutcome) )
    total_score_part_two += getScoreBasedOnOpponent(opponentChoice, desiredOutcome)

    # Add the score for this round to the total score

print(total_score)
