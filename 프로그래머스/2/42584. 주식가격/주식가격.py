def solution(prices):
    stack=[]
    for i in range(len(prices)):
        cnt=0
        for j in range(1,len(prices)-i):
            if prices[i]<=prices[i+j]:
                cnt+=1
                
            else:
                cnt+=1
                break
        stack.append(cnt)
        
    return stack