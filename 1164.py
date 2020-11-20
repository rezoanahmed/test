N = int(input())
for num in range(N):
    X = int(input())
    result = 0
    for i in range(1,X):
        if(X%i==0):
            result = result + i
    if(X == result):
        print(X,'eh perfeito')
    else:
        print(X,'nao eh perfeito')