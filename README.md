# jiggajiggaAI

# Strategy:

Variables:
  - valuepermeter:
     Average value per meter for each runner
  - smallbid, midbid, bigbid:
     How much you are willing to bid for each runner
  - runners:
     A dictionary of the runners containing first the bids of the runners, then the runner number
  - smallRun, midRun, bigRun:
     The runner that needs the most meters, middle amount of meters, and then the least meters to finish the race
     \
     

11/16/17
 - Find the average score of all the runners (the score of runners is calculated by 100-C(p, 2))
    - top 5: (100-(1 choose 2)+100-(2 choose 2)+100-(3 choose 2)+100-(4 choose 2)+100-(5 choose 2))/5 = 96
    - 6-10: (100-(6 choose 2)+100-(7 choose 2)+100-(8 choose 2)+100-(9 choose 2)+100-(10 choose 2))/5 = 71
    - 11-15: (100-(11 choose 2)+100-(12 choose 2)+100-(13 choose 2)+100-(14 choose 2)+100-(15 choose 2))/5 = 21
    
    - Average of all: (96+71+21)/3 = 62.666...
 
 - Total score of all runners
    - (62+2/3)x15 = 960
    - Average for every team: 960/5 = 232
