def ai(pos, funds, dist):
    runner_pos = [pos[0], pos[1], pos[2]]
    runners_done = sum(100 == i for i in runner_pos)
    value_per_meter = (funds[0] - 150000) / (333 - pos[0] - pos[1] - pos[2])
    if runners_done == 2:
        value_per_meter = funds[0] / (300 - pos[0] - pos[1] - pos[2])
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
    if value_per_meter <= 3000 and (pos[0] < 50 or pos[1] < 50 or pos[2] < 50):
        value_per_meter = 3001
    '''

    small_bid = value_per_meter * dist[0]
    mid_bid = value_per_meter * dist[1]
    big_bid = value_per_meter * dist[2]

    if runners_done == 1:
        small_chunk = value_per_meter * dist[0] / 2
        small_bid = 0
        mid_bid = value_per_meter * dist[1] + small_chunk
        big_bid = value_per_meter * dist[2] + small_chunk
    elif runners_done == 2:
        mid_bid = value_per_meter * dist[1] + small_bid + big_bid
        small_bid = 0
        big_bid = 0

    big_run = 0
    small_run = 1

    for i in range(3):
        if runner_pos[i] > runner_pos[big_run]:
            big_run = i
        elif runner_pos[i] < runner_pos[small_run]:
            small_run = i
    
    mid_run = [0, 1, 2]
    mid_run.remove(big_run)
    mid_run.remove(small_run)
    mid_run = mid_run[0]
    
    bids = [[], [], []]
    
    bids[small_run] = ["long", big_bid]
    bids[big_run] = ["short", small_bid]
    bids[mid_run] = ["medium", mid_bid]
    
    return bids
