a,b = list(map(int,input().split()))
cont = 1
for i in range(1,(int(b/a)+1)):
    r = ''
    for j in range(a):
        r = r + str(cont) + ' '
        cont = cont + 1
    print(r[:-1])