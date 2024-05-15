from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    print(n,m)
    # 좌표 구하기 (상하좌우)
    dx = [0, 0, 1, -1]  # 행
    dy = [1, -1, 0, 0]  # 열
    
    que = deque()
    que.append((0, 0))  # x, y 튜플 형태로
    maps[0][0] = 1  # 시작점의 거리를 1로 설정
    
    # 큐가 빌 때까지 반복
    while que:
        #print(que)
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #print(nx,ny)
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if maps[nx][ny] == 0 :
                continue
            if nx==0 and ny==0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                que.append((nx, ny))
        
        answer = maps[n - 1][m - 1]
      
    # 만약 오른쪽 아래 모서리가 1이거나 원래의 값과 같다면, 도달할 수 없음을 의미
    if answer == maps[0][0] or answer==1:
        return -1
    else:
        return answer
    
