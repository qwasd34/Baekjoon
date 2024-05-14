import math
def solution(brown, yellow):
    answer = []
    y=int(math.sqrt(yellow))
    for i in range(1, y+1):
        if yellow%i==0:
            x=yellow//i
            y=i
            if x*2+y*2+4==brown:
                break
    
    answer.append(x+2)
    answer.append(y+2)
    return answer