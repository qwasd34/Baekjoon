# def solution(citations):
#     citations=sorted(citations,reverse=True)
    
#     answer,cnt=0,0
#     for i in range(len(citations)):
#         if i>=citations[i]:
#             answer=i
#             cnt=cnt+1
#             break
#     if cnt==0:
#         answer=len(citations)
#     return answer

def solution(citations):
    citations.sort()   # [0,1,3,5,6]
    
    answer=0
    for i in range(1,len(citations)+1):  
        num=citations[-i]  
        if num>=i:    #i=3일때, 뒤에서3번째 숫자까지 3번이상인용되어야 h-index=3, i=4일때 citations[-4]=1로 만족x
            answer=i
    return answer


