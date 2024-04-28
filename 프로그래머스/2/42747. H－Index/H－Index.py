def solution(citations):
    citations=sorted(citations,reverse=True)
    
    answer,cnt=0,0
    for i in range(len(citations)):
        if i>=citations[i]:
            answer=i
            cnt=cnt+1
            break
    if cnt==0:
        answer=len(citations)
    return answer


