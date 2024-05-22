# RecursionError
# Python 이정한 최대 재귀 깊이 sys.getrecursionlimit() 확인 가능
# BOJ 서버는 1,000

# 최대 재귀 깊이 1,000,000로설정
import sys
sys.setrecursionlimit(10**6)


from collections import deque 

def dfs(x,y):
    #범위에서 나가면 즉시 종료
    if x<0 or x>=h or y<0 or y>=w:
        return False
    # 만약 섬이면, 상,하 ,좌,우 위치도 모두 재귀적 호출 대각선도해야함..
    #print("xy",x,y)
    #print("re",land)
    if land[x][y]==1:
        land[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y-1)
        dfs(x+1,y+1)
        return True
    return False

while True:
    land=[]
    w,h=map(int, input().split())
    # 0 0 이들어오면 break
    if w==0 and h==0:
        break
    land =[list(map(int, input().split())) for i in range(h)]
    #print(land)
    #섬의 개수 카운트
    result=0
    # 모든 노드에 대하여 체크하기
    for i in range(h):
        for j in range(w):
            # 1이 1개라도 있으면 true
            if dfs(i,j)==True:
                result+=1
    #print(land)
    print(result)