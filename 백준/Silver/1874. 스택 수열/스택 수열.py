import sys
input=sys.stdin.readline

class Stack():
    def __init__(self):
        self.stack=[]
    
    def push(self,num):
        self.stack.append(num)
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

    def top(self):
        if len(self.stack)==0:
            return -1
        return self.stack[-1]   

    def see(self):
        print(self.stack) 
    
#main
n=int(input())
sequence=[]
result=[]
cnt=0
st=Stack()
result=[]
k=1
answer=[]
for i in range(n):

    num=int(input())
    sequence.append(num)
#print(sequence)

while cnt<n:
    if k>n+1:
        break
    #print(sequence[cnt])
    #print("top",st.top())
    #print("k",k)
    if sequence[cnt]==st.top():
        j=st.pop()
        result.append(j)
        cnt+=1
        answer.append("-")
    elif sequence[cnt]!=st.top():
        st.push(k)
        k+=1
        answer.append("+")
        
    #st.see()
    #print("cnt",cnt)
    #print("result",result)
#st.see()

if result==sequence:
    for i in answer:
        print(i)
else:
    print("NO")

