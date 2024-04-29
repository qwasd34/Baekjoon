# import math
# def solution(progresses, speeds):
#     answer = []
#     que=[]
#     for i in range(len(progresses)):
#         que.append(math.ceil((100-progresses[i])/speeds[i]))
#     for i in range(len(que)-1):
#         cnt=1
#         if que[i]>=que[i+1]:
#             que[i+1]=que[i]
#     count={}
#     for i in que:
#         try:
#             count[i]+=1
#         except:
#             count[i]=1
#     answer=list(count.values())
        
        
#     return answer



import math
def solution(progresses, speeds):
    answer=[]
    day=[100-i for i in progresses ]
    result= [math.ceil(i/j) for i, j in zip(day, speeds)]
    #math.ceil() 소수점 올림함수
    #print(day)
    #print(result)                #[5,<10, 1, 1, <20, 1]
    st=[]
    st.append(result[0])        #st [5]
    for i in range(1,len(result)):
        #print("st[-1]=",st[-1],"result[i]=",result[i])
        if st[-1]>=result[i]:        #[5],[10,10,10],[20,20] 
            st.append(st[-1])        # st.append(result[i]) 반례 result=[2,1,2] 결과[3] but[2,1]
        else:
            answer.append(len(st))
            st=[]
            st.append(result[i])
        #print("st", "i","ans",st,i,answer)
    answer.append(len(st))
    return answer
   
