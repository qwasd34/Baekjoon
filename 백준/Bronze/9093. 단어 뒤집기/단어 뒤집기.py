import sys
n=int(input())

for i in range(n):
    sentence=[]
    sentence=sys.stdin.readline().rstrip().split()

    reversed_str=[]
    for j in sentence:
        reversed_str.append("".join(reversed(j)))
        result=' '.join(reversed_str)
    
    print(result)