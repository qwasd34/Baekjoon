n,m=map(int,(input().split()))
a=max(n,m)
b=min(n,m)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
print(gcd(a,b))   
print(n*m//gcd(a,b))