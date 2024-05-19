import sys
#dfs 로 재귀함수 써서 풀기
sys.setrecursionlimit(10**6)

# maps=[]
# for i in range(n):
#     maps.append(list(map(int,input())))
#print(maps)


# 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    #print("재귀", x,y,cnt)
    #print(maps)
    #주어진 범위를 벗어나는 경우에는 즉시종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재노드를 방문 아직안했다면
    if maps[x][y]==1:
        #해당노드 방문처리
        #maps[x][y]=maps[x][y]+1
        maps[x][y]=0
        #상하좌우 위치도 모두 재귀적으로 호출\
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

 


#입력

t=int(input())
for q in range(t):
    n,m,k=map(int,input().split())
    maps=[[0]*m for q in range(n)]
    result=0

#행렬 생성
    for l in range(k):
        a,b=map(int, input().split())
        maps[a][b]=1



    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1
    print(result)
