
def solution(s):
    zcnt=0
    cnt=0
    while True:
        if s=="1":
            break
        zcnt+=s.count('0')
        print(s.count('0'))
        s=s.replace('0','')
        num=len(s)
        s=format(num,'b')
        cnt+=1
        

        
        answer = [cnt,zcnt]
    return answer