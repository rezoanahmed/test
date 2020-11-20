while True:
    X = int(input())    
    if(X==0):
        break
    r = ""
    for i in range(1,X+1):
        r += str(i) + " "
    print(r[:-1])