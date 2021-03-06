############################################
## INITIALIZING PLAYERS AND PYGAME SCREEN ##
############################################

import random

names = [''] * 40
from drv import randomrunner

names[30] = "Random Runner"
from drv import offlikeashot

names[31] = "Off Like A Shot"
from drv import steadyfreddy

names[32] = "Steady Freddy"

from ai import ai

names[16] = "ai"


def controller(num, mypos, myfunds, distances):
    if num == 30:
        return randomrunner(mypos, myfunds, distances)
    elif num == 31:
        return offlikeashot(mypos, myfunds, distances)
    elif num == 32:
        return steadyfreddy(mypos, myfunds, distances)
    elif num == 16:
        return ai(mypos, myfunds, distances)


players = [0] * 5
players[0] = int(input("Enter the AI number for the first team: "))
players[1] = int(input("Enter the AI number for the second team: "))
players[2] = int(input("Enter the AI number for the third team: "))
players[3] = int(input("Enter the AI number for the fourth team: "))
players[4] = int(input("Enter the AI number for the fifth team: "))
print("\nPositions at each stage in the race, followed by available funds.\n")

place = 1
rankings = [0] * 15
positions = [0] * 15
funds = [1000000] * 5
teamscores = [0] * 5

##############################
## CONTROLLER RUNS THE RACE ##
##############################

## GATHER BIDS, CLEAN UP VALUES

while funds[0] >= 0 or funds[1] >= 0 or funds[2] >= 0 or funds[3] >= 0 or funds[4] >= 0:
    bids = []
    distances = [random.randint(10, 19), random.randint(20, 29), random.randint(30, 39)]
    for j in range(0, 5):
        if funds[j] >= 0:
            mypos, myfunds = positions[:], funds[:]
            myfunds[0], myfunds[j] = myfunds[j], myfunds[0]
            mypos[0:3], mypos[3 * j:3 * j + 3] = mypos[3 * j:3 * j + 3], mypos[0:3]
            mybids = controller(players[j], mypos, myfunds, distances)
            total = 0
            for k in range(0, 3):
                value = max(int(mybids[k][1]), 0)
                total += value
                if total <= funds[j]:
                    mybids[k][1] = value
                else:
                    total -= value
                    mybids[k][1] = 0
                if rankings[3 * j + k] > 0:
                    mybids[k][1] = -1
                if mybids[k][0] not in ['short', 'medium', 'long']:
                    mybids[k][0] = 'short'
            bids += mybids
        else:
            bids += 3 * [['short', -1]]


            ## DETERMINE WINNING BIDS FOR EACH DISTANCE

    shortwinbid, mediumwinbid, longwinbid = -1, -1, -1
    for j in range(0, 15):
        if bids[j][0] == 'short':
            if bids[j][1] > shortwinbid:
                shortwinbid = bids[j][1]
                shortindex = j
        elif bids[j][0] == 'medium':
            if bids[j][1] > mediumwinbid:
                mediumwinbid = bids[j][1]
                mediumindex = j
        else:
            if bids[j][1] > longwinbid:
                longwinbid = bids[j][1]
                longindex = j


                ## ADVANCE RUNNERS, DEBIT ACCOUNTS, ASSIGN RANKS AS RUNNERS FINISH

    if longwinbid >= 0:
        index = int(longindex / 3)
        funds[index] -= longwinbid
        positions[longindex] = min(positions[longindex] + distances[2], 100)
        if positions[longindex] == 100 and rankings[longindex] == 0:
            rankings[longindex] = place
            place += 1
            if rankings[index * 3] > 0 and rankings[index * 3 + 1] > 0 and rankings[index * 3 + 2] > 0:
                funds[index] = -1
    if mediumwinbid >= 0:
        index = int(mediumindex / 3)
        funds[index] -= mediumwinbid
        positions[mediumindex] = min(positions[mediumindex] + distances[1], 100)
        if positions[mediumindex] == 100 and rankings[mediumindex] == 0:
            rankings[mediumindex] = place
            place += 1
            if rankings[index * 3] > 0 and rankings[index * 3 + 1] > 0 and rankings[index * 3 + 2] > 0:
                funds[index] = -1
    if shortwinbid >= 0:
        index = int(shortindex / 3)
        funds[index] -= shortwinbid
        positions[shortindex] = min(positions[shortindex] + distances[0], 100)
        if positions[shortindex] == 100 and rankings[shortindex] == 0:
            rankings[shortindex] = place
            place += 1
            if rankings[index * 3] > 0 and rankings[index * 3 + 1] > 0 and rankings[index * 3 + 2] > 0:
                funds[index] = -1

    for j in range(0, 5):
        score = 0
        for k in range(0, 3):
            if rankings[3 * j + k] > 0:
                score += 100 - (rankings[3 * j + k] * (rankings[3 * j + k] - 1)) / 2
        teamscores[j] = int(score)

    print(positions, funds)

print("\nFinal scores for each of the five teams.\n")
print(teamscores)
