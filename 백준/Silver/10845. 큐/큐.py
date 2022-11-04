import sys
from queue import Queue
#queue 모듈의 Queue 클래스 사용

input=sys.stdin.readline

queue=Queue()

n=int(input())
for i in range(n):
    cmd=input().strip()
    if "push" in cmd:
        num=cmd[5:]
        queue.put(num)
    elif cmd=="pop":
        if queue.empty():
            print("-1")
        else:
            print(queue.get())
    elif "size" in cmd:
        print(queue.qsize())
    elif cmd=="empty":
        if queue.empty():
            print("1")
        else:
            print("0")
    elif cmd=="front":
        if queue.empty():
            print("-1")
        else:
            print(queue.queue[0])
    elif cmd=="back":
        if queue.empty():
            print("-1")
        else:
            print(queue.queue[-1])
    


