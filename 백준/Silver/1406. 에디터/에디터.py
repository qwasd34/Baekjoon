import sys
input=sys.stdin.readline


str=input().strip()
s_list=list(str)
n=int(input())
point=len(s_list)
stack=[]

for i in range(n):
    cmd=input()
    if "L" in cmd:
        if point!=0:
            num=s_list.pop()
            stack.append(num)
            point-=1
    if "D" in cmd:
        if len(stack)!=0:
            num=stack.pop()
            s_list.append(num)
            point+=1
    if "B" in cmd:
        if point!=0:
            s_list.pop()
            point-=1
    if "P" in cmd:
        word=cmd[2]
        s_list.append(word)
        point+=1

for i in range(len(stack)):
    num=stack.pop()
    s_list.append(num)    
answer=''.join(i for i in s_list)
print(answer)



        