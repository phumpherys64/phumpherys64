#! /usr/local/bin/python3
from typing import List

def getSum(A: int, B: int, C: int) -> int:
    return A + B + C

def getWrongAnswers(N: int, C: str) -> str:
    # Ci ∈{‘‘A",‘‘B"}
    WrongAnswer = ''
    # for i in range(0, len(C)):
    for i in C:
        if i == "A":
            WrongAnswer += "B"
        else:
            WrongAnswer += "A"

    return WrongAnswer

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    cells = 0
    hits = 0
    for row in G:
        for hit in row:
            cells += 1
            hits += hit
    
    return hits / cells

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  
    # N is seats 1 to N
    # K is empty seats on both sides
    # M is diners seated at the table, the ith of whom is in seat
    # S[i]
    
    # 1 <= N <= 10^15
    # 1 <= K <= N
    # 1 <= M <= 500,000
    # M <= N
    # 1 <= S[i] <= N
    
    maxdiners = 0
    prev = 0
    dividend = None

    S = sorted(S, key=int, reverse=False)
    curr = S[0]
    for i in S[1:] + [None]:

        if prev == 0:
            available_seats = curr - 1 - K
        else:
            available_seats = curr - prev - 1 - K - K
        if available_seats < 0:
            available_seats = 0
        maxdiners += available_seats // K
                
        # print("prev:", prev, "curr:", curr, "next:", i, "mxdiners:", maxdiners, "availseats", available_seats)
        prev = curr
        curr = i
        
    else:
        available_seats = N - prev - K - 1
        if available_seats < 0:
            available_seats = 0
        maxdiners += available_seats // K
        # print("prev:", prev, "curr:", curr, "next:", i, "mxdiners:", maxdiners, "availseats", available_seats)
    
    
    return maxdiners

# print(getMaxAdditionalDinersCount(10000000000, 5, 9, [100000, 9, 87, 1000000, 1000, 1000000000, 5000, 20, 550000]))
print(getMaxAdditionalDinersCount(10, 1, 2, [2,6]))
# print(getMaxAdditionalDinersCount(10000000000, 2, 5, [14, 6, 2, 1000000, 1000000000]))
# print(getMaxAdditionalDinersCount(10000000000, 3, 5, [2,11,20,45,75]))
# print(getMaxAdditionalDinersCount(10000000000, 1, 5, [2,75,20,1000000,100000]))
# print(getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]))

# getWrongAnswers(4, "ABBA")
# result = getWrongAnswers(4, "ABBA")
# print(result)

# result = getSum(5,6,7)
# print(result)

# print(getHitProbability(2, 3, [[0,0,1], [1,0,1]]))

