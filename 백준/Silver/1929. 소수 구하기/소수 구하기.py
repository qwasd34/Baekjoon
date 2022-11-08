import sys
input=sys.stdin.readline

def primenum(a):
    if a==1:
        return False
    cnt=0
    for i in range(2,a-1):
        if a%i==0:
            cnt+=1
    if cnt==0 or a==2:
        return True
    else:
        return False


def findnum(n,st):
    a=[True]*(n+1)
    k=int(n**0.5)
  
    for i in range(1,k+1):
        if primenum(i)==True:
           
            for j in range(i+i,n+1,i):
              
                a[j]=False
    return [i for i in range(st,n+1) if a[i]==True]


    
m,n=map(int,(input().split()))
answer=(findnum(n,m))

for i in answer:
    if i >=2:
        print(i)