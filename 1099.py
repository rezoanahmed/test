N = int(input())
for num in range(N):
    sum = 0
    a,b = input().split()
    if(int(a)<int(b)):
        for i in range(int(a)+1,int(b)):
            if(i%2!=0):
                sum = (sum + i)
        print(sum)
    elif(int(a)>int(b)):
        for i in range(int(b)+1,int(a)):
            if(i%2!=0):
                sum = (sum + i)
        print(sum)
    else:
        print(0)