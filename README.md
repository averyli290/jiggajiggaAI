# jiggajiggaAI

###Strategy:

11/16/17
 - Find the average score of all the runners (the score of runners is calculated by 100-C(p, 2))
    - top 5: (100-(1 choose 2)+100-(2 choose 2)+100-(3 choose 2)+100-(4 choose 2)+100-(5 choose 2))/5 = 96
    - 6-10: (100-(6 choose 2)+100-(7 choose 2)+100-(8 choose 2)+100-(9 choose 2)+100-(10 choose 2))/5 = 71
    - 11-15: (100-(11 choose 2)+100-(12 choose 2)+100-(13 choose 2)+100-(14 choose 2)+100-(15 choose 2))/5 = 21
    
    - Average of all: (96+71+21)/3=62.666...
    
  - Bids based on self-value per remaining meter (remaining distance/remaining money)
    -hello i am text 