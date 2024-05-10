# 규칙 1 2 3 5 8 ... f(n)=f(n-1)+f(n-2) 피보나치 
def solution(n):
    f=[0]*(n+2)
    f[1]=1
    f[2]=2
    if n <= 3:
        return n
    for i in range(3, n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n] % 1234567
