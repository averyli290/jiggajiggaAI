def ai(pos, funds, dist):
    valuepermeter = funds[0] / (300-pos[0]-pos[1]-pos[2])
    smallbid = valuepermeter*dist[0]
    midbid = valuepermeter*dist[1]
    bigbid = valuepermeter*dist[2]
    return [["short", smallbid], ["medium", midbid], ["long", bigbid]]
