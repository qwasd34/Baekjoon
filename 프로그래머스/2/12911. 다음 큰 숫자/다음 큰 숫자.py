def solution(n):
    n1=str(format(n,'b'))
    while True:
        k=str(format(n+1,'b'))
        if k.count('1')==n1.count('1'):
            answer=int(k,2)
            break
        else:
            n=n+1
    return answer