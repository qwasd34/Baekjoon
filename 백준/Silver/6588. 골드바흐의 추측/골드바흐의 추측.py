import sys
input=sys.stdin.readline

arr=[True]*(1000001)
    #m=int(n**0.5)
for i in range(2,1001):
    if arr[i]==True:
        for j in range(i+i,1000001,i):
            arr[j]=False


while True:
    num=int(input())
    if num==0:
        break
    for i in range(3,num):
        if arr[i]==True and arr[num-i]==True:
            print(num,"=",i,"+",num-i)
            break
 
    else:
        print("Goldbach's conjecture is wrong")