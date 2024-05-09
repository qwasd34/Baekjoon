def solution(people, limit):
    answer = 0
    people.sort()
    cnt=0
    i=0 #가장 가벼운 사람
    h=len(people)-1 #가장 무거운사람
    while i<=h:
        cnt+=1
        if people[i]+people[h]<=limit:
            i+=1
        h-=1
    return cnt


            
    

