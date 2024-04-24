def solution(nums):
    n=int(len(nums)/2)
    list_n=list(set(nums))
    if len(list_n)<=n:
        answer=len(list_n)
    else:
        answer=n

    
    
    return answer