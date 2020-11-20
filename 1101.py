while True:
    sum = 0
    M,N = list(map(int,input().split()))
    temp = M
    if(M>N):
        M = N
        N = temp
    if(M==0 or N==0):
        break
    else:
        for i in range(M,N+1):
            sum = sum + i
            print(i, end=" ")
        print('Sum=%d'%(sum))