# import itertools

# def solution(numbers):
#     numbers=list(map(str,numbers))
#     #print(numbers)
#     num=list(map(''.join,itertools.permutations(numbers))) #순열
#     #print(num)
#     return max(num)
import functools

def strCompare(num1,num2):
    #print(num1, num2)
    if num1+num2>num2+num1:
        return -1   #왼쪽위치
    else:
        return 1    #오른쪽위치
    
    # return 음수: 먼저들어온요소가 앞으로 정렬
    # return 0: 바뀌지않음
    # return 양수: 나중에 들어온 요소가 앞으로 정렬
    
def solution(numbers):
    # 문자열 리스트로 전환
    numbers=list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(strCompare))
    #print(numbers)
    answer=''.join(numbers)
    if numbers[0]=="0":
        answer='0'
        
    return answer