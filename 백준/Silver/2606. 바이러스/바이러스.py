from collections import deque

def bfs(graph,start,visited):
    answer=0
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        answer+=1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
    print(answer-1) #1번컴퓨터 빼고 출력

n=int(input())
m=int(input())
computers=[[]for i in range(n+1)]
for i in range(m):
    x, y =map(int,input().split())
    computers[x].append(y)
    computers[y].append(x)
#print(computers)

visited =[False]*(n+1)
bfs(computers,1,visited)