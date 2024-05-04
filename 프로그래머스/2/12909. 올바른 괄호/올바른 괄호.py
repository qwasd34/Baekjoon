# def solution(s):
#     stack=list(s)
#     rc,lc=0,0
#     for i in range(len(stack)):
#         if rc==lc:
#             rc,lc=0,0
#         if stack[-1]==')':
#             rc+=1
#             stack.pop()
    
#         elif rc!=0 and stack[-1]=='(':
#             lc+=1
#             stack.pop()

#         else:
#             return False
#     if rc==lc:
#         return True
#     else: return False


def solution(s):
    st=list(s)
    #print(st)
    R=0
    for i in range(len(st)):
        if st[-1]==')':
            st.pop()
            R+=1
        elif R!=0 and st[-1]=='(':
            st.pop()
            R-=1
        else:
            return False
    if R>0:
        return False
    return True


