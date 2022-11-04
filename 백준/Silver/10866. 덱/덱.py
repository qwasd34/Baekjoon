import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
que=deque()

for i in range(n):
    cmd=input().rstrip()
    if "push_front" in cmd:
        num=cmd[11:]
        que.appendleft(num)
    elif "push_back" in cmd:
        num=cmd[10:]
        que.append(num)
    elif "pop_front" in cmd:
        if len(que)==0:
            print("-1")
        else:
            print(que.popleft())
    elif "pop_back" in cmd:
        if len(que)==0:
            print("-1")
        else:
            print(que.pop())
    elif cmd=="size":
        print(len(que))
    elif cmd=="empty":
        if len(que)==0:
            print("1")
        else:
            print("0")
    elif cmd=="front":
        if len(que)==0:
            print("-1")
        else:
           print(que[0])
    elif cmd=="back":
        if len(que)==0:
            print("-1")
        else:
            print(que[-1])
