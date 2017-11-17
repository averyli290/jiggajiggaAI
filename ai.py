from random import shuffle

def ai(pos, funds, dist):
    valuepermeter = funds[0] / (300-pos[0]-pos[1]-pos[2])
    smallbid = valuepermeter*dist[0]
    midbid = valuepermeter*dist[1]
    bigbid = valuepermeter*dist[2]

    d = {100 - pos[0]: 0, 100 - pos[1]: 1, 100 - pos[2]: 2}

    values = [["short", smallbid], ["medium", midbid], ["long", bigbid]]

    bids = [[],[],[]]

    runnerpos = [pos[0], pos[1], pos[2]]

    bigRun = runnerpos.index(max(runnerpos))
    smallRun = runnerpos.index(min(runnerpos))
    midRun = 0
    for i in runnerpos:
        if i is not bigRun and i is not smallRun:
            midRun = i

    bids[smallRun] = ["long", bigbid]
    bids[bigRun] = ["short", smallbid]
    bids[midRun] = ["medium", midbid]

    return bids
