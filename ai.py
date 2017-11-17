from random import shuffle

def ai(pos, funds, dist):
    import random
    valuepermeter = funds[0]/(350-pos[0]-pos[1]-pos[2])
    # to counter steadyfreddy?
    
    if valuepermeter <= 3333 and pos[0] < 25 or pos[1] < 25 or pos[2] < 25:
        valuepermeter = 3333 + random.randint(25, 300)
    '''
    if valuepermeter <= 3333 and pos[0] < 50 or pos[1] < 50 or pos[2] < 50:
        valuepermeter = 3333 + random.randint(25, 300)
    '''
    smallbid = valuepermeter*dist[0]
    midbid = valuepermeter*dist[1]
    bigbid = valuepermeter*dist[2]

    runnerpos = [pos[0], pos[1], pos[2]]
    
    values = [["short", smallbid], ["medium", midbid], ["long", bigbid]]

    bigRun = 0
    smallRun = 1

    for i in range(3):
        if runnerpos[i] > runnerpos[bigRun]:
            bigRun = i
        elif runnerpos[i] < runnerpos[smallRun]:
            smallRun = i
    
    midRun = [0, 1, 2]
    midRun.remove(bigRun)
    midRun.remove(smallRun)
    midRun = midRun[0]
    
    bids = [[], [], []]
    
    bids[smallRun] = ["long", bigbid]
    bids[bigRun] = ["short", smallbid]
    bids[midRun] = ["medium", midbid]
    
    return bids
