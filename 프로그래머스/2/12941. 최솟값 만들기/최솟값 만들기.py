def solution(A,B):
    A.sort()
    B.sort()
    B.reverse()
    answer=[i*j for i, j in zip(A,B)]
    print(sum(answer))
    return sum(answer)
  
