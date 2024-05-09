def solution(people, limit):
    people.sort()
    cnt=0
    i=0 #가장 가벼운 사람
    h=len(people)-1 #가장 무거운사람
    while i<=h: # 가장 가벼운 사람의 인덱스가 가장 무거운 사람의 인덱스보다 작거나 같을 때까지 반복
        if people[i]+people[h]<=limit:
            i+=1    #다음으로 가벼운 사람 선택
        h-=1    #다음으로 무거운사람선택
        cnt+=1  #보트 증가
    return cnt

# from collections import deque

# def solution(people, limit):
#     people.sort()
#     dq=deque(people)
#     answer=0
#     while dq:           # dq가 비어있지 않은 동안 계속 실행합니다.
#         if len(dq)>=2 and dq[-1]+dq[0]<=limit:  # dq에 두 명 이상의 사람이 있고, 무게의 합이 limit보다 작거나 같으면 앞에 조건 x해주면 pop() 오류 
#             dq.pop()
#             dq.popleft()
#             answer+=1
#         else:
#             dq.pop()
#             answer+=1
#     return answer
        
            
    

