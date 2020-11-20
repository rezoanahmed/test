while True:
    result = 0
    X = int(input())
    if(X==0):
        break
    for i in range(X,X+10):
        if(i%2==0):
            result = result + i
    print(result)