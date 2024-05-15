from collections import deque
n,m=map(int,input().split())
maps=[]
for i in range(n):
    maps.append(list(map(int,input())))
#print(maps)

#상하좌우 설정
dx=[-1,1,0,0]
dy=[0,0,-1,1]



def bfs(maps):
    q=deque()
    q.append((0,0))     #시작지점 튜플로 append
    maps[0][0]=1    #시작점거리 1로 설정

    while q:    #큐가 비어있을때까지 반복
        x,y=q.popleft() 
        for i in range(4):  #현위치에서 네방향으로 위치 확인
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m:  #미로찾기 공간을 벗어난경우 무시
                continue
            if maps[nx][ny]==0:     #벽인경우 무시
                continue
            if nx==0 and ny==0: # 시작점으로 돌아간경우 무시
                continue
            if maps[nx][ny]==1: #해당노드를 처음방문한경우에만 최단거리 기록
                maps[nx][ny]=maps[x][y]+1   #인접노드 1-2222 기록 2-3333...
                q.append((nx,ny))
    return maps[n-1][m-1]
print(bfs(maps))

