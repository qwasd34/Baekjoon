def solution(people, limit):
    people.sort()
    cnt=0
    i=0 #가장 가벼운 사람
    h=len(people)-1 #가장 무거운사람
    while i<=h:
        if people[i]+people[h]<=limit:
            i+=1
        h-=1
        cnt+1
    return cnt

"""from collections import deque

def solution(people, limit):
    people.sort()
    dq=deque(people)
    answer=0
    while dq:
        if len(dq)>=2 and dq[-1]+dq[0]<=limit:
            dq.pop()
            dq.popleft()
            answer+=1
        else:
            dq.pop()
            answer+=1
    return answer"""
        
            
    

