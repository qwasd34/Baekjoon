
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)


n=int(input())
fac=list(map(int,str(factorial(n))))

cnt=0
for i in range(len(fac)-1,0,-1):
    if fac[i]==0:
        cnt+=1
    else:
        break 
print(cnt)

