def ai(pos, funds, dist):
    runnerpos = [pos[0], pos[1], pos[2]]
    runnersdone = sum(100 == i for i in runnerpos)
    valuepermeter = (funds[0] - 150000) / (333 - pos[0] - pos[1] - pos[2])
    if runnersdone == 2:
        valuepermeter = funds[0] / (300 - pos[0] - pos[1] - pos[2])
    '''
    value_per_meter0 = (funds[0]/3)/(111-pos[0])
    value_per_meter1 = (funds[0]/3)/(111-pos[1])
    value_per_meter2 = (funds[0]/3)/(111-pos[2])
    '''
    # to counter steadyfreddy?
    '''
    print(value_per_meter0)
    print(value_per_meter1)
    print(value_per_meter2)
    '''
    '''
    if valuepermeter <= 3000 and (pos[0] < 50 or pos[1] < 50 or pos[2] < 50):
        valuepermeter = 3001
    '''

    smallbid = valuepermeter * dist[0]
    midbid = valuepermeter * dist[1]
    bigbid = valuepermeter * dist[2]

    if runnersdone == 1:
        smallchunk = valuepermeter * dist[0] / 2
        smallbid = 0
        midbid = valuepermeter * dist[1] + smallchunk
        bigbid = valuepermeter * dist[2] + smallchunk
    elif runnersdone == 2:
        midbid = valuepermeter * dist[1] + smallbid + bigbid
        smallbid = 0
        bigbid = 0

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
