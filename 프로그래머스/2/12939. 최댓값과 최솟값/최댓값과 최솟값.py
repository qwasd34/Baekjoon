


def solution(s):
    list_num=[int(i) for i in s.split()]
    print(list_num)
    answer=str(min(list_num))+' '+str(max(list_num))
    return answer
    
