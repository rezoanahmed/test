N = int(input())
for i in range(N):
    X,Y=list(map(int,input().split()))
    if(Y==0):
        print('divisao impossivel')
    elif(X==0):
        print(0.0)
    else:
        result = X/Y
        print('%.1f'%result)