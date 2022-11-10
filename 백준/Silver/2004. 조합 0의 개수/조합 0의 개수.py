

n,r=map(int,input().split())

def zero(n):
    five=0
    two=0
    for i in range(1, 14):
        if n>=5**i:
            five=five+n//5**i
        else:
            break
    for i in range(1,36):
        if n>=2**i:
            two=two+n//2**i
        else:
            break  
    return two,five
tupA=zero(n)
tupB=zero(r)
tupC=zero(n-r)

tupMultBC=tuple(sum(elem) for elem in zip(tupB,tupC))

num2=tupA[0]-tupMultBC[0]
num5=tupA[1]-tupMultBC[1]


if num2<=num5:
    print(num2)
else:
    print(num5)