import itertools
#dfs 로 재귀함수 써서 풀기
n=int(input())
maps=[]
for i in range(n):
    maps.append(list(map(int,input())))
#print(maps)


# 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y,cnt):
    #print("재귀", x,y,cnt)
    #print(maps)
    #주어진 범위를 벗어나는 경우에는 즉시종료
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    #현재노드를 방문 아직안했다면
    if maps[x][y]==1:
        #해당노드 방문처리
        maps[x][y]=maps[x][y]+cnt
        #상하좌우 위치도 모두 재귀적으로 호출\
        dfs(x-1,y,cnt)
        dfs(x,y-1,cnt)
        dfs(x+1,y,cnt)
        dfs(x,y+1,cnt)
        return True
    return False

    #모든노드위치에대해 집채우기

result=1

for i in range(n):
    for j in range(n):
        if dfs(i,j,result)==True:
            result+=1
print(result-1)
answer=[]
#print(maps)
# 이중리스트 해제하기
mp=list(itertools.chain(*maps))
#print(mp)
for i in range(2,result+1):
    answer.append(mp.count(i))
answer.sort()


for i in answer:
    print(i)

