def ai(pos,funds,dist):
    import random
    print(pos)
    bid0 = 1000*dist[0]
    bid1 = 1000*dist[1]
    bid2 = 1000*dist[2]
    bids = [['short',bid0],['medium',bid1],['long',bid2]]
    random.shuffle(bids)
    return bids