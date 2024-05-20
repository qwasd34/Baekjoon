from collections import deque

def dfs(graph, v, visited):
    #print(visited)
    #현재 노드를 방문처리
    visited[v]=True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # 큐 구현
    q=deque([start])
    #현재노드 방문처리
    visited[start]=True
    #큐가 빌때까지 반복
    while q:
        #큐에서 원소 뽑아 출력
        v=q.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문하지않은 원소들을 큐에삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True



n, m, v=map(int, input().split())
graph=[[]for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
#작은 숫자 부터 방문하기 위해 sort()이용
for i in graph:
    i.sort()
#print(graph)

visited1=[False]*(n+1)
visited2=[False]*(n+1)
dfs(graph, v, visited1) 
print()
bfs(graph, v, visited2)