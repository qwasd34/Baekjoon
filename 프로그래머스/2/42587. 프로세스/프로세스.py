from collections import deque
def solution(priorities, location):
    dq=deque(priorities)
    print(dq)
    answer=0
    while True:
        if location==0 and dq.index(max(dq))==0:
            answer+=1
            break
        print("dq[o]", dq[0], "max",max(dq))
        print(answer)
        if dq[0]<max(dq):
            dq.append(dq.popleft())
            if location!=0:
                location-=1
            else: 
                location+=len(dq)-1
        else:
            dq.popleft()
            location-=1
            answer+=1
        print(dq)
        print("loc",location , "answer",  answer)
        
    return answer
