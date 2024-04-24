def solution(n):
    n_list=list(range(1,n+1))
    cnt=0
    for i in range(n):
        sum=0
        for j in range(i,len(n_list)):
            sum+=n_list[j]
            if sum== n:
                cnt+=1
                break
            elif sum > n:
                break
    return cnt
    