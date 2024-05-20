

def dfs(family,x,f2,cnt):
    # 전역변수 
    global flag
    visited[x]=True
    #print(x)
    #print(f2)
    #print(visited)
    if x==f2:
        flag=True
        visited[x]=True
        print(cnt)
        return True
    for i in family[x]:
        if not visited[i]:
            dfs(family,i,f2,cnt+1)

n=int(input())
f1, f2=map(int, input().split())
m=int(input())
family=[[]for i in range(n+1)]
for i in range(m):
    x, y =map(int,input().split())
    family[x].append(y)
    family[y].append(x)
#print(family)

visited=[False]*(n+1)


flag=False
dfs(family,f1,f2,0)
if flag==False:
    print(-1)