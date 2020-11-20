X = int(input())
Y = int(input())
temp = X
if(x>y):
    X = Y
    Y = temp
while(X<Y):
    if(X%5==2 or X%5==3 and X!=Y):
        print(X)
    X+=1