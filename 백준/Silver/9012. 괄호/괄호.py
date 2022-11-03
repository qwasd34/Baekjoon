n=int(input())


result=[]

for i in range(n):
    stack=[]
    #flag=True
    str=input()
    Pstring=list(str)
    f=True
    for j in Pstring:
        if j =="(":
            stack.append("(")
        if j==")":
            if len(stack)==0:
                f=False
                break
            else:
                stack.pop()
  
    if len(stack)==0 and f==True:
        result.append("YES")
    else:
        result.append("NO")
for r in result:
    print(r)
            
    

  