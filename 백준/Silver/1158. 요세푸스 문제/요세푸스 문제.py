import sys
from collections import deque
input=sys.stdin.readline

que=deque()

n,cyclenum=map(int,input().split())
result=[]
cnt=1

for i in range(1,n+1):
    que.append(i)


while len(que)!=0:
    if cnt==cyclenum:
        num=que.popleft()
        result.append(num)
        cnt=cnt-cyclenum+1
    
    else:
        num=que.popleft()
        que.append(num)
        cnt+=1



answer=', '.join(map(str,result))

print("<"+answer+">")