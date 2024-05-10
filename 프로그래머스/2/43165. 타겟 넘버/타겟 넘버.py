def solution(numbers, target):
    arr=[0]
    for i in numbers:
        a=[]
        for j in arr:
            a.append(j+i)
            a.append(j-i)
        arr=a
    return arr.count(target)