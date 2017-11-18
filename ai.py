from random import shuffle

def ai(pos, funds, dist):
    import random
    valuepermeter = funds[0]/(333-pos[0]-pos[1]-pos[2])
    '''
    valuepermeter0 = (funds[0]/3)/(111-pos[0])
    valuepermeter1 = (funds[0]/3)/(111-pos[1])
    valuepermeter2 = (funds[0]/3)/(111-pos[2])
    '''
    # to counter steadyfreddy?
    '''
    print(valuepermeter0)
    print(valuepermeter1)
    print(valuepermeter2)
    '''
    '''
    if valuepermeter <= 3000 and (pos[0] < 50 or pos[1] < 50 or pos[2] < 50):
        valuepermeter = 3001
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
