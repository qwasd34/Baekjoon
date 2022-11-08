import sys
input=sys.stdin.readline

n=int(input())


def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
    
for i in range(n):
    a,b=map(int,(input().split()))
    n=max(a,b)
    m=min(a,b)
    num=gcd(n,m)

    print((n*m)//num)
