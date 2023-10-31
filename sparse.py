def split(l):
    l = l[::-1]
    l = [(l[i],i) for i in range(len(l))]
    print(l)
    A , B = [],[]
    i = 0
    canPutInA = True
    canPutInB = True
    while(i < len(l)):
        if(l[i][0] == 0 ):
            canPutInA = True
            canPutInB = True
        if(len(A) == 0 or  (l[i][1] - A[-1][1]) ==2):
            canPutInA=True
        if(len(B) == 0 or l[i][1] - B[-1][1] ==2):
            canPutInB=True
        if(not canPutInA and not canPutInB):
            return -1
        if(canPutInA):
            A.append(l[i])
            i +=1
            if(i < len(l)  and (A[-1][0] == 1  and l[i][0] == 1 and l[i][1] - A[-1][1] ==1 )  ):
                canPutInA = False
            
        elif(canPutInB):
            B.append(l[i])
            i+=1
            if(i<len(l) and B[-1][0] == 1  and l[i][0] == 1 and l[i][1] - B[-1][1] ==1):
                canPutInB = False
    print(A,B)
    if(i<len(l)):
        return [],[]

    return A,B


def solution(N):
    l = [int(i) for i in list('{0:0b}'.format(N))]
    res = split(l)[0]
    print(res)
    if(len(res) == 0):
        return -1
    R = 0
    for a in res:
        R += a[0] * 2**a[1]
    return R
    

print(solution(1023))