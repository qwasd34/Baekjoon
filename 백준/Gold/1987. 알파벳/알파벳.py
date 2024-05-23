# 알파벳 리스트 만들어서 count 하기 ASCII 값으로
# dfs
# 4방향, 범위내, 중복값아님


import sys

input = sys.stdin.readline

def dfs(ci,cj,cnt):
    global ans
    ans=max(cnt,ans)

    # 4방향설정 
    for di,dj in((-1,0),(1,0),(0,-1),(0,1)):
        ni=ci+di
        nj=cj+dj
        if 0<=ni<R and 0<=nj<C and v[ord(arr[ni][nj])]==0:
            v[ord(arr[ni][nj])]=1
            dfs(ni,nj,cnt+1)
            v[ord(arr[ni][nj])]=0
        


R,C=map(int,input().split())
arr = list(input() for i in range(R))

ans = 1 #한군데는 무조건 시작 
v= [0]*128 #Ascii code 
v[ord(arr[0][0])]=1 # 해당값사용
dfs(0,0,1)
print(ans)
